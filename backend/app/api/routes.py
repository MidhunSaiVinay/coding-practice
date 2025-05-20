from __future__ import annotations

import base64
import zlib
from typing import Any, Literal
import logging
import time

import numpy as np
import yfinance as yf
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.montecarlo.engine import MonteCarloEngine
from app.risk.metrics import RiskMetrics

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


class SimulationRequest(BaseModel):
    """Request model for Monte Carlo simulation."""
    model: Literal["gbm", "jump_diffusion", "heston"] = "gbm"
    tickers: list[str] = Field(..., min_items=1)
    params: dict[str, Any]
    n_paths: int = Field(..., gt=0, le=100000)
    horizon: int = Field(..., gt=0, le=2520)  # Max 10 years
    seed: int | None = None


class SimulationResponse(BaseModel):
    """Response model for Monte Carlo simulation."""
    stats: dict[str, float]
    paths: str  # base64-zstd compressed array
    variances: str | None = None  # For Heston model


def validate_ticker(ticker: str) -> str:
    """
    Validate and format ticker symbol for Yahoo Finance.
    
    Args:
        ticker: Input ticker symbol
        
    Returns:
        Formatted ticker symbol
    """
    # Remove any whitespace
    ticker = ticker.strip().upper()
    
    # Handle common index formats
    if ticker.startswith("^"):
        return ticker
    
    # Handle forex pairs
    if "=" in ticker:
        return ticker
    
    # Handle cryptocurrency
    if "-" in ticker:
        return ticker
    
    # Handle futures
    if ".F" in ticker:
        return ticker
    
    # Handle foreign stocks
    if "." in ticker:
        return ticker
    
    # For US stocks, ensure it's clean
    return ticker


def fetch_stock_data(ticker: str, max_retries: int = 3) -> float:
    """
    Fetch stock data from yfinance with retries.
    
    Args:
        ticker: Stock ticker symbol
        max_retries: Maximum number of retry attempts
        
    Returns:
        Latest closing price
        
    Raises:
        HTTPException: If data cannot be fetched after retries
    """
    # Validate and format ticker
    formatted_ticker = validate_ticker(ticker)
    logger.info(f"Fetching data for ticker: {formatted_ticker} (original: {ticker})")
    
    for attempt in range(max_retries):
        try:
            logger.info(f"Attempt {attempt + 1}/{max_retries} for {formatted_ticker}")
            
            # Try downloading data directly first
            data = yf.download(
                formatted_ticker,
                period="1d",
                interval="1d",
                progress=False,
                ignore_tz=True,
                group_by="ticker"
            )
            
            if data.empty:
                logger.warning(f"No data found using download method for {formatted_ticker}, trying Ticker object...")
                # If download fails, try using Ticker object
                ticker_obj = yf.Ticker(formatted_ticker)
                data = ticker_obj.history(
                    period="1d",
                    interval="1d",
                    auto_adjust=True,
                    prepost=False
                )
                
                if data.empty:
                    raise ValueError(f"No price data available for {formatted_ticker}")
            
            # Verify we have valid data
            if "Close" not in data.columns:
                raise ValueError(f"Missing Close price data for {formatted_ticker}")
            
            price = float(data["Close"].iloc[-1])
            if price <= 0:
                raise ValueError(f"Invalid price data for {formatted_ticker}: {price}")
            
            logger.info(f"Successfully fetched price for {formatted_ticker}: ${price:.2f}")
            return price
            
        except Exception as e:
            logger.error(f"Error fetching data for {formatted_ticker} (attempt {attempt + 1}): {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in 2 seconds...")
                time.sleep(2)  # Increased delay between retries
            else:
                error_msg = (
                    f"Could not fetch data for {formatted_ticker} after {max_retries} attempts. "
                    f"Please verify the ticker symbol and try again. "
                    f"Error: {str(e)}"
                )
                logger.error(error_msg)
                raise HTTPException(status_code=404, detail=error_msg)


@router.post("/simulate")
async def simulate(request: SimulationRequest) -> SimulationResponse:
    """
    Run Monte Carlo simulation and return paths and statistics.
    
    Args:
        request: Simulation parameters
        
    Returns:
        Simulation results including statistics and compressed paths
    """
    try:
        # Get initial prices from yfinance
        prices = {}
        for ticker in request.tickers:
            try:
                prices[ticker] = fetch_stock_data(ticker)
            except HTTPException as e:
                # Re-raise the HTTPException to preserve the error message
                raise e
            except Exception as e:
                logger.error(f"Unexpected error fetching data for {ticker}: {str(e)}")
                raise HTTPException(
                    status_code=500,
                    detail=f"Unexpected error fetching data for {ticker}: {str(e)}"
                )

        # Run simulation based on model
        if request.model == "gbm":
            paths = []
            for ticker in request.tickers:
                try:
                    path = MonteCarloEngine.geometric_brownian_motion(
                        s0=prices[ticker],
                        mu=request.params.get("mu", 0.0),
                        sigma=request.params.get("sigma", 0.2),
                        t=request.horizon / 252,  # Convert to years
                        n_steps=request.horizon,
                        n_paths=request.n_paths,
                        seed=request.seed,
                    )
                    paths.append(path)
                except Exception as e:
                    logger.error(f"Error in GBM simulation for {ticker}: {str(e)}")
                    raise HTTPException(
                        status_code=500,
                        detail=f"Error in simulation for {ticker}: {str(e)}"
                    )
            variances = None

        elif request.model == "jump_diffusion":
            paths = []
            for ticker in request.tickers:
                path = MonteCarloEngine.jump_diffusion(
                    s0=prices[ticker],
                    mu=request.params.get("mu", 0.0),
                    sigma=request.params.get("sigma", 0.2),
                    lambda_jump=request.params.get("lambda_jump", 0.1),
                    mu_jump=request.params.get("mu_jump", -0.1),
                    sigma_jump=request.params.get("sigma_jump", 0.1),
                    t=request.horizon / 252,
                    n_steps=request.horizon,
                    n_paths=request.n_paths,
                    seed=request.seed,
                )
                paths.append(path)
            variances = None

        elif request.model == "heston":
            paths = []
            var_paths = []
            for ticker in request.tickers:
                price_path, var_path = MonteCarloEngine.heston_model(
                    s0=prices[ticker],
                    v0=request.params.get("v0", 0.04),
                    kappa=request.params.get("kappa", 2.0),
                    theta=request.params.get("theta", 0.04),
                    sigma_v=request.params.get("sigma_v", 0.3),
                    rho=request.params.get("rho", -0.7),
                    t=request.horizon / 252,
                    n_steps=request.horizon,
                    n_paths=request.n_paths,
                    seed=request.seed,
                )
                paths.append(price_path)
                var_paths.append(var_path)
            variances = base64.b64encode(zlib.compress(np.array(var_paths).tobytes())).decode()
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Model {request.model} not yet implemented",
            )

        # Calculate returns and statistics
        returns = np.diff(paths[0], axis=1) / paths[0][:, :-1]
        stats = RiskMetrics.historical_stats(returns.flatten())

        # Compress paths for efficient transfer
        paths_bytes = np.array(paths).tobytes()
        compressed = zlib.compress(paths_bytes)
        encoded = base64.b64encode(compressed).decode()

        return SimulationResponse(stats=stats, paths=encoded, variances=variances)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in simulation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/data/{ticker}")
async def get_market_data(ticker: str) -> dict[str, Any]:
    """
    Get OHLC data for a ticker from yfinance.
    
    Args:
        ticker: Stock ticker symbol
        
    Returns:
        Dictionary containing OHLC data
    """
    try:
        data = yf.download(ticker, period="1y")
        if data.empty:
            raise HTTPException(status_code=404, detail=f"No data found for {ticker}")
            
        return {
            "dates": data.index.strftime("%Y-%m-%d").tolist(),
            "open": data["Open"].tolist(),
            "high": data["High"].tolist(),
            "low": data["Low"].tolist(),
            "close": data["Close"].tolist(),
            "volume": data["Volume"].tolist(),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
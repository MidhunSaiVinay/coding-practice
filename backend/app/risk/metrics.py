from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
import scipy.stats


class RiskMetrics:
    """Collection of risk metrics for financial time series."""

    @staticmethod
    def value_at_risk(
        returns: NDArray[np.float64],
        confidence_level: float = 0.95,
    ) -> float:
        """
        Calculate Value at Risk (VaR) at specified confidence level.
        
        Args:
            returns: Array of returns
            confidence_level: Confidence level (e.g., 0.95 for 95% VaR)
            
        Returns:
            VaR at specified confidence level
        """
        return np.percentile(returns, (1 - confidence_level) * 100)

    @staticmethod
    def conditional_var(
        returns: NDArray[np.float64],
        confidence_level: float = 0.95,
    ) -> float:
        """
        Calculate Conditional Value at Risk (CVaR) / Expected Shortfall.
        
        Args:
            returns: Array of returns
            confidence_level: Confidence level (e.g., 0.95 for 95% CVaR)
            
        Returns:
            CVaR at specified confidence level
        """
        var = RiskMetrics.value_at_risk(returns, confidence_level)
        return -np.mean(returns[returns <= -var])

    @staticmethod
    def sharpe_ratio(
        returns: NDArray[np.float64],
        risk_free_rate: float = 0.0,
        periods_per_year: int = 252,
    ) -> float:
        """
        Calculate annualized Sharpe ratio.
        
        Args:
            returns: Array of returns
            risk_free_rate: Annual risk-free rate
            periods_per_year: Number of periods in a year
            
        Returns:
            Annualized Sharpe ratio
        """
        excess_returns = returns - risk_free_rate / periods_per_year
        return np.sqrt(periods_per_year) * np.mean(excess_returns) / np.std(excess_returns)

    @staticmethod
    def max_drawdown(returns: NDArray[np.float64]) -> float:
        """
        Calculate maximum drawdown from peak.
        
        Args:
            returns: Array of returns
            
        Returns:
            Maximum drawdown as a positive percentage
        """
        cumulative = (1 + returns).cumprod()
        running_max = np.maximum.accumulate(cumulative)
        drawdown = (running_max - cumulative) / running_max
        return np.max(drawdown)

    @staticmethod
    def historical_stats(returns: NDArray[np.float64]) -> dict[str, float]:
        """
        Calculate key historical statistics.
        
        Args:
            returns: Array of returns
            
        Returns:
            Dictionary of statistics including mean, std, skew, kurtosis
        """
        return {
            "mean": np.mean(returns),
            "std": np.std(returns),
            "skew": float(scipy.stats.skew(returns)),
            "kurtosis": float(scipy.stats.kurtosis(returns)),
            "var_95": RiskMetrics.value_at_risk(returns, 0.95),
            "cvar_95": RiskMetrics.conditional_var(returns, 0.95),
            "sharpe": RiskMetrics.sharpe_ratio(returns),
            "max_dd": RiskMetrics.max_drawdown(returns),
        } 
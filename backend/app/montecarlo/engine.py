from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from scipy.stats import norm


class MonteCarloEngine:
    """Core Monte Carlo simulation engine with various stochastic processes."""

    @staticmethod
    def geometric_brownian_motion(
        s0: float,
        mu: float,
        sigma: float,
        t: float,
        n_steps: int,
        n_paths: int,
        seed: int | None = None,
    ) -> NDArray[np.float64]:
        """
        Generate Geometric Brownian Motion paths.
        
        Args:
            s0: Initial price
            mu: Drift rate
            sigma: Volatility
            t: Time horizon
            n_steps: Number of time steps
            n_paths: Number of simulation paths
            seed: Random seed for reproducibility
            
        Returns:
            Array of shape (n_paths, n_steps + 1) containing simulated paths
        """
        if seed is not None:
            np.random.seed(seed)
            
        dt = t / n_steps
        # Generate random increments
        dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))
        
        # Calculate drift and diffusion terms
        drift = (mu - 0.5 * sigma**2) * dt
        diffusion = sigma * dW
        
        # Generate paths
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = s0
        
        # Vectorized path generation
        paths[:, 1:] = s0 * np.exp(
            np.cumsum(drift + diffusion, axis=1)
        )
        
        return paths

    @staticmethod
    def jump_diffusion(
        s0: float,
        mu: float,
        sigma: float,
        lambda_jump: float,
        mu_jump: float,
        sigma_jump: float,
        t: float,
        n_steps: int,
        n_paths: int,
        seed: int | None = None,
    ) -> NDArray[np.float64]:
        """
        Merton's Jump-Diffusion model implementation.
        
        The model combines geometric Brownian motion with compound Poisson jumps:
        dS_t = S_t * (mu * dt + sigma * dW_t + (exp(J) - 1) * dN_t)
        where J ~ N(mu_jump, sigma_jump^2) and N_t is a Poisson process with intensity lambda_jump.
        
        Args:
            s0: Initial price
            mu: Drift rate
            sigma: Volatility
            lambda_jump: Jump intensity
            mu_jump: Mean jump size
            sigma_jump: Jump size volatility
            t: Time horizon
            n_steps: Number of time steps
            n_paths: Number of simulation paths
            seed: Random seed for reproducibility
            
        Returns:
            Array of shape (n_paths, n_steps + 1) containing simulated paths
        """
        if seed is not None:
            np.random.seed(seed)
            
        dt = t / n_steps
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = s0
        
        # Generate Brownian motion increments
        dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))
        
        # Generate Poisson jumps
        jump_prob = lambda_jump * dt
        jumps = np.random.poisson(jump_prob, (n_paths, n_steps))
        
        # Generate jump sizes
        jump_sizes = np.random.normal(mu_jump, sigma_jump, (n_paths, n_steps))
        
        # Calculate drift term (adjusted for jumps)
        drift = (mu - 0.5 * sigma**2 - lambda_jump * (np.exp(mu_jump + 0.5 * sigma_jump**2) - 1)) * dt
        
        # Generate paths
        for i in range(n_steps):
            # Diffusion term
            diffusion = sigma * dW[:, i]
            
            # Jump term
            jump_term = np.exp(jump_sizes[:, i]) - 1
            jump_term *= jumps[:, i]
            
            # Update paths
            paths[:, i + 1] = paths[:, i] * np.exp(drift + diffusion + jump_term)
        
        return paths

    @staticmethod
    def heston_model(
        s0: float,
        v0: float,
        kappa: float,
        theta: float,
        sigma_v: float,
        rho: float,
        t: float,
        n_steps: int,
        n_paths: int,
        seed: int | None = None,
    ) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Heston stochastic volatility model implementation.
        
        The model consists of two coupled SDEs:
        dS_t = S_t * sqrt(V_t) * dW_1
        dV_t = kappa * (theta - V_t) * dt + sigma_v * sqrt(V_t) * dW_2
        where dW_1 and dW_2 are correlated Brownian motions with correlation rho.
        
        Args:
            s0: Initial price
            v0: Initial variance
            kappa: Mean reversion speed
            theta: Long-run variance
            sigma_v: Volatility of volatility
            rho: Correlation between price and variance
            t: Time horizon
            n_steps: Number of time steps
            n_paths: Number of simulation paths
            seed: Random seed for reproducibility
            
        Returns:
            Tuple of (price paths, variance paths)
        """
        if seed is not None:
            np.random.seed(seed)
            
        dt = t / n_steps
        
        # Initialize arrays
        prices = np.zeros((n_paths, n_steps + 1))
        variances = np.zeros((n_paths, n_steps + 1))
        prices[:, 0] = s0
        variances[:, 0] = v0
        
        # Generate correlated Brownian motions
        dW1 = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))
        dW2 = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))
        dW2 = rho * dW1 + np.sqrt(1 - rho**2) * dW2
        
        # Generate paths using Euler-Maruyama scheme
        for i in range(n_steps):
            # Variance process
            variances[:, i + 1] = (
                variances[:, i]
                + kappa * (theta - variances[:, i]) * dt
                + sigma_v * np.sqrt(np.maximum(variances[:, i], 0)) * dW2[:, i]
            )
            # Ensure variance stays positive
            variances[:, i + 1] = np.maximum(variances[:, i + 1], 0)
            
            # Price process
            prices[:, i + 1] = prices[:, i] * np.exp(
                -0.5 * variances[:, i] * dt
                + np.sqrt(variances[:, i]) * dW1[:, i]
            )
        
        return prices, variances

    @staticmethod
    def correlated_paths(
        paths: list[NDArray[np.float64]],
        correlation_matrix: NDArray[np.float64],
    ) -> list[NDArray[np.float64]]:
        """
        Generate correlated paths using Cholesky decomposition.
        
        Args:
            paths: List of uncorrelated paths
            correlation_matrix: Correlation matrix between assets
            
        Returns:
            List of correlated paths
        """
        n_assets = len(paths)
        if correlation_matrix.shape != (n_assets, n_assets):
            raise ValueError("Correlation matrix dimensions must match number of assets")
            
        # Cholesky decomposition
        L = np.linalg.cholesky(correlation_matrix)
        
        # Transform uncorrelated paths to correlated
        correlated_paths = []
        for i in range(n_assets):
            correlated_path = np.zeros_like(paths[i])
            for j in range(n_assets):
                correlated_path += L[i, j] * paths[j]
            correlated_paths.append(correlated_path)
            
        return correlated_paths 
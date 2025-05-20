# Monte Carlo Simulation Platform

A modern web application for running financial Monte Carlo simulations with various stochastic processes.

## Features

- Geometric Brownian Motion (GBM) simulation
- Jump-Diffusion and Heston models (coming soon)
- Real-time market data via yfinance
- Interactive charts with Plotly.js
- Dark/light theme support
- Responsive Material-UI design

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd monte-carlo-simulator
```

2. Start the development environment:
```bash
make dev
```

This will start both the backend (FastAPI) and frontend (React) services:
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

## API Examples

### Run a GBM Simulation

```bash
curl -X POST http://localhost:8000/api/simulate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gbm",
    "tickers": ["AAPL"],
    "params": {
      "mu": 0.1,
      "sigma": 0.2
    },
    "n_paths": 1000,
    "horizon": 252,
    "seed": 42
  }'
```

### Get Market Data

```bash
curl http://localhost:8000/api/data/AAPL
```

## Development

- Backend: Python 3.12, FastAPI
- Frontend: React + TypeScript + Vite
- State Management: Zustand
- UI: Material-UI v6
- Charts: Plotly.js

### Common Commands

```bash
# Start development servers
make dev

# Run tests
make test

# Lint code
make lint

# Clean up
make clean
```

## Next Steps

- [ ] Implement Jump-Diffusion model
- [ ] Add Heston stochastic volatility model
- [ ] Implement data caching layer
- [ ] Add user authentication
- [ ] Add portfolio optimization features
- [ ] Implement stress testing scenarios 
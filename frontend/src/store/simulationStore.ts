import { create } from "zustand";

interface SimulationParams {
  mu: number;
  sigma: number;
  lambda_jump?: number;
  mu_jump?: number;
  sigma_jump?: number;
  v0?: number;
  kappa?: number;
  theta?: number;
  sigma_v?: number;
  rho?: number;
}

interface SimulationRequest {
  model: "gbm" | "jump_diffusion" | "heston";
  tickers: string[];
  params: SimulationParams;
  n_paths: number;
  horizon: number;
  seed?: number;
}

interface SimulationResult {
  paths: number[][];
  variances?: number[][];
  stats: {
    mean: number;
    std: number;
    var_95: number;
    var_99: number;
    cvar_95: number;
    cvar_99: number;
  };
}

interface SimulationState {
  request: SimulationRequest;
  result: SimulationResult | null;
  isLoading: boolean;
  error: string | null;
  setRequest: (request: SimulationRequest) => void;
  setResult: (result: SimulationResult | null) => void;
  setLoading: (isLoading: boolean) => void;
  setError: (error: string | null) => void;
}

export const useSimulationStore = create<SimulationState>((set) => ({
  request: {
    model: "gbm",
    tickers: ["AAPL"],
    params: {
      mu: 0.1,
      sigma: 0.2,
    },
    n_paths: 1000,
    horizon: 252,
  },
  result: null,
  isLoading: false,
  error: null,
  setRequest: (request) => set({ request }),
  setResult: (result) => set({ result }),
  setLoading: (isLoading) => set({ isLoading }),
  setError: (error) => set({ error }),
})); 
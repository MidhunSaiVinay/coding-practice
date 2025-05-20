import { useState } from "react";
import {
  Box,
  Button,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  Stack,
  Switch,
  TextField,
  Typography,
} from "@mui/material";

interface SimulationFormProps {
  onSubmit: (data: any) => void;
  isAdvanced: boolean;
  onToggleAdvanced: () => void;
}

interface FormData {
  model: string;
  tickers: string[];
  params: {
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
  };
  n_paths: number;
  horizon: number;
  seed: number | null;
}

export const SimulationForm = ({
  onSubmit,
  isAdvanced,
  onToggleAdvanced,
}: SimulationFormProps) => {
  const [formData, setFormData] = useState<FormData>({
    model: "gbm",
    tickers: ["AAPL"],
    params: {
      mu: 0.1,
      sigma: 0.2,
    },
    n_paths: 1000,
    horizon: 252,
    seed: null,
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  const handleModelChange = (model: string) => {
    const newParams = { ...formData.params };
    
    // Reset model-specific parameters
    if (model === "gbm") {
      newParams.mu = 0.1;
      newParams.sigma = 0.2;
    } else if (model === "jump_diffusion") {
      newParams.mu = 0.1;
      newParams.sigma = 0.2;
      newParams.lambda_jump = 0.1;
      newParams.mu_jump = -0.1;
      newParams.sigma_jump = 0.1;
    } else if (model === "heston") {
      newParams.v0 = 0.04;
      newParams.kappa = 2.0;
      newParams.theta = 0.04;
      newParams.sigma_v = 0.3;
      newParams.rho = -0.7;
    }
    
    setFormData({ ...formData, model, params: newParams });
  };

  return (
    <Box component="form" onSubmit={handleSubmit}>
      <Stack spacing={3}>
        <Box sx={{ display: "flex", alignItems: "center", gap: 2 }}>
          <Typography>Basic Mode</Typography>
          <Switch checked={isAdvanced} onChange={onToggleAdvanced} />
          <Typography>Advanced Mode</Typography>
        </Box>

        <FormControl fullWidth>
          <InputLabel>Model</InputLabel>
          <Select
            value={formData.model}
            label="Model"
            onChange={(e) => handleModelChange(e.target.value)}
          >
            <MenuItem value="gbm">Geometric Brownian Motion</MenuItem>
            {isAdvanced && (
              <>
                <MenuItem value="jump_diffusion">Jump-Diffusion</MenuItem>
                <MenuItem value="heston">Heston</MenuItem>
              </>
            )}
          </Select>
        </FormControl>

        <TextField
          fullWidth
          label="Tickers (comma-separated)"
          value={formData.tickers.join(",")}
          onChange={(e) =>
            setFormData({
              ...formData,
              tickers: e.target.value.split(",").map((t) => t.trim()),
            })
          }
        />

        <TextField
          fullWidth
          type="number"
          label="Number of Paths"
          value={formData.n_paths}
          onChange={(e) =>
            setFormData({
              ...formData,
              n_paths: parseInt(e.target.value) || 0,
            })
          }
          inputProps={{ min: 1, max: 100000 }}
        />

        <TextField
          fullWidth
          type="number"
          label="Horizon (days)"
          value={formData.horizon}
          onChange={(e) =>
            setFormData({
              ...formData,
              horizon: parseInt(e.target.value) || 0,
            })
          }
          inputProps={{ min: 1, max: 2520 }}
        />

        {isAdvanced && (
          <>
            {formData.model === "gbm" && (
              <>
                <TextField
                  fullWidth
                  type="number"
                  label="Drift (μ)"
                  value={formData.params.mu}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        mu: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Volatility (σ)"
                  value={formData.params.sigma}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        sigma: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />
              </>
            )}

            {formData.model === "jump_diffusion" && (
              <>
                <TextField
                  fullWidth
                  type="number"
                  label="Drift (μ)"
                  value={formData.params.mu}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        mu: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Volatility (σ)"
                  value={formData.params.sigma}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        sigma: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Jump Intensity (λ)"
                  value={formData.params.lambda_jump}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        lambda_jump: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Mean Jump Size (μ_j)"
                  value={formData.params.mu_jump}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        mu_jump: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Jump Size Volatility (σ_j)"
                  value={formData.params.sigma_jump}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        sigma_jump: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />
              </>
            )}

            {formData.model === "heston" && (
              <>
                <TextField
                  fullWidth
                  type="number"
                  label="Initial Variance (v₀)"
                  value={formData.params.v0}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        v0: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Mean Reversion Speed (κ)"
                  value={formData.params.kappa}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        kappa: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Long-run Variance (θ)"
                  value={formData.params.theta}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        theta: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Vol of Vol (σ_v)"
                  value={formData.params.sigma_v}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        sigma_v: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                />

                <TextField
                  fullWidth
                  type="number"
                  label="Correlation (ρ)"
                  value={formData.params.rho}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      params: {
                        ...formData.params,
                        rho: parseFloat(e.target.value) || 0,
                      },
                    })
                  }
                  inputProps={{ min: -1, max: 1, step: 0.1 }}
                />
              </>
            )}

            <TextField
              fullWidth
              type="number"
              label="Random Seed"
              value={formData.seed || ""}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  seed: e.target.value ? parseInt(e.target.value) : null,
                })
              }
            />
          </>
        )}

        <Button
          type="submit"
          variant="contained"
          size="large"
          fullWidth
        >
          Run Simulation
        </Button>
      </Stack>
    </Box>
  );
}; 
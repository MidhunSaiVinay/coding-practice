import { useEffect, useState } from "react";
import {
  Box,
  Container,
  Grid,
  Paper,
  Typography,
  useTheme,
} from "@mui/material";
import { SimulationForm } from "../components/SimulationForm";
import { StatsTable } from "../components/StatsTable";
import { useSimulationStore } from "../store/simulationStore";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { API_BASE_URL } from "../config";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const SimulationPage = () => {
  const theme = useTheme();
  const [isAdvanced, setIsAdvanced] = useState(false);
  const { request, result, isLoading, error, setRequest, setResult, setLoading, setError } =
    useSimulationStore();

  const handleSubmit = async (data: any) => {
    try {
      setLoading(true);
      setError(null);

      const response = await fetch(`${API_BASE_URL}/api/simulate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Simulation failed");
      }

      const result = await response.json();
      
      // Decode the compressed paths
      const pathsArray = new Float64Array(atob(result.paths).split('').map(c => c.charCodeAt(0)));
      const decodedPaths = Array.from(pathsArray);
      
      // Decode variances if they exist
      let decodedVariances = null;
      if (result.variances) {
        const variancesArray = new Float64Array(atob(result.variances).split('').map(c => c.charCodeAt(0)));
        decodedVariances = Array.from(variancesArray);
      }

      setResult({
        ...result,
        paths: [decodedPaths],
        variances: decodedVariances ? [decodedVariances] : undefined
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  const chartData = {
    labels: Array.from({ length: request.horizon + 1 }, (_, i) => i),
    datasets: [
      {
        label: "Price Paths",
        data: result?.paths[0] || [],
        borderColor: theme.palette.primary.main,
        backgroundColor: theme.palette.primary.main,
        tension: 0.1,
      },
      ...(result?.variances
        ? [
            {
              label: "Variance Path",
              data: result.variances[0],
              borderColor: theme.palette.secondary.main,
              backgroundColor: theme.palette.secondary.main,
              tension: 0.1,
            },
          ]
        : []),
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: "top" as const,
      },
      title: {
        display: true,
        text: `${request.model.toUpperCase()} Simulation Results`,
      },
    },
    scales: {
      y: {
        beginAtZero: false,
      },
    },
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Simulation Parameters
            </Typography>
            <SimulationForm
              onSubmit={handleSubmit}
              isAdvanced={isAdvanced}
              onToggleAdvanced={() => setIsAdvanced(!isAdvanced)}
            />
          </Paper>
        </Grid>

        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Results
            </Typography>
            {error && (
              <Typography color="error" gutterBottom>
                {error}
              </Typography>
            )}
            {isLoading ? (
              <Typography>Loading...</Typography>
            ) : result ? (
              <Box>
                <Box sx={{ mb: 3 }}>
                  <Line data={chartData} options={chartOptions} />
                </Box>
                <StatsTable stats={result.stats} />
              </Box>
            ) : (
              <Typography>Run a simulation to see results</Typography>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}; 
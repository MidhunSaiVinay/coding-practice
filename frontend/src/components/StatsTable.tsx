import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@mui/material";

interface Stats {
  mean: number;
  std: number;
  var_95: number;
  var_99: number;
  cvar_95: number;
  cvar_99: number;
}

interface StatsTableProps {
  stats: Stats;
}

export const StatsTable = ({ stats }: StatsTableProps) => {
  const formatNumber = (num: number) => {
    return new Intl.NumberFormat("en-US", {
      style: "percent",
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    }).format(num);
  };

  const rows = [
    { label: "Mean Return", value: stats.mean },
    { label: "Standard Deviation", value: stats.std },
    { label: "95% Value at Risk", value: stats.var_95 },
    { label: "99% Value at Risk", value: stats.var_99 },
    { label: "95% Conditional VaR", value: stats.cvar_95 },
    { label: "99% Conditional VaR", value: stats.cvar_99 },
  ];

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Metric</TableCell>
            <TableCell align="right">Value</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.label}>
              <TableCell component="th" scope="row">
                {row.label}
              </TableCell>
              <TableCell align="right">{formatNumber(row.value)}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}; 
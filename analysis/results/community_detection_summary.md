# Community detection summary
Generated: 2026-02-28 19:00 

## Algorithm comparison (Atlantic)

| Algorithm | N_communities | Modularity |
|-----------|---------------|------------|
| Louvain | 12 | 0.6217 |
| Infomap | 55 | 0.5611 |
| Fast Greedy | 11 | 0.5967 |
| Leading Eigen | 8 | 0.5804 |
| Walktrap | 35 | 0.5913 |

## Algorithm comparison (Pacific)

| Algorithm | N_communities | Modularity |
|-----------|---------------|------------|
| Louvain | 9 | 0.5979 |
| Infomap | 57 | 0.5553 |
| Fast Greedy | 5 | 0.5685 |
| Leading Eigen | 6 | 0.5754 |
| Walktrap | 49 | 0.5458 |

## Consensus clustering (iterative, nP = 30, tau = 0.5) — final partition for downstream

| Network | N_communities | N_iterations | Converged | Q_on_original |
|---------|---------------|--------------|-----------|---------------|
| Atlantic | 11 | 2 | TRUE | 0.6126 |
| Pacific  | 10 | 2 | TRUE | 0.5930 |

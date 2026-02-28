# Algorithm comparison (pre-consensus)
Generated: 2026-02-28 18:59 

## Atlantic

| Algorithm | N_communities | Modularity |
|-----------|---------------|------------|
| Louvain | 12 | 0.6217 |
| Infomap | 55 | 0.5611 |
| Fast Greedy | 11 | 0.5967 |
| Leading Eigen | 8 | 0.5804 |
| Walktrap | 35 | 0.5913 |

## Pacific

| Algorithm | N_communities | Modularity |
|-----------|---------------|------------|
| Louvain | 9 | 0.5979 |
| Infomap | 57 | 0.5553 |
| Fast Greedy | 5 | 0.5685 |
| Leading Eigen | 6 | 0.5754 |
| Walktrap | 49 | 0.5458 |

## Atlantic vs Pacific (side by side)

| Algorithm | N_communities_Atlantic | N_communities_Pacific | Modularity_Atlantic | Modularity_Pacific |
|-----------|------------------------|------------------------|---------------------|--------------------|
| Louvain | 12 | 9 | 0.621664682065581 | 0.597879266896968 |
| Infomap | 55 | 57 | 0.561060045222309 | 0.55533237625523 |
| Fast Greedy | 11 | 5 | 0.596666271366872 | 0.568486433785619 |
| Leading Eigen | 8 | 6 | 0.58039099539131 | 0.575441705916831 |
| Walktrap | 35 | 49 | 0.591275883303032 | 0.545815565212048 |

## NMI between algorithms (1 = identical, 0 = independent)

### Atlantic

| | Louvain | Infomap | Fast Greedy | Leading Eigen | Walktrap |
|---|--------|--------|-------------|---------------|----------|
| Louvain | 1.000 | 0.630 | 0.676 | 0.603 | 0.673 |
| Infomap | 0.630 | 1.000 | 0.534 | 0.543 | 0.608 |
| Fast Greedy | 0.676 | 0.534 | 1.000 | 0.582 | 0.647 |
| Leading Eigen | 0.603 | 0.543 | 0.582 | 1.000 | 0.589 |
| Walktrap | 0.673 | 0.608 | 0.647 | 0.589 | 1.000 |

### Pacific

| | Louvain | Infomap | Fast Greedy | Leading Eigen | Walktrap |
|---|--------|--------|-------------|---------------|----------|
| Louvain | 1.000 | 0.612 | 0.547 | 0.597 | 0.573 |
| Infomap | 0.612 | 1.000 | 0.521 | 0.517 | 0.619 |
| Fast Greedy | 0.547 | 0.521 | 1.000 | 0.557 | 0.577 |
| Leading Eigen | 0.597 | 0.517 | 0.557 | 1.000 | 0.528 |
| Walktrap | 0.573 | 0.619 | 0.577 | 0.528 | 1.000 |

## VI between algorithms (0 = identical, larger = more different)

### Atlantic

| | Louvain | Infomap | Fast Greedy | Leading Eigen | Walktrap |
|---|--------|--------|-------------|---------------|----------|
| Louvain | 0.000 | 1.906 | 1.160 | 1.542 | 1.260 |
| Infomap | 1.906 | 0.000 | 2.239 | 2.335 | 1.987 |
| Fast Greedy | 1.160 | 2.239 | 0.000 | 1.481 | 1.238 |
| Leading Eigen | 1.542 | 2.335 | 1.481 | 0.000 | 1.564 |
| Walktrap | 1.260 | 1.987 | 1.238 | 1.564 | 0.000 |

### Pacific

| | Louvain | Infomap | Fast Greedy | Leading Eigen | Walktrap |
|---|--------|--------|-------------|---------------|----------|
| Louvain | 0.000 | 2.034 | 1.623 | 1.552 | 1.813 |
| Infomap | 2.034 | 0.000 | 2.230 | 2.381 | 2.028 |
| Fast Greedy | 1.623 | 2.230 | 0.000 | 1.451 | 1.550 |
| Leading Eigen | 1.552 | 2.381 | 1.451 | 0.000 | 1.856 |
| Walktrap | 1.813 | 2.028 | 1.550 | 1.856 | 0.000 |

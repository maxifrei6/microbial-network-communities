# Analysis results

Outputs written when you run the pipeline from the `analysis/` directory:

- **`network_analysis_summary.md`** — From `network_analysis.Rmd`. Basic network stats and connectivity metrics (Atlantic and Pacific). Optional step.
- **`atlantic_adjacency_matrix.csv`**, **`pacific_adjacency_matrix.csv`** — From `network_analysis.Rmd`. Full adjacency matrices (if produced).
- **`community_detection_summary.md`** — From `community_detection.Rmd`. Algorithm comparison and consensus Louvain summary.
- **`algorithm_comparison.md`** — From `community_detection.Rmd`. NMI/VI comparison of the five algorithm partitions.
- **`consensus_log.txt`** — From `community_detection.Rmd`. Log of the iterative consensus clustering runs.
- **`atlantic_consensus_communities.csv`**, **`pacific_consensus_communities.csv`** — **Final consensus partition** (columns: `node`, `community`). Input for `microbial_community_analysis.Rmd`.
- **`atlantic_community_memberships.csv`**, **`pacific_community_memberships.csv`** — From `community_detection.Rmd`. All algorithms plus consensus (for reference or NMI comparison).
- **`microbial_community_summary.md`** — From `microbial_community_analysis.Rmd`. Short summary of the ecological interpretation step.
- **`network_panels_atlantic/`**, **`network_panels_pacific/`** — From `microbial_community_analysis.Rmd`. Six individual panel PDFs per basin (e.g. `network_atlantic_panel_a_modules.pdf` … `network_atlantic_panel_f_class.pdf`). Also copied to `thesis/fig/`.

**Workflow:** `network_analysis.Rmd` (optional) → `community_detection.Rmd` → `microbial_community_analysis.Rmd`. Consensus communities from step 2 are the input for step 3.

**To refresh:** Knit from the `analysis/` directory. Summary `.md` files and CSVs are overwritten each time.

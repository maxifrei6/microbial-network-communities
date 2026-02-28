# Network Communities Project

Seminar project on community detection in microbial (bacteria, archaea, eukaryotes) networks using the GRUMP database.

## Data not in this repository

**The data are not included in the repo** (see `.gitignore`). The folder `analysis/data/` is excluded from version control. To run the analysis pipeline you need to add the required files under `analysis/data/export/estimated_network/` (see **Prerequisites** below). These typically come from your own GRUMP-based pipeline or data export (e.g. from `analysis/scripts/00_prep_grump_students.Rmd` and `01_split_data.Rmd`, or from a separate data preparation step). The repository contains code, the thesis source, and (if generated) results and figures so that the thesis can be compiled after running the pipeline once.

## Project Structure

After restructure, main locations:

```
network-communities/
├── thesis/                 # LaTeX thesis (LMU template)
│   ├── thesis.tex
│   ├── bibliography.bib
│   └── chapters/           # introduction, methods, results, conclusion, appendix
│
├── literature/notes/       # Paper source and notes
│   ├── seminar-paper.Rmd    # R Markdown version of the seminar paper
│   ├── references.bib      # Bibliography (for Rmd; synced with thesis/bibliography.bib)
│   ├── seminar-paper-outline.md
│   ├── DATA_STRUCTURE.md   # Data and export layout
│   └── ...
│
├── analysis/               # Data & analysis pipeline
│   ├── data/
│   │   └── export/
│   │       ├── estimated_network/   # Edgelists and node features
│   │       ├── pacific/
│   │       └── erc/
│   ├── scripts/            # 00_prep_grump_students.Rmd, 01_split_data.Rmd
│   └── results/
│
├── presentation/           # Presentation materials
│   ├── paper-presentation.qmd
│   ├── scripts/
│   └── notes/
│
├── scratch/help-files/    # Literature notes, context prompts
│
└── LMU_SLDS_Thesis_Template/   # Original template (unchanged)
```

## How to run the analysis pipeline

All analysis Rmd files are intended to be run from the **`analysis/`** directory (as the working directory). Paths inside the Rmds assume this.

### Prerequisites

- **Data** (not in repo; place under `analysis/data/export/estimated_network/`):
  - `atlantic_edgelist.csv`, `pacific_edgelist.csv`
  - `node_features_atlantic.csv`, `node_features_pacific.csv`
  - `otu_tax_table_all.csv` (for taxonomic interpretation in the microbial community analysis)
- R packages: `igraph`, `tidyverse`, `knitr`, `kableExtra`, `scales` (and any others required by the Rmds).

### Run order

1. **`community_detection.Rmd`**  
   Loads the edgelists, runs five algorithms (Louvain, Infomap, Fast Greedy, Leading Eigenvector, Walktrap), compares partitions (NMI/VI), runs iterative consensus clustering (Louvain, nP=30, τ=0.5), and exports:
   - `analysis/results/atlantic_consensus_communities.csv`, `pacific_consensus_communities.csv`
   - `analysis/results/community_detection_summary.md`
   - `analysis/results/consensus_log.txt`
   - `thesis/fig/algorithm_comparison_bars.pdf`, `thesis/fig/nmi_heatmap.pdf`

2. **`microbial_community_analysis.Rmd`**  
   Requires the consensus CSVs and node/taxonomy data. Summarises taxonomy and environment per consensus community (bar charts, boxplots), compares basins, and builds the 6-panel network figures. Exports:
   - `analysis/results/microbial_community_summary.md`
   - **Combined:** `thesis/fig/network_atlantic_panels.pdf`, `thesis/fig/network_pacific_panels.pdf`
   - **Individual panels** (one PDF per panel, better spacing; combine in LaTeX if you use only some):  
     Written to **both** `thesis/fig/` and `analysis/results/network_panels_atlantic/` (resp. `network_panels_pacific/`).  
     Names: `network_atlantic_panel_a_modules.pdf` … `network_atlantic_panel_f_class.pdf`, and same for Pacific.  
     (Knit from `analysis/` so paths resolve correctly.)

Optional (for basic network stats only):

- **`network_analysis.Rmd`**  
  Loads edgelists, computes basic statistics and connectivity metrics, writes `analysis/results/network_analysis_summary.md`. No dependency on community detection; can be run before or in parallel with the pipeline above.

### Reproducing thesis figures and tables

- Run **1** then **2** from `analysis/`. Then compile the thesis from `thesis/` (e.g. `cd thesis && pdflatex thesis`). The thesis expects the PDFs in `thesis/fig/` (see “Figures” below). Numbers in the results chapter are taken from the `*_summary.md` files in `analysis/results/` (and from the consensus CSVs).

### One-liner (from project root)

```bash
cd analysis && Rscript -e "rmarkdown::render('community_detection.Rmd'); rmarkdown::render('microbial_community_analysis.Rmd')"
```

(Or open and knit the Rmds in order in RStudio.)

---

## Quick Start

**Seminar paper (Rmd):** `literature/notes/seminar-paper.Rmd`  
**Thesis (LaTeX):** `thesis/thesis.tex`

**Data preparation (if needed):** `analysis/scripts/` (00_prep_grump_students.Rmd → 01_split_data.Rmd)

**Exported networks:**
- `analysis/data/export/estimated_network/atlantic_edgelist.csv`
- `analysis/data/export/estimated_network/pacific_edgelist.csv`

**Data and export layout:** `literature/notes/DATA_STRUCTURE.md`

## Figures (paper vs presentation)

**Paper** (thesis + seminar Rmd) and **presentation** use separate figure folders.

- **Thesis:** `thesis/fig/`  
  - **Generated by the pipeline** (run from `analysis/` as above): `algorithm_comparison_bars.pdf`, `nmi_heatmap.pdf`, `network_atlantic_panels.pdf`, `network_pacific_panels.pdf`.  
  - **Static / methods figures:** `thesis/fig/` also holds (or references) `fig-4.png`, `fig-8.png`, `fig-9.png`, `fig-10.png`, `structure_vs_metadata.png`, etc. If those are kept in `literature/notes/fig/`, the thesis uses paths like `../../literature/notes/fig/` where needed. Compile the thesis from `thesis/` (e.g. `cd thesis && pdflatex thesis`).

- **Seminar paper (Rmd):** `literature/notes/fig/` — paths use `fig/` (same directory as the Rmd).

- **Presentation:** `presentation/results/` (and `presentation/figures/` for logo).  
  - `paper-presentation.qmd` references `results/` for slides. Scripts in `presentation/scripts/` can generate figures there.


## Project Goal

Compare Atlantic and Pacific microbial network communities, estimate modularity, and link detected communities to biological and environmental features (temperature, salinity, depth, taxonomy).

**Paper requirement:** 20–30 pages (9 credits)
- Introduction: Fortunato & Hric theory + GRUMP motivation
- Methods: Community detection theory + data pipeline
- Results: Network analysis + community structure
- Conclusion: Findings + ecological implications

# Presentation Script (Bullet Points)
**Duration: 18.5 minutes**

---

## [SLIDE: Title] (30s)
- Good morning/afternoon
- Today: "Community Detection in Networks: A User Guide" by Fortunato & Hric
- Most popular & problematic topic in network science

---

## [SLIDE: Agenda Part 1] (30s)
- Structure:
  - Background on challenges
  - Two competing views: classic vs modern
  - Validation methods & detection limits

---

## [SLIDE: Agenda Part 2] (30s)
- Second half:
  - Detection methods: spectral, optimization, consensus
  - Alternative approaches
  - Practical recommendations

---

## [SLIDE: 1 Background Information - Challenges] (1 min)
- Core problem: identifying communities
- Three fundamental challenges:
  1. No universal definition
  2. Many competing methods
  3. No standard validation protocol
- Generated confusion & misconceptions

---

## [SLIDE: 1 Background Information - Paper & Goal] (30s)
- Fortunato & Hric, Physics Reports 2016
- Acts as "User Guide"
- Goals:
  - Critical analysis
  - Expose limits of popular methods
  - Provide robust protocols

---

## [SLIDE: 2 What is a Community?] (transition)
- Fundamental question
- Two different views
- Understanding distinction is crucial

---

## [SLIDE: 2.1 Classic View] (1.5 min)
- Dense subgraphs, clearly separated
- Based on edge counting
- Internal edges > external edges
- Major flaw: treats "rest of network" as single object
- Breaks down in large, heterogeneous networks

---

## [SLIDE: 2.2 Modern View - SBM] (2-2.5 min)
- Shift from counting to probabilities
- Key insight: same community = higher edge probability
- p_in (within) vs p_out (between)
- Stochastic Block Model (SBM):
  - Probability matrix shown
  - Assortative: p_in > p_out
  - Null model: p_in = p_out (Erdős-Rényi)
- SBM is generative: assign nodes → connect probabilistically
- Creates realistic structures
- If not distinguishable from random baseline → not a community

---

## [SLIDE: 2.2 Modern View - Adjacency Matrix] (1 min)
- Visual demonstration of SBM
- Adjacency matrix sorted by communities
- Dense blocks on diagonal (communities)
- Sparse off-diagonal (between communities)
- Structure immediately visible
- Shows how SBM generates realistic networks

---

## [SLIDE: 3.1 Benchmarks - Girvan-Newman] (1 min)
- Two types of benchmarks:
  - Computer-generated (from models)
  - Actual networks (known via metadata)
- Girvan-Newman too simple
- All nodes equal degree, all communities equal size
- Unrealistic—real networks are heterogeneous

---

## [SLIDE: 3.1 Benchmarks - LFR] (1 min)
- LFR is the standard
- Power-law distributions for:
  - Degree
  - Community size
- Realistic proxy for real-world networks
- Heterogeneity crucial—real networks are scale-free

---

## [SLIDE: 3.2 Structure vs Metadata] (1 min)
- Important point: structural communities ≠ metadata
- Visualization shows misalignment
- Example: same dorm ≠ structural community
- Don't trust node labels as ground truth
- Metadata enriches interpretation, not strict validation
- Solution: structure alongside annotations, not replacement

---

## [SLIDE: 4 Detection Methods] (transition)
- Many methods require q (number of clusters) as input
- Important consideration when choosing

---

## [SLIDE: 4.1 Spectral Methods - Text] (1-1.5 min)
- Use eigenvalues/eigenvectors of graph matrices (A or L)
- Embed nodes → cluster in eigenspace
- Problem in sparse networks:
  - Bulk eigenvalues (noise) merge with signal
  - Confuses algorithms
- Solution: Non-Backtracking Matrix (B)
- Count real eigenvalues outside spectral circle = q
- Mathematical rigor, works when others fail

---

## [SLIDE: 4.1 Spectral Methods - Visualization] (0.5 min)
- Shows eigenvalue separation
- Gray dots: bulk noise (spectral circle)
- Red dots: signal (communities)
- Clean separation enables detection

---

## [SLIDE: 4.2 Optimization - Modularity] (2 min)
- Most popular: modularity maximization
- Q compares actual vs expected edges
- Formula: Q = 1/(2m) Σ(A_ij - P_ij)δ(C_i, C_j)
- Breakdown:
  - A_ij: actual adjacency matrix
  - P_ij: expected (config model: k_i*k_j/2m)
  - δ: 1 if same community, 0 otherwise
  - 2m: normalization (total edges)
- Intuition:
  - Sum over all node pairs
  - Same community: add (actual - expected)
  - Positive = more edges than expected (good)
  - Negative = fewer edges (bad)
  - Range: -1 to 1
- Louvain algorithm: fast, greedy optimization
- Widely implemented but has serious flaws

---

## [SLIDE: 4.2 Optimization - Null Model] (1 min)
- Must always test against null model
- Random graphs can have high Q!
- High modularity ≠ proof of real communities
- This is the modularity trap

---

## [SLIDE: 4.2 Optimization - Problems] (30s)
- Three main problems:
  1. Resolution limit: forces merging in large networks
  2. Rugged landscape: many local maxima
  3. Modularity trap: random graphs have high Q

---

## [SLIDE: 4.3 Consensus Clustering] (1.5 min)
- Solution to instability
- Many algorithms (Louvain) are stochastic
- Different results each run
- Running once is dangerous
- Protocol:
  1. Run algorithm multiple times
  2. Build consensus matrix D_ij
  3. Records how often i and j appear together
  4. Re-cluster consensus matrix
- Result: filters noise, stable communities
- Fuzzy → crisp
- Essential for serious analysis

---

## [SLIDE: 4.4 Alternatives Overview] (45s)
- Brief overview of other methods:
- Infomap: random walks trapped in communities
  - Best for directed, flow networks
- SBM Inference: Maximum Likelihood
  - Most rigorous, prevents overfitting
- OSLOM: statistical significance testing
  - Prevents false positives
- Edge Clustering: cluster edges not vertices
  - Useful for overlapping communities

---

## [SLIDE: 5 Outlook] (1 min)
- No silver bullet
- Method depends on network features
- Recommendations:
  - Rigor: SBM Inference or Spectral (non-backtracking)
  - Stability: always use Consensus Clustering
  - Validity: test against null models
  - Avoid trap: high Q ≠ real communities
- Key takeaway: requires careful methodology
  - Appropriate null models
  - Significance testing
  - Robust algorithms
- Modern probabilistic view provides foundation
- Must apply correctly
- Thank you, happy to take questions

---

## [SLIDE: Appendix - Detectability] (BACKUP - Q&A only)
- When are communities detectable?
- In sparse networks: detection can be mathematically impossible
- Signal too weak
- Threshold formula shown
- Below threshold: no algorithm can reliably detect
- Signal too weak vs noise
- Backup for questions about detectability limits

---

## TIMING SUMMARY:
- Introduction & Agenda: 1.5 min
- Background: 1.5 min
- What is Community: 5 min
- Validation: 3 min
- Detection Methods: 7.5 min
- Outlook: 1 min
- **Total: 18.5 minutes**


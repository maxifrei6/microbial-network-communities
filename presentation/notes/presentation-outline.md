# Presentation Script: Community Detection in Networks
**Duration: 15-20 minutes**

---

## [SLIDE: Title] (30 seconds)

**Good morning/afternoon. Today I'll be presenting on "Community Detection in Networks: A User Guide" by Fortunato and Hric. This paper addresses one of the most popular—and problematic—topics in network science.**

---

## [SLIDE: Agenda Part 1] (30 seconds)

**I'll structure my presentation as follows: First, I'll provide background on why community detection is challenging. Then I'll explain two competing views of what a community is—the classic edge-counting approach versus the modern probabilistic approach. Finally, I'll discuss validation methods and the fundamental limits of detection.**

---

## [SLIDE: Agenda Part 2] (30 seconds)

**In the second half, I'll dive into detection methods, focusing on spectral methods, optimization approaches, and consensus clustering. I'll also briefly overview alternative methods. I'll conclude with practical recommendations.**

---

## [SLIDE: 1 Background Information - Key Challenges] (1 minute)

**Let me start with the core problem. Identifying communities is arguably the most popular and problematic topic in network science.**

**The fundamental challenges are threefold: First, there is no universal definition of what a community is. Second, there are many competing methods, each with different assumptions. Third, there is no standard protocol for validation. This has generated significant confusion and misconceptions in the field.**

---

## [SLIDE: 1 Background Information - Paper & Authors + Goal] (30 seconds)

**This paper by Fortunato and Hric was published in Physics Reports in 2016. It acts as a "User Guide" to address these issues. The paper offers critical analysis, exposes the limits of popular methods, and provides robust protocols for detection.**

---

## [SLIDE: 2 What is a Community?] (transition slide)

**So, what is a community? This is where the confusion begins. There are two fundamentally different views, and understanding this distinction is crucial.**

---

## [SLIDE: 2.1 Classic View] (1.5 minutes)

**The classic view, which dominated early work, defines communities as dense subgraphs that are clearly separated from the rest of the network. Most methods based on this view rely on edge counting.**

**As you can see in this figure, communities are characterized by having more internal edges than external edges. The key idea is simple: count edges inside versus edges outside. If you have more internal edges, it's a community.**

**However, this approach has serious flaws: it treats the "rest of the network" as a single object, which breaks down in large, heterogeneous networks.**

---

## [SLIDE: 2.2 Modern View - SBM] (2-2.5 minutes) ⚠️ NEEDS MORE DEPTH

**The modern view shifts from counting edges to thinking about probabilities. The key insight: vertices of the same community have a higher probability—denoted $p_{in}$—to form edges with their partners than with other vertices—denoted $p_{out}$.**

**This is formalized through the Stochastic Block Model, or SBM. For each pair of nodes $i$ and $j$, the edge probability is:**

**$\Pr(A_{ij} = 1) = p_{z_i z_j}$**

**where $z_i$ is the community assignment of node $i$. Here's the probability matrix for a two-community case. We have $p_{in}$ on the diagonal—the probability of edges within communities—and $p_{out}$ off the diagonal—the probability of edges between communities.**

**When $p_{in} > p_{out}$, we have assortative mixing, which creates standard communities. The SBM is generative: we assign nodes to communities, then connect them probabilistically according to this matrix. This creates realistic network structures.**

**Crucially, the null hypothesis is Erdős-Rényi, where $p_{in} = p_{out}$. If a group is not statistically distinguishable from this random baseline, it is not a community.**

---

## [SLIDE: 2.2 Modern View - Adjacency Matrix] (1 minute)

**Here's what the SBM structure looks like when visualized. This is an adjacency matrix sorted by communities. You can see clear block structure—dense blocks on the diagonal where communities are, and sparse regions off the diagonal.**

**This visualization makes the community structure immediately obvious to the human eye, and demonstrates how the SBM generates realistic network structures.**

---

## [SLIDE: 3.1 Benchmarks - Girvan-Newman] (1 minute)

**Benchmarks can be computer-generated, according to some model, or actual networks, whose group structure is supposed to be known via non-topological features (metadata).**

**The Girvan-Newman benchmark is too simple. As you can see in this visualization, all nodes have equal degree and all communities have equal size. This is unrealistic—real networks are heterogeneous.**

---

## [SLIDE: 3.1 Benchmarks - LFR] (1 minute)

**The LFR benchmark is the standard. It incorporates power-law distributions for both degree and community size, making it a realistic proxy for real-world networks. This heterogeneity is crucial because real networks are scale-free.**

---

## [SLIDE: 3.2 Structure vs Metadata] (1 minute)

**Before moving to detection methods, I need to highlight an important point: structural communities often do not align with metadata. This visualization shows the misalignment—nodes with the same metadata label (like dormitory assignments) may not form structural communities in the network topology.**

**Do not trust node labels as ground truth for communities. Students in the same dorm may not interact more than students in different dorms. Metadata should be used to interpret and enrich results, not strictly to validate them. The solution is using structure alongside annotations, not replacing structure with metadata.**

---

## [SLIDE: 4 Detection Methods] (transition slide)

**Now let's turn to detection methods. Many methods require the number of clusters $q$ as input, which is an important consideration when choosing methods.**

---

## [SLIDE: 4.1 Spectral Methods] (1.5-2 minutes)

**Spectral methods use the eigenvalues and eigenvectors of graph matrices—typically the adjacency matrix or Laplacian—to map nodes into space and cluster them.**

**However, there's a problem: on sparse networks, the "bulk" eigenvalues—which are just noise—merge with the informative eigenvalues that contain the community signal. This confuses the algorithm.**

**The fix is crucial: use the Non-Backtracking Matrix, denoted $B$. Its eigenvalues cleanly separate the signal from the bulk noise, even in sparse graphs. The number of real eigenvalues outside the "spectral circle" corresponds to the optimal number of clusters $q$.**

**This provides mathematical rigor and works even when other methods fail.**

---

## [SLIDE: 4.2 Optimization - Modularity] (2 minutes) ⚠️ AS REQUESTED

**The most popular approach is optimization, specifically modularity maximization. Modularity, denoted $Q$, compares actual edges to expected edges in a null model. The formula is:**

**$Q = \frac{1}{2m} \sum_{ij} \left(A_{ij} - P_{ij}\right) \delta(C_i, C_j)$**

**where $A_{ij}$ is the actual adjacency matrix, $P_{ij}$ is the expected number of edges in the null model (typically the configuration model: $P_{ij} = \frac{k_i k_j}{2m}$), $m$ is the total number of edges, and $\delta(C_i, C_j)$ equals 1 if nodes $i$ and $j$ are in the same community, 0 otherwise.**

**The intuition: We sum over all pairs of nodes. If they're in the same community, we add the difference between actual and expected edges. Positive values mean more edges than expected—good for communities. Negative values mean fewer edges—bad for communities. We normalize by $2m$ to get a value between -1 and 1.**

**The Louvain algorithm maximizes $Q$ efficiently through greedy optimization. It's fast and widely implemented, but modularity has serious flaws that we need to understand.**

---

## [SLIDE: 4.2 Optimization - Null Model] (1 minute)

**This visualization shows why you must always test against a null model. Random graphs can achieve high modularity scores! High modularity does not prove real communities exist—this is the modularity trap.**

---

## [SLIDE: 4.2 Optimization - Problems] (30 seconds)

**Modularity has three main problems: First, the resolution limit—it forces small communities to merge in large networks. Second, the rugged landscape—many local maxima make optimization difficult. Third, the modularity trap—random graphs can have high $Q$.**

---

## [SLIDE: 4.3 Consensus Clustering] (1.5 minutes)

**The solution to instability is consensus clustering. Since many algorithms—like Louvain—are stochastic and give different results each run, running them once is dangerous.**

**The protocol is: run the algorithm multiple times. Build a consensus matrix $D_{ij}$ that records how often nodes $i$ and $j$ appear together. Then re-cluster this consensus matrix.**

**The result filters out noise and creates stable, robust communities. Fuzzy partitions become crisp. This is essential for any serious analysis.**

---

## [SLIDE: 4.4 Alternatives Overview] (45 seconds)

**Let me briefly overview other approaches. Infomap uses random walks that get "trapped" in communities—best for directed, flow-based networks. SBM inference uses Maximum Likelihood Estimation—the most rigorous approach that prevents overfitting. OSLOM tests statistical significance to prevent false positives. Edge clustering works on edges instead of vertices, which is useful for overlapping communities.**

---

## [SLIDE: 5 Outlook] (1 minute)

**To conclude, there is no silver bullet. Method choice depends on the specific network features.**

**My recommendations: For rigor, use SBM Inference or Spectral methods with the non-backtracking matrix. For stability, always use Consensus Clustering—run algorithms multiple times and build consensus. For validity, check significance against null models. And avoid the trap: remember that high modularity does not equal real communities.**

**The key takeaway is that community detection requires careful methodology. You need appropriate null models, significance testing, and robust algorithms. The modern probabilistic view provides the theoretical foundation, but you must apply it correctly.**

**Thank you. I'm happy to take questions.**

---

## [SLIDE: Appendix - Detectability] (BACKUP SLIDE - if time permits or for Q&A)

**Under which conditions are communities detectable? In sparse networks, detection can be mathematically impossible if the signal is too weak.**

**The threshold is: $\langle k_{in}\rangle - \frac{\langle k_{out}\rangle}{q-1} \le \sqrt{\langle k_{in}\rangle + \langle k_{out}\rangle}$. Below this threshold, no algorithm can reliably detect communities—the signal is too weak relative to the noise.**

**This is a backup slide that can be used during Q&A if questions about detectability limits arise.**

---

## TIMING BREAKDOWN:

- **Introduction & Agenda**: 1.5 minutes
  - Title: 30 seconds
  - Agenda Part 1: 30 seconds
  - Agenda Part 2: 30 seconds

- **Background Information**: 1.5 minutes
  - Key Challenges: 1 minute
  - Paper & Authors + Goal: 30 seconds

- **What is a Community?**: 5 minutes
  - Classic View: 1.5 minutes
  - Modern View - SBM: 2-2.5 minutes ⚠️ (with edge probability formula and generative process)
  - Modern View - Adjacency Matrix: 1 minute

- **Validation**: 3 minutes (Detectability moved to Appendix)
  - Benchmarks - Girvan-Newman: 1 minute (with fig-9)
  - Benchmarks - LFR: 1 minute (with fig-10, two-column layout)
  - Structure vs Metadata: 1 minute

- **Detection Methods**: 7.5 minutes
  - Spectral Methods: 1.5-2 minutes
  - Optimization - Modularity: 2 minutes (formula explained in detail with bullet points)
  - Optimization - Null Model: 1 minute (with fig-24)
  - Optimization - Problems: 30 seconds
  - Consensus Clustering: 1.5 minutes (two-column layout with fig-22)
  - Alternatives Overview: 45 seconds (compact table format)

- **Outlook**: 1 minute

- **Total: ~18.5 minutes**

**⚠️ TIMING NOTES:**
- Current total is **18.5 minutes**, which fits perfectly for a 15-20 minute presentation
- Detectability moved to **Appendix** (optional slide if time permits or for Q&A)
- If you need to stay under 18 minutes exactly, consider:
  - Reducing SBM to 2 minutes (instead of 2.5)
  - This would bring total to ~18 minutes

**Note**: Adjust timing based on audience questions and your speaking pace. The script is designed to be flexible—you can shorten the alternatives overview or expand on spectral methods if your supervisor asks questions.

---

## 📋 CONTENT DEPTH RECOMMENDATIONS

### ✅ Sections that are appropriately deep:
- **Classic View** (1.5 min) - Good balance
- **Spectral Methods** (1.5-2 min) - Appropriate for the level of detail
- **Consensus Clustering** (1.5 min) - Well explained with visualization
- **Outlook** (1 min) - Concise conclusion is appropriate

### ⚠️ Sections that need more depth (already addressed above):
1. **SBM** - Added edge probability formula and generative process explanation
2. **Modularity** - Expanded formula explanation and intuition
3. **Structure vs Metadata** - Added more context about misalignment

### 🔧 Sections that could be trimmed if needed:
- **Alternatives Overview** - Can reduce to 30 seconds if time is tight
- **Background** - Already concise, but could trim 15 seconds if necessary

### ⏱️ If you need to cut to 18 minutes:
- Reduce SBM to 2 minutes (from 2.5)
- Reduce Structure vs Metadata to 45 seconds (from 1 min)
- Reduce Alternatives to 30 seconds (from 45 sec)
- **Total: ~18 minutes**

### ⏱️ Current Structure (18.5 minutes):
- Timing is now optimized for a 15-20 minute presentation
- Better balance between depth and time constraints
- Detectability in appendix keeps focus on core content

---

## 📝 RECENT CHANGES TO PRESENTATION

### Structure Changes:
1. **Detectability removed from main flow** - moved to Appendix
   - Was taking 1 minute in Validation section
   - Now available as backup slide for Q&A
   - Agenda updated: 3.2 Detectability → removed, 3.3 Structure vs Metadata → 3.2

2. **Girvan-Newman benchmark enhanced**
   - Added visualization (fig-9)
   - Converted to bullet points for clarity
   - Increased time to 1 minute (from 45 seconds)

3. **Consensus Clustering improved**
   - Changed to two-column layout
   - Figure on left, explanation on right
   - Better visual balance

4. **Alternatives table compacted**
   - Shortened column headers and text
   - "Best For" instead of "Use Case"
   - Shortened method names (e.g., "Infomap" instead of "Dynamics (Infomap)")
   - Should now fit on slide without cutoff

### Timing Impact:
- **Before**: ~19.5 minutes (too long, rushed)
- **After**: ~18.5 minutes (optimal, allows for flexibility)
- Validation section: 3.5 min → 3 min (but better paced)
- Detection Methods: 8 min → 7.5 min (cleaner)
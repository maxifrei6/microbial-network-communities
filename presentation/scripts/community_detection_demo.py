import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches
from networkx.algorithms import community

SEED = 42
np.random.seed(SEED)

def create_erdos_renyi_graph(n=100, p=0.05, seed=SEED):
    return nx.erdos_renyi_graph(n, p, seed=seed)

def create_stochastic_block_model(n=100, p_in=0.3, p_out=0.05, seed=SEED):
    sizes = [n // 2, n - n // 2]
    probs = [[p_in, p_out], [p_out, p_in]]
    G = nx.stochastic_block_model(sizes, probs, seed=seed)
    group_labels = {}
    for node in G.nodes():
        group_labels[node] = G.nodes[node]['block']
    return G, group_labels

def visualize_null_model(G):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    
    pos = nx.spring_layout(G, seed=SEED, k=2.5, iterations=100, scale=10)
    
    nx.draw_networkx_nodes(G, pos, node_color='#3498db', 
                          node_size=400, alpha=0.9, ax=ax)
    nx.draw_networkx_edges(G, pos, alpha=0.15, width=1.5, ax=ax)
    
    ax.set_title(f'Null Model: Erdős-Rényi Random Graph\nN={G.number_of_nodes()}, E={G.number_of_edges()}\nNo planted structure', 
                 fontsize=18, fontweight='bold', pad=20)
    ax.axis('off')
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    
    plt.tight_layout()
    plt.savefig('../figures/1_null_model.png', dpi=200, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: ../figures/1_null_model.png")

def visualize_sbm(G, group_labels, p_in, p_out):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    
    pos = nx.spring_layout(G, seed=SEED, k=1.5, iterations=100, scale=10)
    
    colors = ['#e74c3c' if group_labels[node] == 0 else '#3498db' for node in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, node_color=colors, 
                          node_size=400, alpha=0.9, ax=ax)
    nx.draw_networkx_edges(G, pos, alpha=0.12, width=1.2, ax=ax)
    
    red_patch = mpatches.Patch(color='#e74c3c', label='Community A')
    blue_patch = mpatches.Patch(color='#3498db', label='Community B')
    ax.legend(handles=[red_patch, blue_patch], loc='upper right', fontsize=14, framealpha=0.9)
    
    ax.set_title(f'Stochastic Block Model (SBM)\nN={G.number_of_nodes()}, E={G.number_of_edges()}\n' +
                 f'p_in={p_in}, p_out={p_out}, Ratio={p_in/p_out:.1f}', 
                 fontsize=18, fontweight='bold', pad=20)
    ax.axis('off')
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    
    plt.tight_layout()
    plt.savefig('../figures/2_sbm.png', dpi=200, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: ../figures/2_sbm.png")

def visualize_detectability_spectrum(n=100, p_in=0.3, seed=SEED):
    scenarios = [
        {'p_out': 0.05, 'label': 'Strong Signal (Easy)', 'ratio': p_in/0.05},
        {'p_out': 0.20, 'label': 'Weak Signal (Hard)', 'ratio': p_in/0.20},
        {'p_out': 0.30, 'label': 'No Signal (Impossible)', 'ratio': 1.0}
    ]
    
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))
    fig.suptitle('Detectability Threshold: Adjacency Matrices', fontsize=20, fontweight='bold', y=0.98)
    
    for idx, scenario in enumerate(scenarios):
        p_out = scenario['p_out']
        G, group_labels = create_stochastic_block_model(n, p_in, p_out, seed=seed+idx)
        
        sorted_nodes = sorted(G.nodes(), key=lambda x: group_labels[x])
        adj_matrix = nx.to_numpy_array(G, nodelist=sorted_nodes)
        
        ax = axes[idx]
        im = ax.imshow(adj_matrix, cmap='Blues', interpolation='nearest', aspect='auto')
        
        boundary = n // 2
        ax.axhline(y=boundary-0.5, color='red', linewidth=3, linestyle='--', alpha=0.8)
        ax.axvline(x=boundary-0.5, color='red', linewidth=3, linestyle='--', alpha=0.8)
        
        ax.set_title(f"{scenario['label']}\np_in={p_in}, p_out={p_out}\nRatio: {scenario['ratio']:.2f}",
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Node', fontsize=12)
        ax.set_ylabel('Node', fontsize=12)
        
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    
    plt.tight_layout()
    plt.savefig('../figures/3_detectability.png', dpi=200, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: ../figures/3_detectability.png")

def calculate_modularity(G, communities):
    return community.modularity(G, communities)

def detect_communities_greedy(G):
    return community.greedy_modularity_communities(G)

def demonstrate_modularity_trap(n=100, p=0.05, p_in=0.3, p_out=0.05, seed=SEED):
    print("\n" + "="*80)
    print("MODULARITY TRAP ANALYSIS")
    print("="*80)
    
    # Random graph
    print("\n[1] NULL MODEL (Random Graph):")
    G_random = create_erdos_renyi_graph(n, p, seed=seed)
    communities_random = detect_communities_greedy(G_random)
    Q_random = calculate_modularity(G_random, communities_random)
    print(f"    Nodes: {G_random.number_of_nodes()}, Edges: {G_random.number_of_edges()}")
    print(f"    Detected communities: {len(communities_random)}")
    print(f"    >>> MODULARITY Q = {Q_random:.4f}")
    print(f"    ⚠️  WARNING: Q={Q_random:.4f} in a RANDOM graph (just noise!)")
    
    # SBM graph
    print(f"\n[2] PLANTED MODEL (SBM):")
    G_sbm, true_labels = create_stochastic_block_model(n, p_in, p_out, seed=seed)
    communities_sbm = detect_communities_greedy(G_sbm)
    Q_sbm = calculate_modularity(G_sbm, communities_sbm)
    print(f"    Nodes: {G_sbm.number_of_nodes()}, Edges: {G_sbm.number_of_edges()}")
    print(f"    True communities: 2 (planted)")
    print(f"    Detected communities: {len(communities_sbm)}")
    print(f"    >>> MODULARITY Q = {Q_sbm:.4f}")
    
    print(f"\n[3] THE TRAP:")
    print(f"    Random Q:  {Q_random:.4f} (NO structure)")
    print(f"    SBM Q:     {Q_sbm:.4f} (WITH structure)")
    print(f"    >> Random graph has {'HIGHER' if Q_random > Q_sbm else 'lower'} Q!")
    print(f"    >> High modularity ≠ real communities")
    print(f"    >> Always test against null model!")
    print("="*80 + "\n")
    
    visualize_modularity_trap(G_random, communities_random, Q_random,
                             G_sbm, communities_sbm, Q_sbm, true_labels)
    
    return Q_random, Q_sbm

def visualize_modularity_trap(G_random, communities_random, Q_random,
                             G_sbm, communities_sbm, Q_sbm, true_labels):
    
    fig = plt.figure(figsize=(28, 14))
    gs = GridSpec(2, 2, figure=fig, hspace=0.25, wspace=0.15)
    
    # Random graph visualization
    ax1 = fig.add_subplot(gs[0, 0])
    pos_random = nx.spring_layout(G_random, seed=SEED, k=2.0, iterations=100, scale=10)
    
    node_to_comm = {}
    for idx, comm in enumerate(communities_random):
        for node in comm:
            node_to_comm[node] = idx
    colors_random = plt.cm.Set3(np.linspace(0, 1, len(communities_random)))
    node_colors_random = [colors_random[node_to_comm[node]] for node in G_random.nodes()]
    
    nx.draw_networkx_nodes(G_random, pos_random, node_color=node_colors_random,
                          node_size=350, alpha=0.85, ax=ax1)
    nx.draw_networkx_edges(G_random, pos_random, alpha=0.15, width=1, ax=ax1)
    ax1.set_title(f"Random Graph - Detected 'Communities'\nQ = {Q_random:.4f}\n⚠️ These are just NOISE!", 
                 fontsize=16, fontweight='bold', color='darkred')
    ax1.axis('off')
    ax1.set_xlim(-12, 12)
    ax1.set_ylim(-12, 12)
    
    # Random adjacency
    ax2 = fig.add_subplot(gs[0, 1])
    sorted_nodes_random = []
    for comm in communities_random:
        sorted_nodes_random.extend(sorted(comm))
    adj_matrix_random = nx.to_numpy_array(G_random, nodelist=sorted_nodes_random)
    im1 = ax2.imshow(adj_matrix_random, cmap='Blues', interpolation='nearest', aspect='auto')
    ax2.set_title(f"Random Graph Adjacency Matrix\n(sorted by detected communities)", 
                 fontsize=16, fontweight='bold')
    ax2.set_xlabel('Node', fontsize=12)
    ax2.set_ylabel('Node', fontsize=12)
    plt.colorbar(im1, ax=ax2, fraction=0.046, pad=0.04)
    
    # SBM visualization
    ax3 = fig.add_subplot(gs[1, 0])
    pos_sbm = nx.spring_layout(G_sbm, seed=SEED, k=1.5, iterations=100, scale=10)
    colors_true = ['#e74c3c' if true_labels[node] == 0 else '#3498db' for node in G_sbm.nodes()]
    
    nx.draw_networkx_nodes(G_sbm, pos_sbm, node_color=colors_true,
                          node_size=350, alpha=0.85, ax=ax3)
    nx.draw_networkx_edges(G_sbm, pos_sbm, alpha=0.12, width=1, ax=ax3)
    ax3.set_title(f"SBM Graph - True Communities\nQ = {Q_sbm:.4f}\n✓ Real planted structure", 
                 fontsize=16, fontweight='bold', color='darkgreen')
    ax3.axis('off')
    ax3.set_xlim(-12, 12)
    ax3.set_ylim(-12, 12)
    
    red_patch = mpatches.Patch(color='#e74c3c', label='Community A')
    blue_patch = mpatches.Patch(color='#3498db', label='Community B')
    ax3.legend(handles=[red_patch, blue_patch], loc='upper right', fontsize=12, framealpha=0.9)
    
    # SBM adjacency
    ax4 = fig.add_subplot(gs[1, 1])
    sorted_nodes_sbm = sorted(G_sbm.nodes(), key=lambda x: true_labels[x])
    adj_matrix_sbm = nx.to_numpy_array(G_sbm, nodelist=sorted_nodes_sbm)
    im2 = ax4.imshow(adj_matrix_sbm, cmap='Blues', interpolation='nearest', aspect='auto')
    
    boundary = len(G_sbm.nodes()) // 2
    ax4.axhline(y=boundary-0.5, color='red', linewidth=3, linestyle='--', alpha=0.8)
    ax4.axvline(x=boundary-0.5, color='red', linewidth=3, linestyle='--', alpha=0.8)
    
    ax4.set_title(f"SBM Adjacency Matrix\n(sorted by true communities)", 
                 fontsize=16, fontweight='bold')
    ax4.set_xlabel('Node', fontsize=12)
    ax4.set_ylabel('Node', fontsize=12)
    plt.colorbar(im2, ax=ax4, fraction=0.046, pad=0.04)
    
    fig.suptitle('THE MODULARITY TRAP: Why Q > 0 ≠ Real Communities', 
                fontsize=22, fontweight='bold', y=0.99)
    
    plt.tight_layout()
    plt.savefig('../figures/4_modularity_trap.png', dpi=200, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: ../figures/4_modularity_trap.png")

def main():
    print("\n" + "="*80)
    print(" NETWORK COMMUNITY DETECTION DEMO")
    print("="*80)
    
    N = 100
    p_er = 0.05
    p_in = 0.3
    p_out = 0.05
    
    print("\n[1] Generating NULL MODEL...")
    G_random = create_erdos_renyi_graph(N, p_er, SEED)
    visualize_null_model(G_random)
    
    print("\n[2] Generating PLANTED MODEL (SBM)...")
    G_sbm, group_labels = create_stochastic_block_model(N, p_in, p_out, SEED)
    visualize_sbm(G_sbm, group_labels, p_in, p_out)
    
    print("\n[3] Demonstrating DETECTABILITY THRESHOLD...")
    visualize_detectability_spectrum(N, p_in, SEED)
    
    print("\n[4] Demonstrating MODULARITY TRAP...")
    Q_random, Q_sbm = demonstrate_modularity_trap(N, p_er, p_in, p_out, SEED)
    
    print("\n" + "="*80)
    print(" COMPLETE - All plots saved!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()

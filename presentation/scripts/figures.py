import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigs

# Set clearer fonts for presentation slides
plt.rcParams.update({'font.size': 14})

def plot_structure_vs_metadata():
    """
    Visual 1: Generates a graph where structural communities (topology)
    do not align with metadata labels.
    """
    # 1. Generate a Network with clear structure (3 communities)
    # Using Stochastic Block Model (SBM)
    sizes = [30, 30, 30]
    probs = [[0.5, 0.05, 0.05], 
             [0.05, 0.5, 0.05], 
             [0.05, 0.05, 0.5]]
    
    G = nx.stochastic_block_model(sizes, probs, seed=42)
    pos = nx.spring_layout(G, seed=42)  # Layout based on structure

    # 2. Define "True" Structure (the blocks)
    true_communities = []
    for i, size in enumerate(sizes):
        true_communities.extend([i] * size)

    # 3. Define "Metadata" (Noisy/Misaligned)
    # We shuffle 60% of the labels to simulate "dormitory assignments" that don't match friends
    metadata = np.array(true_communities)
    n_shuffle = int(len(metadata) * 0.6)
    shuffle_indices = np.random.choice(len(metadata), n_shuffle, replace=False)
    metadata[shuffle_indices] = np.random.permutation(metadata[shuffle_indices])

    # 4. Plot Side-by-Side
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Structural Communities
    nx.draw_networkx_nodes(G, pos, node_color=true_communities, cmap='viridis', node_size=100, ax=axes[0])
    nx.draw_networkx_edges(G, pos, alpha=0.3, ax=axes[0])
    axes[0].set_title("Network Topology (Structure)\n(What the algorithm sees)", fontsize=16)
    axes[0].axis('off')

    # Right: Metadata Labels
    nx.draw_networkx_nodes(G, pos, node_color=metadata, cmap='plasma', node_size=100, ax=axes[1])
    nx.draw_networkx_edges(G, pos, alpha=0.3, ax=axes[1])
    axes[1].set_title("Metadata Labels (e.g., Dorms)\n(Misaligned with structure)", fontsize=16)
    axes[1].axis('off')

    plt.tight_layout()
    plt.savefig("../figures/structure_vs_metadata.png", dpi=300)
    print("Generated: ../figures/structure_vs_metadata.png")
    plt.show()

def plot_spectral_eigenvalues():
    """
    Visual 2: Simulates the eigenvalue spectrum of the Non-Backtracking Matrix.
    Shows the 'Bulk' (noise) vs 'Signal' (outliers).
    """
    # Parameters for simulation
    N = 1000  # Number of eigenvalues to simulate
    radius = 5.0 # Radius of the bulk noise (sqrt(c))
    
    # 1. Generate Bulk Noise (Random eigenvalues inside a circle)
    # Rejection sampling to get uniform distribution inside a circle
    theta = np.random.uniform(0, 2*np.pi, N)
    r = radius * np.sqrt(np.random.uniform(0, 1, N))
    x_bulk = r * np.cos(theta)
    y_bulk = r * np.sin(theta)

    # 2. Generate Signal (Outliers)
    # These represent 3 communities (q=3) outside the bulk
    # Real eigenvalues significantly larger than the radius
    outliers_x = [15, 8, 7.5] 
    outliers_y = [0, 0, 0] # Real eigenvalues lie on the x-axis

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot Bulk
    ax.scatter(x_bulk, y_bulk, c='lightgray', alpha=0.5, label='Bulk Noise (Random part)')
    
    # Plot Spectral Circle Boundary
    circle = plt.Circle((0, 0), radius, color='black', fill=False, linestyle='--', linewidth=2, label='Spectral Radius $\sqrt{c}$')
    ax.add_artist(circle)

    # Plot Signal Outliers
    ax.scatter(outliers_x, outliers_y, c='red', s=150, edgecolors='black', label='Signal (Communities)')

    # Annotations
    ax.text(15, 1.5, 'Leading Eigenvalue', fontsize=12, ha='center')
    ax.text(7.75, 1.5, 'Community Eigenvalues\n(q=3)', fontsize=12, ha='center')

    # Styling
    ax.set_aspect('equal')
    ax.set_xlabel("Real Part")
    ax.set_ylabel("Imaginary Part")
    ax.set_title("Eigenvalues of Non-Backtracking Matrix ($B$)\nSeparation of Signal vs. Noise", fontsize=16)
    ax.legend(loc='lower right')
    ax.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig("../figures/spectral_eigenvalues.png", dpi=300)
    print("Generated: ../figures/spectral_eigenvalues.png")
    plt.show()

# Run the functions
if __name__ == "__main__":
    plot_structure_vs_metadata()
    plot_spectral_eigenvalues()
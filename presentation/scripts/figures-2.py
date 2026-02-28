import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def plot_signal_vs_noise_matrix():
    """
    Generates a visual comparison of 'Noise' (Random Graph) 
    vs 'Signal' (Stochastic Block Model).
    """
    N = 100
    
    # 1. Generate NOISE (Erdos-Renyi Random Graph)
    # No structure, just random edges
    G_noise = nx.erdos_renyi_graph(N, p=0.15, seed=42)
    A_noise = nx.to_numpy_array(G_noise)

    # 2. Generate SIGNAL (Stochastic Block Model)
    # Clear community structure
    sizes = [33, 33, 34]
    # High prob inside (0.5), Low prob between (0.05)
    probs = [[0.5, 0.05, 0.05], 
             [0.05, 0.5, 0.05], 
             [0.05, 0.05, 0.5]]
    G_signal = nx.stochastic_block_model(sizes, probs, seed=42)
    A_signal = nx.to_numpy_array(G_signal)

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot Noise
    axes[0].spy(A_noise, markersize=2, color='black')
    axes[0].set_title("NOISE (Random Matrix)\nStandard methods get confused here", fontsize=14)
    axes[0].set_xticks([])
    axes[0].set_yticks([])
    # Add red box to show lack of structure
    rect = plt.Rectangle((0,0), N-1, N-1, linewidth=3, edgecolor='red', facecolor='none')
    axes[0].add_patch(rect)

    # Plot Signal
    axes[1].spy(A_signal, markersize=2, color='black')
    axes[1].set_title("SIGNAL (Community Structure)\nWhat Spectral Methods recover", fontsize=14)
    axes[1].set_xticks([])
    axes[1].set_yticks([])
    # Add green boxes to highlight communities
    start = 0
    for size in sizes:
        rect = plt.Rectangle((start, start), size, size, linewidth=3, edgecolor='green', facecolor='none')
        axes[1].add_patch(rect)
        start += size

    plt.tight_layout()
    plt.savefig("../figures/signal_vs_noise_matrix.png", dpi=300)
    print("Generated: ../figures/signal_vs_noise_matrix.png")
    plt.show()
    

if __name__ == "__main__":
    plot_signal_vs_noise_matrix()
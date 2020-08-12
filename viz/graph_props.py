"""
Visualization of basic graph properties.
"""
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

from BioSpecGT.graph.base import Graph
from BioSpecGT.linalg import number_of_paths


def plot_degree(adj, bins=100):
    """
    Plot a histogram of the distribution of the node degrees.
    :param adj: adjacency matrix
    :param bins: number of bins
    :return:
    """
    plt.hist([len(adj[k]) for k in adj.keys()], bins=bins)
    plt.title("Degree distribution")
    plt.xlabel('Number of neighbours')
    plt.show()


def weight_distr(adj, bins=100):
    # TODO: weights are counted twice
    """
    Plot a histogram of the edge weight distribution.
    :param adj: adjacency matrix
    :param bins: number of bins
    :return:
    """
    weight_list = [adj[k].values() for k in adj.keys()]
    plt.hist([item for sublist in weight_list for item in sublist], bins=bins)
    plt.title("Edge weight distribution")
    plt.xlabel('Weight')
    plt.show()


# TODO: remove
def _floyd(mat: np.ndarray) -> np.ndarray:
    d = mat.copy()
    d.astype(np.int)
    n = mat.shape[0]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i, k] + d[k, j] < d[i, j]:
                    d[i, j] = d[i, k] + d[k, j]
    return d


# TODO: use dijkstra or more efficient version in C/C++
def small_world_phenomena(G: Graph):
    """
    Test the small-world-phenomena for this graph graphically, i.e. plot the number of paths between nodes
    vs. the distance between nodes (as number of edges).
    See http://snap.stanford.edu/na09/02-small_world.pdf for reference.
    This works as follows:
    1. For the x-axis, the Dijkstra algorithm is used to compute the
    :param G: the graph
    :return:
    """
    v = len(G.vertices)
    adj = G.adjacency_matrix()
    x = _floyd(adj).flatten()
    y = [number_of_paths(G, i, j) for i in range(v) for j in range(v)]

    plt.scatter(x=x, y=y)

    plt.xlabel('Distance between nodes')
    plt.ylabel('Number of paths')

    plt.show()

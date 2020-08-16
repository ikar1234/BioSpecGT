"""
Visualization of basic graph properties.
"""
from matplotlib import pyplot as plt
import numpy as np

from BioSpecGT.graph.base import Graph
from BioSpecGT.linalg import number_of_paths


def plot_degree(G, bins=100):
    """
    Plot a histogram of the distribution of the node degrees.
    :param adj: adjacency matrix
    :param bins: number of bins
    :return:
    """
    adj_list = G.adjacency_list()
    plt.hist(adj_list.values(), bins=bins)
    plt.title("Degree distribution")
    plt.xlabel('Number of neighbours')
    plt.show()


def weight_distr(G, bins=100):
    """
    Plot a histogram of the edge weight distribution.
    :param G: graph
    :param bins: number of bins
    :return:
    """
    weight_list = [e.weight for e in G.edges]
    plt.hist(weight_list, bins=bins)
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

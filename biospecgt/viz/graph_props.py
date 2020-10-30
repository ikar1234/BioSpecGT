"""
Visualization of basic graph properties.
"""
from matplotlib import pyplot as plt
import numpy as np
from BioSpecGT.biospecgt.utils.graphutils import floyd

from BioSpecGT.biospecgt.graph.base import Graph
from BioSpecGT.biospecgt.linalg import number_of_paths


def plot_degree(G: Graph, bins: int = None):
    """
    Plot a histogram of the distribution of the node degrees.

    Parameters
    ----------
    G: Graph
        Input graph
    bins: int
        Number of bins to plot

    Returns
    -------

    """
    adj_list = G.adjacency_list()
    plt.hist(adj_list.values(), bins=bins)
    plt.title("Degree distribution")
    plt.xlabel('Number of neighbours')
    plt.show()


def weight_distr(G: Graph, bins: int = None):
    """
    Plot a histogram of the edge weight distribution.

    Parameters
    ----------
    G: Graph
        Input graph
    bins: int
        Number of bins to plot

    Returns
    -------

    """
    weight_list = [e.weight for e in G.edges]
    plt.hist(weight_list, bins=bins)
    plt.title("Edge weight distribution")
    plt.xlabel('Weight')
    plt.show()


def small_world_phenomena(G: Graph):
    """
    Test the small-world-phenomena for this graph graphically, i.e. plot the number of paths between nodes
    vs. the distance between nodes (as number of edges).

    Parameters
    ----------
    G: Graph
        Input graph

    Returns
    -------

    References
    -------
    See http://snap.stanford.edu/na09/02-small_world.pdf for reference.
    """
    v = len(G.vertices)
    adj = G.adjacency_matrix()
    x = floyd(adj).flatten()
    y = [number_of_paths(G, i, j) for i in range(v) for j in range(v)]

    plt.scatter(x=x, y=y)

    plt.xlabel('Distance between nodes')
    plt.ylabel('Number of paths')

    plt.show()

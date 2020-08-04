"""
Visualization of basic graph properties.
"""
from matplotlib import pyplot as plt


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

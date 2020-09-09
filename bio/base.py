"""
Base functions.
"""

# TODO: high-level only?
from BioSpecGT.graph.base import Graph, Vertex


def most_connected_gene(dct):
    """
    Gives the name of the gene with the highest number of connections.
    Works for both weighted and unweighted graphs.
    :param dct: adjacency matrix
    :return:
    """
    return max([(len(dct[k]), k) for k in dct.keys()])


def topk_genes(dct, k: int = 10):
    """
    Gives the name of the k genes with the highest number of connections.
    Works for both weighted and unweighted graphs.
    :param dct: adjacency matrix
    :param k: number of genes to output
    :return:
    """
    min_len = min(k, len(dct.keys()))
    return sorted([(len(dct[i]), i) for i in dct.keys()])[:min_len]


def top10_genes(dct):
    """
    Gives the name of the k genes with the highest number of connections.
    Works for both weighted and unweighted graphs.
    :param dct: adjacency matrix
    :return:
    """
    return topk_genes(dct)


def highest_weight_gene(dct):
    """
    Gives the name of the gene with the highest number of connections.
    Works for both weighted graphs. For
    :param dct: adjacency matrix
    :return:
    """
    return max([(sum(dct[k].values), k) for k in dct.keys()])


def connections(dct, k):
    # TODO: prettify output
    return dct[k]


def connectivity(G: Graph) -> int:
    return len(G.edges)


def betweenness(G, n: Vertex) -> int:
    """
    The betweenness of a node corresponds to the sum of the shortest paths connecting all pair of nodes in the network,
    passing through that specific node.
    :param G:
    :param n:
    :return:
    """
    # TODO: think of a low-level implementation which computes all shortest-paths and immediately
    #       increases the count, without checking if the node is in the path,  otherwise this might
    #       be inefficient

    ...


def get_gene_info(gene):
    """
    Get full info of a particular gene.
    :param gene:
    :return:
    """
    ...


def get_GO(gene):
    """
    Get GO info about a particular gene.
    :param gene:
    :return:
    """
    ...

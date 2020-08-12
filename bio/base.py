"""
Base functions.
"""


# TODO: high-level only?


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

"""
Base functions for importing the datasets.
"""
from collections import defaultdict


def _parse_graph(fname: str, weighted=False):
    # TODO: test
    """
    Parse graph from a CSV/TSV file.
    :param fname: file name
    :param weighted: keep weights of the graph
    :return: if unweighted, a list of tuples (adjacency list), otherwise a list of tuples, where the second entry is a dictionary
    """
    with open(fname, 'r+') as f:
        if weighted:
            edges = ((e.split()[0], {e.split()[1]: e.split()[2]}) for e in f.readlines()[1:])
        else:
            edges = ((e.split()[0], e.split()[1]) for e in f.readlines()[1:])
    d = defaultdict(list)
    for k, v in edges:
        d[k].append(v)
    return d


def load_ecoli_protein_network(weighted=False):
    return _parse_graph('data/E.coli.protein.links.v11.0.tsv', weighted=weighted)

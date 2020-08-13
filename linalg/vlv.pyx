import numpy as np

from BioSpecGT.graph.base import Graph

def vLv(double[:] v not None, G: Graph) -> float:
    """
    Efficiently compute the vector-matrix-vector product of the graph laplacian and a vector.
    Uses the sum of quadratic terms representation of the product.
    Runs in O(|E|). Optimal for sparse graphs.
    # TODO: dense graphs?
    :param G: undirected graph
    :param v: the vector
    :return: a real number
    """
    return sum([(v[e.out_vertex.index] - v[e.in_vertex.index]) ** 2 for e in G.edges if
                e.out_vertex.label > e.in_vertex.label])

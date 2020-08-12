"""
Basic functions on graphs involving linear algebra.
"""
import numpy as np
from numpy.linalg import matrix_power
from numpy.linalg import inv
from numpy import eye

from BioSpecGT.graph.base import Graph


def number_of_paths(G: Graph, i: int, j: int, n: int = None) -> int:
    # TODO: how to do for big/sparse graphs?
    """
    Gives the number of paths in an acyclic graph between two nodes.
    :param G: the graph
    :param i: first node
    :param j: second node
    :param n: length of path. If None, the total number is computed.
    :return:
    """
    A = G.adjacency_matrix(np.int)
    if n is not None:
        print(matrix_power(A, n)[i, j])
        return matrix_power(A, n)[i, j]
    gg = inv(eye(N=A.shape[0]) - A)
    print(gg)
    return gg[i, j]

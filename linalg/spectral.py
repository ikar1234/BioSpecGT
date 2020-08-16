"""
Spectral graph theory
"""
import numpy as np
from typing import List, Tuple
from warnings import warn

from BioSpecGT.graph.base import Graph, Vertex
from BioSpecGT.utils.graphutils import minimum_spanning_tree
from BioSpecGT.utils.packages import is_installed

from BioSpecGT.linalg.vlv import vLv

__all__ = [
    'laplacian_matrix',
    'signed_laplacian_matrix',
    'rw_laplacian_matrix',
    'normalized_laplacian_matrix',
    'bound_l2',
    'bound_l2_CBT',
    'estimate_l2',
    'compute_l2',
    'bound_conductance',
    'bound_isoparametric_number'
]


def laplacian_matrix(G: Graph) -> np.ndarray:
    g = G.adjacency_matrix()
    return np.diag(g.sum(axis=1)) - G.adjacency_matrix()


def signed_laplacian_matrix(G: Graph) -> np.ndarray:
    g = G.adjacency_matrix()
    return np.diag(g.sum(axis=1)) + G.adjacency_matrix()


def normalized_laplacian_matrix() -> np.ndarray:
    ...


def rw_laplacian_matrix() -> np.ndarray:
    """
    Get the Random-Walk Laplacian.
    :return:
    """
    ...


def compute_l2(G: Graph) -> float:
    """
    Compute l2 directly. Useful for small graphs.
    :return: exact value (up to a numerical error) of l2
    """
    # TODO: sparse
    return np.linalg.eigh(laplacian_matrix(G))[0][1]


def estimate_l2(G: Graph):
    """
    Estimate l2. Useful for middle-sized graphs.
    :return: estimate of l2
    """
    ...


def bound_l2(G: Graph):
    """
    Give a lower and an upper bound of l2. Useful for large graphs.
    :return: lower and upper bound of l2
    """
    span = minimum_spanning_tree(G)

    # TODO: ok?
    if is_installed('scipy'):
        from scipy.optimize import minimize


        def jac(v, g):
            return laplacian_matrix(g) @ v

        cons = ({'type': 'eq',
                 'fun': lambda x: np.array([np.sum(x) - 1])
                 })
        up = minimize(fun=vLv, args=(G), x0=np.random.normal(size=len(G.vertices)), method='trust-constr',
                      constraints=cons, jac=jac).fun
    else:
        up = ...
    # lower bound is l2 of the spanning tree
    lo = compute_l2(span)
    return lo, up


def bound_l2_CBT(G: Graph, h: int = None, n: int = None):
    """
    Give a lower and upper bound on l2 for a complete binary tree.
    Runs in O(1) since the bound are explicitly known.
    :param G: complete binary tree
    :param h: (optional) height of the tree
    :param n: (optional) number of nodes in the tree
    :return: lower and upper bound
    """
    # infer n from the graph
    if h is None and n is None:
        n = len(G.vertices)
    elif h is not None:
        n = 2 ** h - 1

    return 1 / ((n - 1) * np.log2(n)), 2 / (n - 1)


def bound_isoparametric_number(G: Graph, S: List[Vertex], l2: float = None) -> float:
    """
    Give a lower bound on the isoparametric number of a graph.
    The isoparametric number is the smallest value of the isoparametric ratio of some set of vertices of a graph.
    It tells us how close the graph is to being bipartite.
    :param G: undirected graph
    :param S: set of vertices
    :param l2: (optional) smallest non-zero eigenvalue. Will be computed if not given.
    :return: lower bound on the isoparametric number
    """
    if l2 is None:
        l2 = compute_l2(G)
    return l2 * (1 - len(S) / len(G.vertices))


def bound_conductance(G: Graph = None, d: int = None, l2: float = None):
    """
    Give a lower and an upper bound on the conductance of a d-regular graph.
    The conductance is the smallest value of the isoparametric ratio of some set of vertices of a graph.
    It tells us how close the graph is to being bipartite.
    (This is Cheeger's inequality)
    :param G: undirected graph
    :param d: number of edges for each vertex
    :param l2: (optional) smallest non-zero eigenvalue. Will be computed if not given.
    :return: lower bound on the conductance
    """
    if G is None and d is None and l2 is None:
        raise ValueError("You need to specify either the graph G or the parameters d and l2.")
    # the only meaningful bound for an empty graph
    if G is not None and len(G.vertices) == 0:
        warn('An empty graph was given')
        return 0, 0
    if d is None:
        d = G.get_degree(G.vertices[0])

    if l2 is None and G is not None:
        l2 = compute_l2(G)
    return l2 / (2 * d), (2 * l2 / d) ** 0.5

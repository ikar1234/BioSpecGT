"""
Profiler for the functions.
Corresponds mostly to the tests.
Remove after deployment.
"""
import cProfile

from BioSpecGT.graph.generator import complete_graph, complete_binary_tree, sparse_graph
from BioSpecGT.linalg.spectral import bound_l2
from BioSpecGT.utils.graphutils import minimum_spanning_tree


def profile_prim():
    n = 90
    g = complete_graph(n, directed=True)
    cProfile.runctx('minimum_spanning_tree(g)', globals(), locals())


def profile_k_regular():
    n = 160000
    cProfile.runctx('g = complete_binary_tree(n)', globals(), locals())


def profile_sparse():
    n = 1000
    p = 0.15
    cProfile.runctx('sparse_graph(n,p)', globals(), locals())


def profile_bound_l2():
    g = complete_graph(n=60)
    cProfile.runctx('bound_l2(g)', globals(), locals())


if __name__ == '__main__':
    # profile_prim()
    # profile_k_regular()
    # profile_sparse()
    profile_bound_l2()

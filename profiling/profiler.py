"""
Profiler for the functions.
Corresponds mostly to the tests.
Remove after deployment.
"""
import cProfile

from BioSpecGT.biospecgt.graph.generator import complete_graph, complete_binary_tree, sparse_graph, k_regular_graph
from BioSpecGT.biospecgt.linalg.spectral import bound_l2
from BioSpecGT.biospecgt.utils.graphutils import minimum_spanning_tree
from BioSpecGT.biospecgt.utils.graphutils import BFS

from networkx.generators import random_regular_graph


def profile_prim():
    n = 400
    g = complete_graph(n, directed=True)
    cProfile.runctx('BFS(g)', globals(), locals())


def profile_k_regular():
    n = 3500
    k = 650
    cProfile.runctx('g = k_regular_graph(n, k)', globals(), locals(), sort='tottime')
    # cProfile.runctx('g = random_regular_graph(k, n)', globals(), locals(), sort='tottime')


def profile_sparse():
    n = 1000
    p = 0.85
    cProfile.runctx('sparse_graph(n,p)', globals(), locals(), sort='tottime')


def profile_bintree():
    n = 2**14-1
    cProfile.runctx('complete_binary_tree(n)', globals(), locals(), sort='tottime')


def profile_bound_l2():
    g = complete_graph(n=400, directed=False)
    cProfile.runctx('bound_l2(g)', globals(), locals(), sort='tottime')


if __name__ == '__main__':
    # profile_prim()
    profile_k_regular()
    # profile_sparse()
    # profile_bintree()
    # profile_bound_l2()

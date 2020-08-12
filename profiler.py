"""
Profiler for the functions.
Corresponds mostly to the tests.
Remove after deployment.
"""
import cProfile

from BioSpecGT.graph.generator import complete_graph
from BioSpecGT.utils.graphutils import prim


def profile_prim():
    n = 60
    g = complete_graph(n)
    cProfile.runctx('prim(g)', globals(), locals())


if __name__ == '__main__':
    profile_prim()

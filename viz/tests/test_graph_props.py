import unittest

from BioSpecGT.graph.generator import complete_graph, k_regular_graph
from BioSpecGT.viz import small_world_phenomena


class MyTestCase(unittest.TestCase):
    def test_small_world(self):
        n = 12
        k = 4
        graph = complete_graph(n)
        small_world_phenomena(graph)


if __name__ == '__main__':
    unittest.main()

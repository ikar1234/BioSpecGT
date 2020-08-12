import unittest

from BioSpecGT.graph.generator import complete_graph
from BioSpecGT.utils.graphutils import prim


class MyTestCase(unittest.TestCase):
    def test_prim(self):
        n = 10
        g = complete_graph(n)
        g1 = prim(g)
        self.assertEqual(len(g1.vertices), n)
        self.assertEqual(len(g1.edges), n-1)


if __name__ == '__main__':
    unittest.main()

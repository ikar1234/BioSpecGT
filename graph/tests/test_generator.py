import unittest
from ..generator import *


class MyTestCase(unittest.TestCase):
    def test_k_regular_graph(self):
        n = 5
        k = 2
        graph = k_regular_graph(n, k)
        self.assertEqual(len(graph.vertices), n)
        self.assertEqual(len(graph.edges), n * k)

    def test_complete_graph(self):
        n = 1000
        graph = complete_graph(n)
        self.assertEqual(len(graph.vertices), n)
        self.assertEqual(len(graph.edges), n ** 2 - n)

    def test_path_graph(self):
        ...

    def test_cycle_graph(self):
        ...

    def test_euler_graph(self):
        ...

    def test_complete_binary_tree_dir(self):
        n = 63
        g = complete_binary_tree(n, directed=True)
        self.assertEqual(len(g.edges), n - 1)

    def test_complete_binary_tree_undir(self):
        n = 63
        g = complete_binary_tree(n, directed=False)
        self.assertEqual(len(g.edges), 2 * n - 2)


if __name__ == '__main__':
    unittest.main()

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


if __name__ == '__main__':
    unittest.main()

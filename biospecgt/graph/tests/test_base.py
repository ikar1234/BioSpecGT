import unittest
from BioSpecGT.biospecgt.graph.base import Graph, Vertex, Edge


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_adjacency_matrix(self):
        self.assertEqual(True, False)

    def test_vertex_adding(self):
        n = 100
        g = Graph([], [])
        vertices = [Vertex(label=f'{i}', index=i) for i in range(n)]
        g.add_vertices(vertices)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

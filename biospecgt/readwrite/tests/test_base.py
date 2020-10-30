import unittest
from BioSpecGT.biospecgt.readwrite import *


class MyTestCase(unittest.TestCase):
    def test_parse_edges_from_list_str(self):
        l = ['v1 v2 1', 'v1 v3 2', 'v3 v1']
        g = parse_edges_from_list(l, default_weight=6, edge_type='int')
        self.assertEqual([e.weight for e in g.edges], [1, 2, 6])

    def test_parse_edges_from_list_tuple(self):
        l = [('v1', 'v2', 1), ('v1', 'v3', 2), ('v1', 'v2')]
        g = parse_edges_from_list(l, default_weight=6, edge_type='int')
        self.assertEqual([e.weight for e in g.edges], [1, 2, 6])


if __name__ == '__main__':
    unittest.main()

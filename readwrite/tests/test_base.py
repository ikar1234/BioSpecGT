import unittest
from BioSpecGT.readwrite import *


class MyTestCase(unittest.TestCase):
    def test_parse_edges_from_list(self):
        l = ['v1 v2 1', 'v1 v3 2', 'v3 v1']
        g = parse_edges_from_list(l, default_weight=6, edge_type='int')
        print([e.weight for e in g.edges])


if __name__ == '__main__':
    unittest.main()

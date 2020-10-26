import unittest
from BioSpecGT.readwrite import *


class MyTestCase(unittest.TestCase):
    def test_parse_edges_from_list(self):
        l = ['v1 v2 1', 'v1 v3 2', 'v3 v1 5']
        g = parse_edges_from_list(l)
        print(g.vertices)


if __name__ == '__main__':
    unittest.main()

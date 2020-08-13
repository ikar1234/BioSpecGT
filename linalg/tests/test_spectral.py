import unittest

from BioSpecGT.graph.generator import k_regular_graph, complete_graph
from BioSpecGT.linalg.spectral import bound_l2


class MyTestCase(unittest.TestCase):
    def test_bound_l2(self):
        g = complete_graph(n=60)
        up, lo = bound_l2(g)
        # print(f'{lo} <= l2 <= {up}')
        self.assertGreater(up, lo)


if __name__ == '__main__':
    unittest.main()

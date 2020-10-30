import unittest
from BioSpecGT.biospecgt.datasets._base import load_ecoli_protein_network


# TODO

class MyTestCase(unittest.TestCase):
    def test_ecoli(self):
        g = load_ecoli_protein_network()


if __name__ == '__main__':
    unittest.main()

"""
Base functions for importing the datasets.
"""
from collections import defaultdict
import gzip

from BioSpecGT import Graph
from BioSpecGT.readwrite import read_edgelist


def load_ecoli_protein_network() -> Graph:
    return read_edgelist('data/E.coli.protein.links.v11.0.tsv.zip', open_gzip=True)

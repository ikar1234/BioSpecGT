"""
Base classes and functions.
"""
from typing import Dict, List
import numpy as np
import scipy as sp

from BioSpecGT.biospecgt.graph.ccgenerator import CVertex, CEdge, CGraph


class Vertex(CVertex):
    pass


class Edge(CEdge):
    pass


class Graph(CGraph):
    pass

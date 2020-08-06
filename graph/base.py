"""
Base classes and functions.
"""
# TODO: abc?
# import abc
from typing import Dict, List
import numpy as np
import scipy as sp


class Vertex:
    # label of the vertex
    label: str
    # index in the graph, starts from 0
    index: int
    # meta-info about the vertex
    meta: Dict

    def __init__(self, label: str, index: int, **meta):
        self.label = label
        self.index = index
        self.meta = meta

    def __eq__(self, other):
        """
        Tests two vertices for equality. Index-invariant.
        :param other:
        :return:
        """
        return self.label == other.label


class Edge:
    out_vertex: Vertex
    in_vertex: Vertex
    has_weight: bool
    # default is 1
    weight: float

    def __init__(self, out_vertex: Vertex, in_vertex: Vertex, weight: int = None):
        self.out_vertex = out_vertex
        self.in_vertex = in_vertex
        if weight is None:
            self.has_weight = False
            weight = 1
        else:
            self.has_weight = True
        self.weight = weight

    def __eq__(self, other):
        return self.out_vertex == other.out_vertex and self.in_vertex == other.in_vertex and self.weight == other.weight

    def __str__(self):
        if self.has_weight:
            weight_str = f" with weight {self.weight}"
        else:
            weight_str = "."
        return f"An edge between {self.in_vertex.label} and {self.out_vertex.label}" + weight_str


class Graph:
    vertices: List[Vertex]
    edges: List[Edge]

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def adjacency_matrix(self):
        # TODO: vertex indexing check
        v = len(self.vertices)
        m = np.zeros((v, v))
        for e in self.edges:
            m[e.in_vertex.index, e.out_vertex.index] = 1

    def add_egdes(self, edges: List[Edge]):
        self.edges.extend(edges)

    def add_vertex(self, vertex: Vertex):
        vertex.index = len(self.vertices)
        self.vertices.append(vertex)

    def add_vertices(self, vertices: List[Vertex]):
        i = len(self.vertices)
        for v in vertices:
            v.index = i
            i += 1
        self.vertices.extend(vertices)

    def __str__(self):
        """
        Output the graph info.
        :return:
        """
        return f"A graph with {len(self.vertices)} vertices and {len(self.edges)} edges."

    def __len__(self):
        """
        Output a meaningful(?) length of the graph.
        :return:
        """
        return len(self.vertices)

    def __eq__(self, other):
        """
        Test two graphs for equality
        :param other:
        :return:
        """
        return all([v in other.vertices for v in self.vertices]) and all([v in other.edges for v in self.edges])

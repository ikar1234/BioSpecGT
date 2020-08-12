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

    def __str__(self):
        return f"A vertex with label {self.label} and following info:\n{self.meta}"


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
    directed: bool

    def __init__(self, vertices, edges, directed=True):
        self.vertices = vertices
        self.edges = edges
        self.directed = directed

    def adjacency_matrix(self, dtype=bool):
        # TODO: vertex indexing check
        v = len(self.vertices)
        m = np.zeros((v, v), dtype=dtype)
        for e in self.edges:
            m[e.in_vertex.index, e.out_vertex.index] = 1
        return m

    # TODO: compare runtime for different graphs and decide which to use
    # TODO: yield?
    def get_neighbours(self, v: Vertex) -> List[Vertex]:
        return [e.in_vertex for e in self.edges if e.out_vertex == v]

    # TODO: compare runtime for different graphs and decide which to use

    def get_degree(self, v: Vertex) -> int:
        return sum(self.adjacency_matrix()[:, v.index])

    def add_egdes(self, edges: List[Edge]):
        self.edges.extend(edges)

    def remove_egdes(self, edges: List[Edge]):
        for e in edges:
            self.edges.remove(e)

    def add_vertex(self, vertex: Vertex):
        vertex.index = len(self.vertices)
        self.vertices.append(vertex)

    # def from_indices(self, inds: List[int]) -> List[Vertex]:
    #     """
    #     Given a list of indices, return the corresponding nodes in the graph.
    #     :param inds: list of integer-values indices
    #     :return:
    #     """
    #     # TODO: better?
    #     inds.sort()
    #     return [v for v in self.vertices if v.index in inds]

    def add_vertices(self, vertices: List[Vertex]):
        """
        Add and label a set of nodes
        :param vertices:
        :return:
        """
        i = len(self.vertices)
        for v in vertices:
            v.index = i
            i += 1
        self.vertices.extend(vertices)

    def find_by_index(self, index: int):
        """
        Find a node by its index.
        :param index:
        :return:
        """
        return [v for v in self.vertices if v.index == index]

    def copy(self):
        """
        Return a shallow copy of the graph
        :return:
        """
        return Graph(self.vertices, self.edges)

    def make_undirected(self):
        """
        Make a directed graph undirected by added edges in both ways
        :return:
        """
        # TODO: detect cycles of length 2 in the graph to make this efficient
        self.add_egdes(
            [Edge(e.in_vertex, e.out_vertex) for e in self.edges if Edge(e.in_vertex, e.out_vertex) not in self.edges])
        return self

    def make_unweighted(self):
        """
        Make the graph unweighted, by removing the edge weights.
        :return:
        """
        for e in self.edges:
            e.has_weight = False
            e.weight = 1
        return self

    def make_weighted(self, weights=None):
        """
        Make the graph unweighted, by removing the edge weights.
        :return:
        """
        for ind, e in enumerate(self.edges):
            e.has_weight = True
            # default weight for unweighted graphs is 1
            if weights is not None and len(weights) > ind:
                e.weight = weights[ind]
        return self

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
        Test two graphs for equality.
        :param other:
        :return:
        """
        return all([v in other.vertices for v in self.vertices]) and all([v in other.edges for v in self.edges])

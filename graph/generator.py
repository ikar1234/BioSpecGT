"""
Function for generating graphs.
"""
from BioSpecGT.graph.base import Graph, Vertex, Edge
import numpy as np
import itertools
from typing import List, Dict
from time import time


# from networkx.generators import complete_graph


def k_regular_graph(n: int, k: int) -> Graph:
    # TODO: optimize
    """
    Generate a random k-regular graph (each vertex has degree k).
    :param n: the number of vertices k
    :param k: the degree of each vertex
    :return: a Graph object
    """
    t1 = time()
    vertices: List[Vertex] = [Vertex(label=f'{i}') for i in range(n)]

    t2 = time()
    print('Init: ', t2 - t1)
    rand_vert = np.random.choice(a=vertices, size=k)
    edges: List[Edge] = [Edge(out_vertex=v, in_vertex=i) for i in rand_vert for v in vertices]

    t3 = time()
    print('Loop: ', t3 - t2)
    return Graph(vertices=vertices, edges=edges)


def complete_graph(n: int) -> Graph:
    t1 = time()
    # TODO: faster?
    vertices: List[Vertex] = [Vertex(label=f'{i}') for i in range(n)]
    edges = [Edge(v, i) for v, i in itertools.permutations(vertices, 2)]
    print(time() - t1)
    return Graph(vertices, edges)


def sparse_graph(n: int, perc: float = 0.05) -> Graph:
    ...


def dense_graph(n: int, perc: float = 0.85) -> Graph:
    ...


def path_graph() -> Graph:
    ...


def cycle_graph() -> Graph:
    ...


def complete_binary_tree() -> Graph:
    ...


def petersen_graph() -> Graph:
    ...


def morse_graph() -> Graph:
    ...

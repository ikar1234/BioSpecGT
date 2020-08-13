"""
Function for generating graphs.
"""
import random

from BioSpecGT.graph.base import Graph, Vertex, Edge
import numpy as np
import itertools
from typing import List

__all__ = ['k_regular_graph',
           'empty_graph',
           'complete_graph',
           'petersen_graph',
           'morse_graph',
           'sparse_graph',
           'cycle_graph',
           'dense_graph',
           'path_graph',
           'complete_binary_tree'
           ]


def empty_graph(n: int = 0) -> Graph:
    """
    Empty graph with or without vertices.
    :param n: (optional) number of vertices
    :return:
    """
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]

    return Graph(vertices, [])


def k_regular_graph(n: int, k: int) -> Graph:
    # TODO: optimize
    """
    Generate a random k-regular graph (each vertex has degree k).
    :param n: the number of vertices k
    :param k: the degree of each vertex
    :return: a Graph object
    """
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]

    rand_vert = np.random.choice(a=vertices, size=k)
    # item for sublist in rand_vert for item in sublist
    # TODO
    edges: List[Edge] = [Edge(out_vertex=v, in_vertex=i) for i in rand_vert for v in vertices]

    return Graph(vertices=vertices, edges=edges)


def complete_graph(n: int) -> Graph:
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]
    edges = [Edge(v, i) for v, i in itertools.permutations(vertices, 2)]
    return Graph(vertices, edges)


def sparse_graph(n: int, perc: float = 0.05) -> Graph:
    """
    Create a random sparse graph.
    :param n: number of vertices
    :param perc: percentage of possible edges
    :return:
    """
    return _graph_perc(n, perc)


def _graph_perc(n: int, perc: float) -> Graph:
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]
    v1 = random.choices(vertices, k=int(perc * n ** 2))
    v2 = random.choices(vertices, k=int(perc * n ** 2))
    edges = [Edge(v, i) for v, i in zip(v1, v2)]
    return Graph(vertices, edges)


def dense_graph(n: int, perc: float = 0.85) -> Graph:
    """
    Create a random dense graph.
    :param n: number of vertices
    :param perc: percentage of possible edges
    :return:
    """
    return _graph_perc(n, perc)


def euler_graph(n: int, cycle=True) -> Graph:
    """
    Create a random graph with an Euler path.
    :param n: number of vertices
    :param cycle: if True, there is also an Euler cycle in the graph.
    :return:
    """
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]
    v2 = random.choices(vertices, k=n)
    edges = [Edge(v, i) for v, i in zip(vertices, v2)]


def path_graph(n: int, directed=False) -> Graph:
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]
    edges = [Edge(vertices[i], vertices[i + 1]) for i in range(n - 1)]
    if not directed:
        edges += [Edge(vertices[i], vertices[i - 1]) for i in range(1, n)]

    return Graph(vertices, edges, directed=directed)


def cycle_graph(n: int) -> Graph:
    p = path_graph(n)
    edge = [Edge(p.vertices[-1], p.vertices[0])]
    p.add_egdes(edge)
    return p


def complete_binary_tree(n: int, directed=False) -> Graph:
    # TODO: test that n is a Mersenne prime
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]
    # TODO: extend?
    edges = [Edge(vertices[i], vertices[2 * i + 1]) for i in range(n // 2)]
    edges += [Edge(vertices[i], vertices[2 * i + 2]) for i in range(n // 2 - 1)]
    if directed:
        return Graph(vertices, edges, directed=True)
    edges += [Edge(vertices[2 * i + 1], vertices[i]) for i in range(n // 2)]
    edges += [Edge(vertices[2 * i + 2], vertices[i]) for i in range(n // 2 - 1)]
    return Graph(vertices, edges)


def petersen_graph() -> Graph:
    ...


def morse_graph() -> Graph:
    ...

"""
Function for generating graphs.
"""
from BioSpecGT.graph.base import Graph, Vertex, Edge
import numpy as np
import itertools
from typing import List, Dict
from time import time

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
    t1 = time()
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]

    t2 = time()
    print('Init: ', t2 - t1)
    rand_vert = np.random.choice(a=vertices, size=k)
    # item for sublist in rand_vert for item in sublist
    # TODO
    edges: List[Edge] = [Edge(out_vertex=v, in_vertex=i) for i in rand_vert for v in vertices]

    t3 = time()
    print('Loop: ', t3 - t2)

    for i in range(len(edges)):
        print(edges[i])

    return Graph(vertices=vertices, edges=edges)


def complete_graph(n: int) -> Graph:
    # t1 = time()
    # TODO: faster?
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]
    edges = [Edge(v, i) for v, i in itertools.permutations(vertices, 2)]
    # print(time() - t1)
    return Graph(vertices, edges)


def sparse_graph(n: int, perc: float = 0.05) -> Graph:
    """
    Create a random sparse graph.
    :param n: number of vertices
    :param perc: percentage of possible edges
    :return:
    """
    ...


def dense_graph(n: int, perc: float = 0.85) -> Graph:
    """
    Create a random dense graph.
    :param n: number of vertices
    :param perc: percentage of possible edges
    :return:
    """
    ...


def euler_graph(n: int, cycle=True) -> Graph:
    """
    Create a random graph with an Euler path.
    :param n: number of vertices
    :param cycle: if True, there is also an Euler cycle in the graph.
    :return:
    """
    # TODO
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]


def path_graph(n: int) -> Graph:
    vertices: List[Vertex] = [Vertex(label=f'{i}', index=i) for i in range(n)]
    edges = [Edge(vertices[i], vertices[i + 1]) for i in range(n)]

    return Graph(vertices, edges).make_undirected()


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
    edges.extend([Edge(vertices[i], vertices[2 * i + 2]) for i in range(n // 2)])
    if directed:
        return Graph(vertices, edges)
    return Graph(vertices, edges).make_undirected()


def petersen_graph() -> Graph:
    ...


def morse_graph() -> Graph:
    ...

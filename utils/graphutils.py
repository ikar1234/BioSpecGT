"""
Graph utilities, such as algorithms and functions.
"""
from BioSpecGT.graph.base import Graph, Edge

import numpy as np
import heapq
from .prim import prim


def minimum_spanning_tree(G: Graph) -> Graph:
    # TODO: more?
    return prim(G)


def prim1(G: Graph) -> Graph:
    # TODO: Cython?
    """
    Prim's algorithm for minimal spanning tree.
    :param G: graph
    :return: minimal spanning tree
    """
    vl = len(G.vertices)

    pi = np.ones(vl) * np.inf
    pred = np.ones(vl, dtype=int) * (-1)
    h = []
    for v in G.vertices:
        ind = v.index
        heapq.heappush(h, (ind, pi[ind]))
    while len(h) > 0:
        u = heapq.heappop(h)
        # vertices in h
        h_vert = [x[0] for x in h]
        for e in G.edges:
            w = e.in_vertex
            ind = w.index
            weight = e.weight
            # TODO: optimize searching the whole heap
            if ind in h_vert and weight < pi[ind]:
                pred[ind] = u[0]
                pi[ind] = weight
                heapq.heappush(h, (ind, pi[ind]))
    # sorted by their indices
    vertices = G.vertices
    edges = [Edge(vertices[v.index], vertices[pred[v.index]]) for v in vertices if pred[v.index] != -1]
    if not G.directed:
        return Graph(vertices, edges).make_undirected()
    return Graph(vertices, edges)


def dijkstra(mat: np.ndarray):
    n = mat.shape[0]
    pred = np.ones(n) * (-1)
    pi = np.ones(n) * np.inf
    pi[0] = 0
    h = []
    heapq.heappush(h, (pi[0], 0))
    while len(h) > 0:
        v = heapq.heappop(h)
        # print(f'Minimum {v}')
        v_0 = v[1]
        for ind, w in enumerate(mat[v_0, :]):
            if mat[v_0, ind] == np.inf:
                continue
            old_w = pi[ind]
            if pi[ind] > pi[v_0] + mat[v_0, ind]:
                pi[ind] = pi[v_0] + mat[v_0, ind]
                pred[ind] = v_0
                if ind in map(lambda x: x[1], h):
                    # remove w
                    i = h.index((old_w, ind))
                    h[i] = h[-1]
                    heapq.heappop(h)
                    heapq.heapify(h)
                heapq.heappush(h, (pi[ind], ind))
    print(pi)
    print(pred)


def bellmann_ford(mat: np.ndarray):
    n = mat.shape[0]
    pred = np.ones(n) * (-1)
    pi = np.ones(n) * np.inf
    pi[0] = 0

    for i in range(n):
        print(pred, pi)
        for w in range(n):
            for v in range(n):
                if pi[w] > pi[v] + mat[v, w]:
                    pi[w] = pi[v] + mat[v, w]
                    pred[w] = v
    print(pi)
    print(pred)
    for w in range(n):
        for v in range(n):
            if pi[w] > pi[v] + mat[v, w]:
                return False


def floyd(mat: np.ndarray):
    d = mat.copy()
    n = mat.shape[0]

    for k in range(2):
        for i in range(n):
            for j in range(n):
                if d[i, k] + d[k, j] < d[i, j]:
                    d[i, j] = d[i, k] + d[k, j]
    return d

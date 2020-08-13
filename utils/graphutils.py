"""
Graph utilities, such as algorithms and functions.
"""
from BioSpecGT.graph.base import Graph, Edge

import numpy as np
import heapq
from .prim import prim, BFS


def minimum_spanning_tree(G: Graph) -> Graph:
    if G.weighted:
        return prim(G)
    else:
        # TODO: profile and optimize
        return BFS(G)


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

from BioSpecGT.graph.base import Graph, Edge

import numpy as np
import heapq
from collections import deque

def prim(G: Graph) -> Graph:
    """
    Prim's algorithm for minimal spanning tree.
    :param G: graph
    :return: minimal spanning tree
    """
    cdef int vl,w,ind
    cdef double weight
    cdef int[:] h_vert
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
            if ind in h_vert and weight < pi[ind]:
                pred[ind] = u[0]
                pi[ind] = weight
                heapq.heappush(h, (ind, pi[ind]))

    vertices = G.vertices
    edges = [Edge(vertices[v.index], vertices[pred[v.index]]) for v in vertices if pred[v.index] != -1]
    if not G.directed:
        return Graph(vertices, edges).make_undirected()
    return Graph(vertices, edges)

def BFS(G: Graph) -> Graph:

    cdef int vl, ind

    st = deque([])
    v0 = G.vertices[0]
    st.append(v0)

    vl = len(G.vertices)

    pred = np.ones(vl, dtype=int) * (-1)

    vis = np.zeros(vl, dtype=bool)

    vis[v0.index] = True

    adj_list = G.adjacency_list()

    while len(st) > 0:
        v = st.pop()
        for w in adj_list[v]:
            ind = w.index
            if not vis[ind]:
                st.append(w)
                vis[ind] = True
                pred[ind] = v.index

    vertices = G.vertices
    edges = [Edge(vertices[v.index], vertices[pred[v.index]]) for v in vertices if pred[v.index] != -1]
    if not G.directed:
        return Graph(vertices, edges).make_undirected()
    return Graph(vertices, edges)

from BioSpecGT.graph.base import Graph, Edge

import numpy as np
import heapq

def prim(G: Graph) -> Graph:
    """
    Prim's algorithm for minimal spanning tree.
    :param G: graph
    :return: minimal spanning tree
    """
    cdef int vl
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
    # sorted by their indices
    vertices = G.vertices
    edges = [Edge(vertices[v.index], vertices[pred[v.index]]) for v in vertices if pred[v.index] != -1]
    if not G.directed:
        return Graph(vertices, edges).make_undirected()
    return Graph(vertices, edges)

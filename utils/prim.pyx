from BioSpecGT.graph.base import Graph, Edge

import numpy as np
cimport numpy as np
import heapq
cimport cython
from collections import deque

np.import_array()

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

DTYPE = np.int
ctypedef np.int_t DTYPE_t

@cython.boundscheck(False)
@cython.wraparound(False)
def BFS(G: Graph) -> Graph:

    cdef int vl, v0, i
    cdef dict adj_list
    cdef list w_neigh
    cdef np.ndarray[DTYPE_t] pred, vis

    st = deque([])

    gvert = G.vertices
    vl = len(gvert)
    if vl == 0:
        return Graph([],[])
    v0 = gvert[0].index
    st.append(v0)


    pred = np.ones(vl, dtype=int) * (-1)

    vis = np.zeros(vl, dtype=bool)

    vis[v0] = True

    adj_list = G.adjacency_list(inds=True)

    while len(st) > 0:
        v = st.pop()
        w_neigh = adj_list[v]
        for i in range(w_neigh):
            w = w_neigh[i]
            if not vis[w]:
                st.append(w)
                vis[w] = True
                pred[w] = v


    edges = [Edge(gvert[pred[v.index]], gvert[v.index]) for v in gvert if pred[v.index] != -1]
    if not G.directed:
        return Graph(gvert, edges).make_undirected()
    return Graph(gvert, edges)

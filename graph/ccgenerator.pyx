# cython: boundscheck=False
# cython: wraparound=False

import numpy as np
cimport numpy as np
cimport cython
from itertools import chain

np.import_array()

from BioSpecGT.graph.base import Graph, Edge

DTYPE = np.int
ctypedef np.int_t DTYPE_t

cdef class CVertex:
    def __cinit__(self, label: str, index: int, **meta):
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

    def __hash__(self):
        return hash(self.index)

    def __str__(self):
        return f"A vertex with label {self.label} and following info:\n{self.meta}"


def _k_regular_graph(unsigned int n, unsigned int k, bint selfloop):
    """
    Generate a random k-regular graph (each vertex has degree k).
    :param n: the number of vertices k
    :param k: the degree of each vertex
    :param selfloop: self-loops for some nodes
    :return: a Graph object
    """
    cdef list vertices, edges
    cdef np.ndarray[DTYPE_t] rand_vert
    cdef Py_ssize_t i, j
    cdef int vt

    vertices = [Vertex(label=f'{vt}', index=vt) for vt in range(n)]
    edges = []
    for i in range(n):
        if selfloop:
            rand_vert = np.random.choice(a=range(n), size=k)
        else:
            rand_vert = np.random.choice(a=chain(range(i), range(i + 1, n)), size=k)
        edges += [Edge(vertices[i], vertices[j]) for j in rand_vert[i * k:(i + 1) * k]]

    return Graph(vertices=vertices, edges=edges)

def _cgraph_perc(unsigned int n, double perc):
    cdef list vertices, edges
    cdef np.ndarray[DTYPE_t] v1, v2
    cdef int v, i

    vertices = [Vertex(label=f'{i}', index=i) for i in range(n)]

    v1 = np.random.choice(a=range(n), k=int(perc * n ** 2))
    v2 = np.random.choice(a=range(n), k=int(perc * n ** 2))
    edges = [Edge(vertices[v], vertices[i]) for v, i in zip(v1, v2)]
    return Graph(vertices, edges)

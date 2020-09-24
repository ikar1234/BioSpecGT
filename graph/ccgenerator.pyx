# cython: boundscheck=False
# cython: wraparound=False

import numpy as np
cimport numpy as np
cimport cython
from itertools import chain

np.import_array()

DTYPE = np.int
ctypedef np.int_t DTYPE_t

cdef class CVertex:
    cdef public int index
    cdef public str label
    cdef readonly dict meta

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

    def __hash__(self):
        return hash(self.index)

    def __str__(self):
        return f"A vertex with label {self.label} and following info:\n{self.meta}"

cdef class CEdge:
    cdef public CVertex in_vertex
    cdef public CVertex out_vertex
    cdef public bint has_weight
    cdef public float weight

    # __slots__ = ['out_vertex', 'in_vertex', 'has_weight', 'weight']

    def __init__(self, out_vertex: CVertex, in_vertex: CVertex, weight: float = None):
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

    def __hash__(self):
        return hash((self.in_vertex.index, self.out_vertex.index))

    def __str__(self):
        cdef str weight_str

        if self.has_weight:
            # TODO: compare
            # weight_str = f" with weight {self.weight}"
            weight_str = " with weight {}".format(self.weight)
        else:
            weight_str = "."
        return f"An edge between {self.in_vertex.label} and {self.out_vertex.label}" + weight_str

cdef class CGraph:
    cdef public list vertices
    cdef public list edges
    cdef public bint directed
    cdef public bint weighted

    # __slots__ = ['vertices', 'edges', 'directed', 'weighted']

    def __init__(self, vertices, edges, directed=False):
        self.vertices = vertices
        self.edges = edges
        self.directed = directed

        cdef int l
        l = len(self.edges)
        # take info about weights from the first edge
        # empty graphs are unweighted per default
        self.weighted = l and self.edges[0].has_weight

    def adjacency_matrix(self, dtype=np.bool):
        cdef int v
        cdef CEdge e

        v = len(self.vertices)
        m = np.zeros((v, v), dtype=dtype)
        for e in self.edges:
            m[e.in_vertex.index, e.out_vertex.index] = e.weight
        return m

    cdef dict adjacency_list(self, inds=False):
        """
        Get the adjacency list of a graph.
        :param inds: whether to use the indices of the nodes.
        :return:
        """
        cdef dict d
        cdef CEdge e

        if inds:
            d = {}.fromkeys((v.index for v in self.vertices), [])
            for e in self.edges:
                d[e.out_vertex.index].append(e.in_vertex.index)
        else:
            d = {}.fromkeys(self.vertices, [])
            for e in self.edges:
                d[e.out_vertex].append(e.in_vertex)
        return d

    cdef list get_neighbours(self, v):
        cdef CEdge e
        return [e.in_vertex for e in self.edges if e.out_vertex == v]

    cdef int get_degree(self, CVertex v):
        return len(self.get_neighbours(v))

    cdef void add_egdes(self, edges):
        self.edges += edges

    cdef void remove_egdes(self, edges):
        cdef CEdge e
        for e in edges:
            self.edges.remove(e)

    cdef void add_vertex(self, vertex):
        vertex.index = len(self.vertices)
        self.vertices.append(vertex)

    cdef void add_vertices(self, vertices):
        """
        Add and label a set of nodes
        :param vertices:
        :return:
        """
        cdef int i
        cdef CVertex v

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
        cdef CVertex v
        return [v for v in self.vertices if v.index == index]

    cdef CGraph copy(self):
        """
        Return a shallow copy of the graph
        :return:
        """
        return CGraph(self.vertices, self.edges)

    cdef CGraph make_undirected(self):
        """
        Make a directed graph undirected by added edges in both ways
        :return:
        """
        self.add_egdes(
            [CEdge(e.in_vertex, e.out_vertex) for e in self.edges])
        self.edges = list(set(self.edges))
        self.directed = False
        return self

    cdef CGraph make_unweighted(self):
        """
        Make the graph unweighted, by removing the edge weights.
        :return:
        """
        for e in self.edges:
            e.has_weight = False
            e.weight = 1
        return self

    cdef CGraph make_weighted(self, weights=None):
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

    vertices = [CVertex(label=f'{vt}', index=vt) for vt in range(n)]
    edges = []
    for i in range(n):
        if selfloop:
            rand_vert = np.random.choice(a=range(n), size=k)
        else:
            rand_vert = np.random.choice(a=chain(range(i), range(i + 1, n)), size=k)
        edges += [CEdge(vertices[i], vertices[j]) for j in rand_vert[i * k:(i + 1) * k]]

    return CGraph(vertices=vertices, edges=edges)

def _cgraph_perc(unsigned int n, double perc):
    cdef list vertices, edges
    cdef np.ndarray[DTYPE_t] v1, v2
    cdef int v, i

    vertices = [CVertex(label=f'{i}', index=i) for i in range(n)]

    v1 = np.random.choice(a=range(n), k=int(perc * n ** 2))
    v2 = np.random.choice(a=range(n), k=int(perc * n ** 2))
    edges = [CEdge(vertices[v], vertices[i]) for v, i in zip(v1, v2)]
    return CGraph(vertices, edges)

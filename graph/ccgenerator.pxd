from libcpp cimport bool

cdef class Vertex:
    cdef public int index
    cdef public str label
    cdef readonly dict meta

# cdef class Edge:
#     cdef public Vertex in_vertex
#     cdef public Vertex out_vertex
#     cdef public bool has_weight
#     cdef public float weight
#
# cdef class Graph:
#     cdef public list vertices
#     cdef public list edges
#     cdef public list directed
#     cdef public list weighted

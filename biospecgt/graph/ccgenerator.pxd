# from libcpp cimport bool
#
# cdef class CVertex:
#     cdef public int index
#     cdef public str label
#     cdef readonly dict meta
#
# cdef class CEdge:
#     cdef public CVertex in_vertex
#     cdef public CVertex out_vertex
#     cdef public bool has_weight
#     cdef public float weight
#
# cdef class CGraph:
#     cdef public list vertices
#     cdef public list edges
#     cdef public list directed
#     cdef public list weighted

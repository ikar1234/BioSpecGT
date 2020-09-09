"""
Kernel functions (for graphs).
"""
from BioSpecGT.graph.base import Graph, Vertex, Edge
from networkx import cartesian_product


def graph_cartesian(g1: Graph, g2: Graph):
    # node labels are (v1,v2)
    vertices = [Vertex(label=f'{v}', index=i)
                for i, v in enumerate(zip(g1.vertices, g2.vertices))]
    edges = []
    return Graph(vertices=vertices, edges=edges)


def rw_kernel(g1: Graph, g2: Graph):
    ...


def sp_kernel(g1: Graph, g2: Graph):
    ...


def sp_kernel(g1: Graph, g2: Graph):
    ...

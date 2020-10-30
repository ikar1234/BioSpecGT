"""
Kernel functions (for graphs).
"""
from BioSpecGT.biospecgt.graph.base import Graph, Vertex, Edge
from networkx import cartesian_product


def graph_cartesian(g1: Graph, g2: Graph):
    # node labels are (v1,v2)
    vertices = [Vertex(label=f'{v}', index=i)
                for i, v in enumerate(zip(g1.vertices, g2.vertices))]
    edges = []
    return Graph(vertices=vertices, edges=edges)


def rw_kernel(g1: Graph, g2: Graph):
    """
        The random-walk kernel.
        :param g1: first graph
        :param g2: second graph
        :return:
        """
    ...


def sp_kernel(g1: Graph, g2: Graph):
    """
    The shortest-path kernel.
    :param g1: first graph
    :param g2: second graph
    :return:
    """
    ...


def weisfeiler_lehman(g1: Graph, g2: Graph):
    ...

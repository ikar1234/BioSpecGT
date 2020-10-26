from typing import Union

# TODO: test

from BioSpecGT.graph.base import Graph, Edge

__all__ = [
    "write_edgelist",
    "parse_edges_from_list",
    "read_edgelist",
]


def write_edgelist(G: Graph, path: str, sep: str = '\t', comments: list = None, mark_comm: str = '#', write_meta=False):
    """
    Write a graph as an edge list to a tsv file.
    :param G: input graph
    :param path: path to write the graph
    :param sep: separator
    :param comments: list of comments to be written at top to the file
    :param mark_comm: comment marker
    :param write_meta: whether to write the meta data of the graph as a comment. meta data is distinguished
            from comments by having the marker written twice
        Example meta data line: ##source:kaggle
    :return:
    """
    header = ''
    if write_meta:
        for k, v in G.meta.items():
            header += f'{mark_comm}{mark_comm}{k}:{v}\n'
    if comments is not None:
        for c in comments:
            header += f'{mark_comm}{c}\n'
    header += f"in{sep}out"
    if G.weighted:
        header += f"{sep}weight"
    with open(path, 'w+') as f:
        f.write(header)
        f.write('\n')
        for e in G.edges:
            f.write(f'{e.in_vertex}{sep}{e.out_vertex}')
            if G.weighted:
                f.write(f'{sep}{e.weight}')
            f.write('\n')


def _convert_str(val: str, str_type: str) -> Union[str, int, float]:
    """
    Convert an input string to a particular type.
    Parameters
    ----------
    val : str
        Input string
    str_type: str
        Output type

    Returns
    -------
    The converted input, depending on the type.

    Raises
    -------
    ValueError
        In case that the input cannot be converted. The ValueError thrown is prettified.


    Notes
    -------
    This is an internal function.
    """
    if str_type == 'str' or str_type == "string" or str_type == "charcter":
        return val
    elif str_type == 'int' or str_type == "integer":
        try:
            return int(val)
        except ValueError:
            raise ValueError(f'Wrong key/value type or input. It seems that {val} cannot be converted to {str_type}.')
    elif str_type == 'float' or str_type == "decimal":
        try:
            return float(val)
        except ValueError:
            raise ValueError(f'Wrong key/value type or input. It seems that {val} cannot be converted to {str_type}.')


def _parse_meta(meta: str, key_type: str = 'str', val_type: str = 'str') -> dict:
    """
    Parse the meta data to a dictionary.
    Parameters
    ----------
    meta: str
        The line containing the meta data
    key_type: str
        Output type of the key
    val_type: str
        Output type of the value

    Returns
    -------
    A dictionary with the parsed meta data.

    Notes
    -------
    This is an internal function.
    """
    key, val = meta[2::].strip().split(':')
    key = _convert_str(key, key_type)
    val = _convert_str(val, val_type)
    d = dict()
    d[key] = val
    return d


def read_edgelist(path: str, sep: str = '\t', comments: list = None, mark_comm: str = '#', parse_meta=False,
                  meta_types: list = None):
    """
    Parse an edge list in tsv format.
    :param path: path to write the graph
    :param sep: separator
    :param comments: list of comments to be written at top to the file
    :param mark_comm: comment marker
    :param parse_meta: whether to parse the provided meta data. meta data is distinguished
            from comments by having the marker written twice
            Example meta data line: ##source:kaggle
    :param meta_types: the types of the input meta data.
            Encoding is as follows:
            string type - str,string
            int type - int, integer
            float type - float, decimal
            Example: [('str','int')]
    :return:
    """
    G = Graph()

    with open(path, 'r+') as f:
        meta = dict()
        meta_marker = mark_comm + mark_comm
        for line in f:
            if parse_meta and line.startswith(meta_marker):
                meta += _parse_meta(line.strip())


def _parse_edge(e: str, default_weight=None) -> Edge:
    """
    Parse a string into an edge.
    Parameters
    ----------
    e: str
        String
    default_weight
        Default weight value for the missing weights.

    Returns
    -------

    """
    v1, v2, *weight = e.split(' ')
    if default_weight is not None:
        weight = default_weight
    elif weight == []:
        weight = None
    return Edge(v1, v2, weight)


def parse_edges_from_list(l: list, default_weight: Union[int, float] = None, **meta):
    """
    Parse a list of edges into a graph.
    Parameters
    ----------
    l: list
        List of edges. Edges could be strings of the format 'node1 node2 (weight)' or tuples.
    sep: str
        Separator in case that edges are given by strings.
    default_weight: int or float
        If only some edges are weighted, use this value as default for the others.
    meta: dict
        Meta data of the graph

    Returns
    -------
    g: Graph

    Examples
    -------
    l1 = ['v1 v2 2', 'v1 v3 1']
    g = parse_edges_from_list(l1)


    l2 = [('v1','v2', 2), ('v1','v3', 1)]
    g = parse_edges_from_list(l2)

    """
    if l is None or len(l) == 0:
        return Graph()
    l_type = type(l[0])

    if l_type == str:
        edges = [_parse_edge(e, default_weight=default_weight) for e in l]
    elif l_type == tuple or l_type == list:
        # weighted graph with default edges
        if default_weight is not None:
            edges = [Edge(e[0], e[1], e[2]) if len(e) == 3 else Edge(e[0], e[1], default_weight) for e in l]

        # weighted graph
        elif len(l[0]) == 3:
            try:
                edges = [Edge(e[0], e[1], e[2]) for e in l]
            except IndexError:
                raise IndexError("It seems that not every edge is weighted. If this is on purpose, "
                                 "use the default_weight argument to specify default weight for the missing weights.")

        # unweighted graph
        else:
            edges = [Edge(e[0], e[1]) for e in l]
    else:
        raise ValueError('An edge must be represented either by a string or by a tuple or list.')

    return Graph(edges=edges)

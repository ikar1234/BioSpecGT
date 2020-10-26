from typing import Union

from BioSpecGT.graph.base import Graph

__all__ = [
    "write_edgelist",
    "parse_edgelist",
    "read_edgelist",
    "read_weighted_edgelist",
    "write_weighted_edgelist",
]


def write_edgelist(G: Graph, path: str, sep: str = '\t', comments: list = None, mark_comm: str = '#', write_meta=False):
    """
    Write a graph as an edge list to a tsv file.
    :param G: input graph
    :param path: path to write the graph
    :param sep: separator
    :param comments: list of comments to be written at top to the file
    :param mark_comm: comment marker
    # TODO: uncomment when meta is added
    :param write_meta: whether to write the meta data of the graph as a comment. meta data is distinguished
            from comments by having the marker written twice
        Example meta data line: ##source:kaggle
    :return:
    """
    header = ''
    # if write_meta:
    #     for k, v in G.meta.items():
    #         header += f'{mark_comm}{mark_comm}{k}:{v}\n'
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


def _parse_meta(meta: str, key_type: str, val_type: str) -> dict:
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


def parse_edgelist(G: Graph, path: str, sep: str = '\t', comments: list = None, mark_comm: str = '#', parse_meta=False,
                   meta_types: list = None):
    """
    Parse a graph from an edge list in tsv format.
    :param G: input graph
    :param path: path to write the graph
    :param sep: separator
    :param comments: list of comments to be written at top to the file
    :param mark_comm: comment marker
    # TODO: uncomment when meta is added
    :param parse_meta: whether to parse the provided meta data. meta data is distinguished
            from comments by having the marker written twice
            Example meta data line: ##source:kaggle
    :param meta_types: the types of the input meta data.
            Encoding is as follows:
            string type - str,string
            int type - int, integer
            float type - float, decimal
            Example: [('str','')]
    :return:
    """
    G = Graph()

    with open(path, 'r+') as f:
        meta = dict()
        meta_marker = mark_comm + mark_comm
        for line in f:
            if parse_meta and line.startswith(meta_marker):
                meta += _parse_meta(line.strip())


def read_edgelist():
    ...


def read_weighted_edgelist():
    ...


def write_weighted_edgelist():
    ...

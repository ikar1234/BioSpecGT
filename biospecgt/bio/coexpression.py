"""
Functions connected to co-expression networks.
"""
import numpy as np

from BioSpecGT.biospecgt import Graph


def build_coexpr(data: np.ndarray) -> Graph:
    """
    Construct the co-expression network of a set of genes from expression data.
    This is done as follows:
        - gene expression data -> take correlation coefficient
        - similarity matrix -> take threshold
        - connect vertices with correlation above the threshold
    Parameters
    ----------
    data: numpy matrix

    Returns
    -------
    A graph where two genes are connected if they expressions are correlated.

    """

    ...

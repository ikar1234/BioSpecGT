"""
Spectral graph theory
"""



def laplacian_matrix():
    ...


def normalized_laplacian_matrix():
    ...



def rw_laplacian_matrix():
    """
    Get Random-Walk Laplacian.
    :return:
    """
    ...

def compute_l2():
    """
    Compute l2 directly. Useful for small graphs.
    :return: exact value (up to a numerical error) of l2
    """
    ...


def estimate_l2():
    """
    Estimate l2. Useful for middle-sized graphs.
    :return: estimate of l2
    """
    ...


def bound_l2():
    """
    Give a lower and an upper bound of l2. Useful for large graphs.
    :return: lower and upper bound of l2
    """
    ...

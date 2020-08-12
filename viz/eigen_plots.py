"""
Plots connected to the eigenvalues and eigenvectors of the Laplacian.
"""
from matplotlib import pyplot as plt
import numpy as np


def _eigen_proj(eig1, eig2, frm=2, eigval1=None, eigval2=None, lines=True, jitter=False):
    """
    Plot the eigenvectors corresponding to the first and second non-negative eigenvalues.
    :param eig1: first eigenvector
    :param eig2: second eigenvector
    :param frm: index of smallest nonnegative eigenvalue
    :param eigval1: smallest nonnegative eigenvalue
    :param eigval2: second-smallest nonnegative eigenvalue
    :param lines: connect point to lines
    :param jitter: jitter point (in case that they overlap)
    :return: scatter plot
    """
    if jitter:
        eig1 += np.random.normal(0, 1e-2, size=eig1.shape)
        eig2 += np.random.normal(0, 1e-2, size=eig2.shape)
    plt.scatter(x=eig1, y=eig2)
    if eigval1 is not None and eigval2 is not None:
        plt.xlabel(f'{frm}. eigenvalue: {eigval1}')
        plt.ylabel(f'{frm + 1}. eigenvalue: {eigval2}')
    # lines
    if lines:
        plt.plot(eig1, eig2, 'r-')
    plt.show()


def plot_spectrum(mat: np.ndarray = None, eigs=None, sym=True):
    # TODO: test etc.
    """
    Plot the spectrum of a matrix, either by finding the eigenvalues from the matrix itself, or by giving them as a parameter.
    :param mat: (optional) matrix
    :param eigs: (optional) eigenvalues
    :param sym: symmetric matrix
    :return:
    """
    if mat is None and eigs is None:
        raise ValueError('Either the matrix or the eigenvalues must be given')
    if eigs is None:
        if sym:
            eigs = np.linalg.eigh(mat)[0]
        else:
            eigs = np.linalg.eig(mat)[0]
    plt.plot(eigs)
    plt.show()

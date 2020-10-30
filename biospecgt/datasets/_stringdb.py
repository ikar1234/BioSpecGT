"""
Functions for accessing the STRING database.
"""
import requests

# TODO

# TODO
API_KEY = 0


# TODO?
def request_():
    ...


def load_protein_network(organism: str = 'A.thaliana', id: int = 3702, weighted: bool = False):
    """
    Load the protein interaction network of an organism.
    :param organism: name of the organism
    :param id: (optional) taxonomy id of the organism. Used if the organism name was not given.
    :param weighted:
    :return:
    """
    fl = requests.get(
        url='https://string-db.org/api/tsv-no-header/interaction_partners?identifiers=[your_identifiers]&[optional_parameters]').content

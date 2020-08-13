"""
Packages handling and more.
"""
import importlib.util


def is_installed(pack: str) -> bool:
    # For illustrative purposes.
    package_name = pack

    spec = importlib.util.find_spec(package_name)
    return spec is not None

import numpy
from setuptools import setup
from Cython.Build import cythonize

import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

setup(
    ext_modules=cythonize("prim.pyx", annotate=True, include_path=[numpy.get_include()],
                          compiler_directives={'language_level': "2"}),
)

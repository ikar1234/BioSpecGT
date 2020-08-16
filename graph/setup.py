from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension("ccgenerator", ["ccgenerator.c"],
              include_dirs=[numpy.get_include()]),
]

setup(
    ext_modules=ext_modules,
)

for e in ext_modules:
    e.cython_directives = {'language_level': "3"}  # all are Python-3

# setup(
#     ext_modules=cythonize("ccgenerator.pyx"),
#     include_dirs=[numpy.get_include()],
# )

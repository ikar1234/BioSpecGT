from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

'''
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

setup(name='Foo',
      ext_modules=cythonize([Extension("bar", ["bar.pyx"], include_dirs=[numpy.get_include()])])
)
'''

# ext_modules = [
#     Extension("prim", ["prim.pyx"],
#               include_dirs=[numpy.get_include()]),
# ]

setup(name='Prim',
      ext_modules=cythonize([Extension("prim", ["prim.pyx"], include_dirs=[numpy.get_include()])])
      )

# for e in ext_modules:
#     e.cython_directives = {'language_level': "3"}  # all are Python-3

# setup(
#     ext_modules=cythonize("prim.pyx"),
#     include_dirs=[numpy.get_include()],
# )

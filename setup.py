from setuptools import setup
from distutils.util import convert_path

from Cython.Build import cythonize
import numpy

# Work around bugs in passing CFLAGS to the Cython compilation process
import os
os.environ['CFLAGS'] = '-Ofast -DNPY_NO_DEPRECATED_API'

main_ns = {}
ver_path = convert_path('internetarchivepdf/const.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

version = main_ns['__version__']
setup(
    version = version,
    download_url = 'https://github.com/internetarchive/archive-pdf-tools/archive/%s.tar.gz' % version,
    include_dirs = [numpy.get_include()],
    ext_modules = cythonize(
        ['cython/sauvola.pyx', 'cython/optimiser.pyx'],
        compiler_directives = {'language_level' : '3'},
    ),
)

from setuptools import setup, find_packages
from Cython.Build import cythonize
# python setup.py build_ext --inplace
setup(
    name="{{project_slug}}",
    version="0.1.0",
    packages=find_packages(),
    ext_modules=cythonize("cython/*.pyx"),
    install_requires=[
        # List your dependencies here if you have any
    ],
)

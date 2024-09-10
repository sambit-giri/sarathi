'''
Created on 2024-09-10
@author: Sambit Giri
Setup script
'''

import setuptools
from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize
import numpy as np
import os

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(name='sarathi',
      version='0.0.1',
      author='Sambit Giri',
      author_email='sambit.giri@gmail.com',
      packages=find_packages("src"),
      package_dir={"": "src"},
      package_data={'sarathi': ['input_data/*']},
      install_requires=requirements,
      include_package_data=True,
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
)

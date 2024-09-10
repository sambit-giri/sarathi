'''
Created on 2022-12-23
@author: Sambit Giri
Setup script
'''

from setuptools import setup, find_packages
#from distutils.core import setup


setup(name='sarathi',
      version='0.0.1',
      author='Sambit Giri',
      author_email='sambit.giri@gmail.com',
      packages=find_packages("src"),
      package_dir={"": "src"},
      package_data={'sarathi': ['input_data/*']},
      install_requires=['numpy', 'scipy', 'matplotlib',
                        'pytest'],
      include_package_data=True,
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
)

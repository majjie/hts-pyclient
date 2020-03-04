from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='redimate-pyclient',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python 3 client, to communicate with the Redimate framework',
    long_description=open('README.md').read(),
    url='https://github.com/majjie/redimate-py-client',
    author='Screebo Limited',
    author_email='admin@screebo.com'
)
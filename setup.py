from setuptools import *

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hts-pyclient',
    version='0.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python 3 client, to communicate with the HTS framework',
    long_description=long_description,
    url='https://github.com/majjie/hts-pyclient',
    author='Screebo Limited',
    author_email='admin@screebo.com',    
)
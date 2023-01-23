"""
Setup to create the package
"""
import polidoro_command
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='polidoro-command',
    version=polidoro_command.VERSION,
    description='Package to create command line command in Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/heitorpolidoro/polidoro-command',
    author='Heitor Polidoro',
    license='unlicense',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    python_requires=">=3.9"
)

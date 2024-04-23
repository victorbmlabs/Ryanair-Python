#!/usr/bin/env python
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

setup(
    name="Ryanair Python",
    version="1.0.0",
    description="Extension of ryanair-py",
    long_description_content_type="text/markdown",
    author="Victor BmLabs",
    author_email="victor@bmlabs.eu",
    url="https://github.com/victorbmlabs/RyanAir-Python",
    packages=["ryanair"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "backoff"],
    package_data={"ryanair": ["airports.csv"]},
)

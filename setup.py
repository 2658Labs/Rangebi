import os
import re

from setuptools import setup, find_packages


setup(
    name='Rangebi',
    author="2658 labs",
    version="0.0.1",
    url="https://github.com/2658labs/Rangebi",
    description="A mixed wrapper over coloroma, halo and pretty tables for building beautiful python cli applications.",
    packages=["Rangebi"],
    install_requires=[
        'colorama',
        'halo',
        'prettytable'
    ],
    # we requires python 3+
    python_requires='>=3.5',
    author_email="aspraz2658@gmail.com",
    keywords=["coloroma", "colors in python", "python", "Rangebi"],
    project_url={
        "Source Code": "http://github.com/asprazz/covid19-cli",
        "Issues": "http://github.com/asprazz/covid19-cli/issues",
        "Documentation": "https://ankush.tech/projects/covid19-cli/docs/",
    },
    license="MIT"
)

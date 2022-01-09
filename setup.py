# !/usr/bin/env python
"""Setup for cookiecutter-py3-package."""

from setuptools import find_packages, setup

__version__ = "0.15.7"

setup(
    name="cookiecutter-py3-package",
    packages=find_packages(exclude=("tests*", "testing*")),
    version=__version__,
    description="An easy Cookiecutter template for Python 3 Packaging with \
        continuous delivery using GitHub actions.",
    author="Mark Sevelj",
    license="BSD",
    author_email="mark.sevelj@dunwright.com.au",
    url="https://github.com/imAsparky/cookiecutter-py3-package",
    keywords=[
        "cookiecutter",
        "Python 3",
        "template",
        "package",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
)

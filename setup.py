"""
Python Companion to Doing Bayesian Data Analysis
"""
import pathlib
from setuptools import setup, find_packages


def get_install_requires():
    """Get install requires from requirements.txt"""
    path = pathlib.Path("requirements.txt")
    return [
        x for x in path.read_text().split("\n")
        if x and not x.startswith("#")
    ]


NAME = "doing_bayesian_data_analysis"
VERSION = "0.1"
DESCRIPTION = "Python Companion to Doing Bayesian Data Analysis"
CLASSIFIERS = [
    "Programming Language :: Python :: 3.7",
]
AUTHOR = 'Zijie "ZJ" Poh'
URL = "https://github.com/zjpoh/doing_bayesian_data_analysis"
MAINTAINER = "zjpoh"
PACKAGES = find_packages()
INSTALL_REQUIRES = get_install_requires()
SETUP_REQUIRES = ["pytest-runner"]
TESTS_REQUIRE = ["pytest"]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    classifiers=CLASSIFIERS,
    author=AUTHOR,
    url=URL,
    maintainer=MAINTAINER,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    tests_require=TESTS_REQUIRE
)

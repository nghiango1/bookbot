#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="demo-flask-vuejs-rest",
    version="1.0",
    # Modules to import from other scripts:
    packages=find_packages(),
    # Executables
    scripts=["web_interface.py"],
)

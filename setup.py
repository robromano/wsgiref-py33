#!/usr/bin/env python

"""Distutils setup file"""

from setuptools import setup, find_packages

# Metadata
PACKAGE_NAME = "wsgiref-py33"
PACKAGE_VERSION = "0.1.2-1"

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="WSGI (PEP 333) Reference Library",
    author="Phillip J. Eby",
    author_email="web-sig@python.org",
    license="PSF or ZPL",
    url="https://github.com/robromano/wsgiref-py33",
    long_description = open('README.txt').read(),
    test_suite  = 'test_wsgiref',
    packages    = ['wsgiref'],
)


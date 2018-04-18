#! /usr/bin/env python2.7
__author__ = "Adam Richardson"
__Date__ = 18 / 04 / 18

from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
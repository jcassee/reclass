#!/usr/bin/env python

from distutils.core import setup

import reclass


setup(
    name = reclass.__name__,
    description = reclass.__description__,
    long_description = open("README").read(),
    version = reclass.__version__,
    author = reclass.__author__,
    author_email = reclass.__author_email__,
    license = reclass.__license__,
    url = "https://github.com/madduck/reclass",
    packages = ["reclass"],
    entry_points = {
        'console_scripts': [
            'reclass = reclass.main:main',
        ],
    },
    install_requires = [
	'PyYAML',
    ],
)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Install as Python package:
    python3 setup.py install
"""

import setuptools
from kindlecomicconverter import __version__

NAME = 'KindleComicConverter_headless'
VERSION = __version__



setuptools.setup(
    name=NAME,
    version=VERSION,
    author='Ciro Mattia Gonano, Pawel Jastrzebski',
    author_email='ciromattia@gmail.com, pawelj@iosphe.re',
    description='KindleComicConverter sans GUI, PyQt and raven(Sentry).',
    license='ISC License (ISCL)',
    keywords=['kindle', 'kobo', 'comic', 'manga', 'mobi', 'epub', 'cbz'],
    url='http://github.com/whtsky/kcc',
    entry_points={
        'console_scripts': [
            'kcc-c2e = kindlecomicconverter.startup:startC2E',
            'kcc-c2p = kindlecomicconverter.startup:startC2P',
        ],
    },
    packages=['kindlecomicconverter'],
    install_requires=[
        'Pillow>=5.2.0',
        'psutil>=5.0.0',
        'python-slugify>=1.2.1',
    ],
    classifiers=[],
    zip_safe=False,
)

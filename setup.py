#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-xvfb',
    version='2.0.0',
    author='Florian Bruhin',
    author_email='me@the-compiler.org',
    maintainer='Florian Bruhin',
    maintainer_email='me@the-compiler.org',
    license='MIT',
    url='https://github.com/The-Compiler/pytest-xvfb',
    description='A pytest plugin to run Xvfb for tests.',
    long_description=read('README.rst'),
    py_modules=['pytest_xvfb'],
    install_requires=['pytest>=2.8.1', 'pyvirtualdisplay>=1.3'],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'xvfb = pytest_xvfb',
        ],
    },
)

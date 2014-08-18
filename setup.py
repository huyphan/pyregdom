#!/usr/bin/env python

import os
import sys

import regdom

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'regdom'
]

setup(
    name='pyregdom',
    version=regdom.__version__,
    description='Detect the registered domain for a given domain name based on Mozillas effective TLD listing',
    long_description=None,
    author='Huy Phan',
    author_email='dachuy@gmail.com',
    url='https://github.com/huyphan/pyregdom',
    packages=packages,
    package_dir={'regdom': 'regdom'},
    include_package_data=True,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
)
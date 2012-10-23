#!/usr/bin/env python

from distutils.core import setup

setup(name='KVNest',
	  version='0.5',
	  description='Objected Oriented Keys for Redis ... in Python.',
	  author='Michael Katsevman',
	  url='https://github.com/anateus/kvnest',
	  packages=['kvnest'],
	  package_dir={'kvnest':'src'})
#!/usr/bin/env python

from distutils.core import setup

setup(name='python-bitcoinrpc-tornado',
      version='0.1',
      description='Enhanced version of python-jsonrpc for use with Bitcoin',
      long_description=open('README.md').read(),
      author='Jeff Garzik <jgarzik@exmulti.com>, Alexey Evseev <alexevseev@gmail.com>',
      maintainer='Jeff Garzik <jgarzik@exmulti.com>, Alexey Evseev <alexevseev@gmail.com>',
      url='http://github.com/st4lk/python-bitcoinrpc-tornado',
      packages=['bitcoinrpc_async'],
      classifiers=['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Retrieving the data for a module within a zip archive.

"""

import sys
sys.path.insert(0, 'zipimport_example.zip')

import os
import example_package
print example_package.__file__
print example_package.__loader__.get_data('example_package/README.txt')

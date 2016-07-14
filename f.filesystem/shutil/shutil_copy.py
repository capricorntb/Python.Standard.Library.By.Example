#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Copying a file

"""

from shutil import *
import os

os.mkdir('example')
print 'BEFORE:', os.listdir('example')
copy('shutil_copy.py', 'example')
print 'AFTER:', os.listdir('example')

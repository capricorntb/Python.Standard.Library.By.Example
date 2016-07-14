#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Copying a file

"""

from shutil import *
from glob import glob

with open('example.txt', 'wt') as f:
    f.write('contents')

print 'BEFORE: ', glob('example*')
move('example.txt', 'example.out')
print 'AFTER : ', glob('example*')

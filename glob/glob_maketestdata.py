#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Create test data for the glob examples.

"""

__module_id__ = "$Id$"

import os

def mkfile(filename):
    print filename
    f = open(filename, 'wt')
    try:
        f.write('\n')
    finally:
        f.close()

print 'dir'
os.mkdir('dir')

mkfile('dir/file.txt')
mkfile('dir/file1.txt')
mkfile('dir/file2.txt')
mkfile('dir/filea.txt')
mkfile('dir/fileb.txt')

print 'dir/subdir'
os.mkdir('dir/subdir')

mkfile('dir/subdir/subfile.txt')

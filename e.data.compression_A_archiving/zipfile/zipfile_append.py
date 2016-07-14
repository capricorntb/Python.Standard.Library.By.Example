#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Writing data to a new archive.
"""

from zipfile_infolist import print_info
import zipfile

print 'creating archive'
with zipfile.ZipFile('append.zip', mode='w') as zf:
    zf.write('README.txt')

print
print_info('append.zip')

print 'appending to the archive'
with zipfile.ZipFile('append.zip', mode='a') as zf:
    zf.write('README.txt', arcname='README2.txt')

print
print_info('append.zip')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Writing data to a new archive using an alternate name.
"""

from zipfile_infolist import print_info
import zipfile

with zipfile.ZipFile('write_arcname.zip', mode='w') as zf:
    zf.write('README.txt', arcname='NOT_README.txt')

print_info('write_arcname.zip')

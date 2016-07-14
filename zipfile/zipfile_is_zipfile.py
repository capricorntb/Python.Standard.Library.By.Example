#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test if a file is a zipfile.
"""

import zipfile

for filename in [ 'README.txt', 'example.zip', 
                  'bad_example.zip', 'notthere.zip' ]:
    print '%15s  %s' % (filename, zipfile.is_zipfile(filename))

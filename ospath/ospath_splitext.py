#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Separate a filename into the base and extension.
"""

__version__ = "$Id$"

import os.path

for path in [ 'filename.txt',
              'filename',
              '/path/to/filename.txt',
              '/',
              '',
              'my-archive.tar.gz',
              'no-extension.',
              ]:
    print '%21s :' % path, os.path.splitext(path)

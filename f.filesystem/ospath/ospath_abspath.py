#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Compute an absolute path from a relative path.
"""

__version__ = "$Id$"

import os
import os.path

os.chdir('/tmp')

for path in [ '.',
              '..',
              './one/two/three',
              '../one/two/three',
              ]:
    print '%17s : "%s"' % (path, os.path.abspath(path))

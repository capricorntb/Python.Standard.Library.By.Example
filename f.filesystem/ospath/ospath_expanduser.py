#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Expand tilde in filenames.
"""

__version__ = "$Id$"

import os.path

for user in [ '', 'dhellmann', 'postgresql' ]:
    lookup = '~' + user
    print '%12s : %s' % (lookup, os.path.expanduser(lookup))

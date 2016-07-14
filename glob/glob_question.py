#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example expansion of question mark wild card.

"""

__module_id__ = "$Id$"

import glob

for name in glob.glob('dir/file?.txt'):
    print name

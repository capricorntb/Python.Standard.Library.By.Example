#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The asterisk as wildcard character.

"""

__module_id__ = "$Id$"

import glob
for name in glob.glob('dir/*'):
    print name

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Differ example
"""

import difflib
from difflib_data import *

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print '\n'.join(diff)

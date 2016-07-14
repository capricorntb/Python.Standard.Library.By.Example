#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Context diff example
"""

import difflib
from difflib_data import *

diff = difflib.context_diff(text1_lines, text2_lines, lineterm='')
print '\n'.join(list(diff))

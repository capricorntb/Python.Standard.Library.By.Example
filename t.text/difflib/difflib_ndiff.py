#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ndiff example
"""

import difflib
from difflib_data import *

diff = difflib.ndiff(text1_lines, text2_lines)
print '\n'.join(list(diff))

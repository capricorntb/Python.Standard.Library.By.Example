#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unified diff example
"""

import difflib
from difflib_data import *

diff = difflib.unified_diff(text1_lines,
                            text2_lines,
                            lineterm='',
                            )
print '\n'.join(list(diff))

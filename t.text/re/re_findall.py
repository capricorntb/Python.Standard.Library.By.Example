#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Repetition of patterns
"""

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print 'Found "%s"' % match

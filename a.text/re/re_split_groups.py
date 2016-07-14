#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Splitting input based on a pattern.
"""

import re

text = '''Paragraph one
on two lines.

Paragraph two.


Paragraph three.'''

print 'With split:'
for num, para in enumerate(re.split(r'(\n{2,})', text)):
    print num, repr(para)
    print

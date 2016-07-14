#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Substitute based on patterns.
"""

import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**.  This **too**.'

print 'Text:', text
print 'Bold:', bold.sub(r'<b>\1</b>', text)

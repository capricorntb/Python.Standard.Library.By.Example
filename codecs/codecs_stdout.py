#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Printing unicode text to sys.stdout.
"""

import codecs
import sys

text = u'pi: π'

# Printing to stdout may cause an encoding error
print 'Default encoding:', sys.stdout.encoding
print 'TTY:', sys.stdout.isatty()
print text

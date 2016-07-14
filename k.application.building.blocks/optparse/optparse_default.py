#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using optparse with single-letter options.
"""

import optparse

parser = optparse.OptionParser()
parser.add_option('-o', action="store", default="default value")

options, args = parser.parse_args()

print options.o

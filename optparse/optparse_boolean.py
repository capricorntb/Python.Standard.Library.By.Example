#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Boolean flags.
"""

import optparse

parser = optparse.OptionParser()
parser.add_option('-t', action='store_true',
                  default=False, dest='flag')
parser.add_option('-f', action='store_false',
                  default=False, dest='flag')

options, args = parser.parse_args()

print 'Flag:', options.flag



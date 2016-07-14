#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Printing help with optparse.  

Call this script with --help on the command line.
"""

import optparse

parser = optparse.OptionParser()
parser.add_option('--no-foo', action="store_true", 
                  default=False, 
                  dest="foo",
                  help="Turn off foo",
                  )
parser.add_option('--with', action="store",
                  help="Include optional feature")

parser.parse_args()

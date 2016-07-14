#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using read when getpass won't work because we are not connected to a terminal.

"""

import getpass
import sys

if sys.stdin.isatty():
    p = getpass.getpass('Using getpass: ')
else:
    print 'Using readline'
    p = sys.stdin.readline().rstrip()

print 'Read: ', p

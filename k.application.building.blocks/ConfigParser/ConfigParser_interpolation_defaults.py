#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reading a configuration file.
"""

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('interpolation_defaults.ini')

print 'URL:', parser.get('bug_tracker', 'url')

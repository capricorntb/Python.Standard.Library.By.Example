#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Load pickles from a file
"""

try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO
import sys

filename = sys.argv[1]

with open(filename, 'rb') as in_s:
    # Read the data
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print 'READ: %s (%s)' % (o.name, o.name_backwards)

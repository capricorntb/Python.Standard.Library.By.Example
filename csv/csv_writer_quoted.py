#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example of writing a comma separated value file, using more quoting.

"""

import csv
import sys

with open(sys.argv[1], 'wt') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
    for i in range(3):
        writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )

print open(sys.argv[1], 'rt').read()

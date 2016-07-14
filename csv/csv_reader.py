#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example of reading a comma separated value file.
"""

import csv
import sys

with open(sys.argv[1], 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

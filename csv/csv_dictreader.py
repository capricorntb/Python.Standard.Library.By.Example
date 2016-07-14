#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dictionary reader.

"""

import csv
import sys

with open(sys.argv[1], 'rt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print row

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import itertools
import os

with gzip.open('example_lines.txt.gz', 'wb') as output:
    output.writelines(
        itertools.repeat('The same line, over and over.\n', 10)
        )

os.system('gzcat example_lines.txt.gz')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import os

outfilename = 'example.txt.gz'
with gzip.open(outfilename, 'wb') as output:
    output.write('Contents of the example file go here.\n')

print outfilename, 'contains', os.stat(outfilename).st_size, 'bytes'
os.system('file -b --mime %s' % outfilename)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zlib

input_data = 'Some repeated text.\n' * 1024

results = set()
for i in xrange(1, 10):
    data = zlib.compress(input_data, i)
    results.add(data)

print len(results)

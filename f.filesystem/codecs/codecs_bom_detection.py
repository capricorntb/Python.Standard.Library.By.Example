#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Detecting the BOM.
"""

import codecs
from codecs_to_hex import to_hex

# Look at the raw data
with open('nonnative-encoded.txt', mode='rb') as f:
    raw_bytes = f.read()

print 'Raw    :', to_hex(raw_bytes, 2)

# Re-open the file and let codecs detect the BOM
with codecs.open('nonnative-encoded.txt',
                 mode='rt',
                 encoding='utf-16',
                 ) as f:
    decoded_text = f.read()

print 'Decoded:', repr(decoded_text)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Files as context managers.
"""

with open('/tmp/pymotw.txt', 'wt') as f:
    f.write('contents go here')
# file is automatically closed



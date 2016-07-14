#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Square roots
"""

import math

print math.sqrt(9.0)
print math.sqrt(3)
try:
    print math.sqrt(-1)
except ValueError, err:
    print 'Cannot compute sqrt(-1):', err
    

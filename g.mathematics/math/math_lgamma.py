#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Natural logarithm of Gamma
"""

import math

for i in [ 0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 ]:
    try:
        print '{:2.1f}  {:.20f}  {:.20f}'.format(
            i,
            math.lgamma(i),
            math.log(math.gamma(i)),
            )
    except ValueError, err:
        print 'Error computing lgamma(%s):' % i, err


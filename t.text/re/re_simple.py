#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple pattern examples.
"""

import re

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

print 'Text: %r\n' % text

for pattern in patterns:
    print 'Seeking "%s" ->' % pattern, 

    if re.search(pattern,  text) is None:
        print 'no match'
    else:
        print 'match!'

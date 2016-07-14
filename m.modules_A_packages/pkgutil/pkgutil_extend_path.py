#!/usr/bin/env python
# -*- coding: utf-8 -*-

import demopkg1
print 'demopkg1           :', demopkg1.__file__

try:
    import demopkg1.shared
except Exception, err:
    print 'demopkg1.shared    : Not found (%s)' % err
else:
    print 'demopkg1.shared    :', demopkg1.shared.__file__

try:
    import demopkg1.not_shared
except Exception, err:
    print 'demopkg1.not_shared: Not found (%s)' % err
else:
    print 'demopkg1.not_shared:', demopkg1.not_shared.__file__

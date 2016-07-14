#!/usr/bin/env python
# -*- coding: utf-8 -*-

import anydbm

db = anydbm.open('/tmp/example.db', 'w')
try:
    db[1] = 'one'
except TypeError, err:
    print '%s: %s' % (err.__class__.__name__, err)
finally:
    db.close()

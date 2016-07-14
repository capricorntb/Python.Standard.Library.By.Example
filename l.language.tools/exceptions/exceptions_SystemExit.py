#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    sys.exit(1)
except SystemExit, err:
    print 'Tried to exit with code', err.code

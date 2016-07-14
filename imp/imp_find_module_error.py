#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imp

try:
    imp.find_module('no_such_module')
except ImportError, err:
    print 'ImportError:', err


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import sys

from traceback_example import produce_exception

try:
    produce_exception()
except Exception, err:
    print 'format_exc():'
    print traceback.format_exc()

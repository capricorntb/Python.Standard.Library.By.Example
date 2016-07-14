#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write('Some data')
    temp.seek(0)
    
    print temp.read()

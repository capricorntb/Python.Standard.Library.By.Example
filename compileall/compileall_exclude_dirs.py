#!/usr/bin/env python
# -*- coding: utf-8 -*-

import compileall
import re

compileall.compile_dir('examples', 
    rx=re.compile(r'/subdir'))

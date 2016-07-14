#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reading the names out of a ZIP archive.
"""

import zipfile

with zipfile.ZipFile('example.zip', 'r') as zf:
    print zf.namelist()

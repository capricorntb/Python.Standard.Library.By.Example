#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Print the table of contents of a ZIP archive
"""

import zipfile

with zipfile.ZipFile('example.zip', 'r') as zf:
    print zf.printdir()

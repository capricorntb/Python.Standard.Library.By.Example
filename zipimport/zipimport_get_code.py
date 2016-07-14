#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Retrieving the code for a module within a zip archive.
"""

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
code = importer.get_code('zipimport_get_code')
print code

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Retrieving the source code for a module within a zip archive.

"""

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
for module_name in ['zipimport_get_code', 'zipimport_get_source']:
    source = importer.get_source(module_name)
    print '=' * 80
    print module_name
    print '=' * 80
    print source
    print

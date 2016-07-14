#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Finding a module within a zip archive.

"""

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')

for module_name in [ 'zipimport_find_module', 'not_there' ]:
    print module_name, ':', importer.find_module(module_name)

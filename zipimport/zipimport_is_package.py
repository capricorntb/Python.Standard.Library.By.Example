#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Determine whether a module within a ZIP archive is a package or a regular module.

"""

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
for name in ['zipimport_is_package', 'example_package']:
    print name, importer.is_package(name)



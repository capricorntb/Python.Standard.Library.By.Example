#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Retrieving the code for a module within a zip archive.

"""

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
module = importer.load_module('zipimport_get_code')
print 'Name   :', module.__name__
print 'Loader :', module.__loader__
print 'Code   :', module.code



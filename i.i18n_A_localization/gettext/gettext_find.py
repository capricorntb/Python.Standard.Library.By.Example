#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gettext

catalogs = gettext.find('example', 'locale', all=True)
print 'Catalogs:', catalogs

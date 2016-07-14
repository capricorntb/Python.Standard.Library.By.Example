#!/usr/bin/env python
# -*- coding: utf-8 -*-

import locale

sample_locales = [ ('USA',      'en_US'),
                   ('France',   'fr_FR'),
                   ('Spain',    'es_ES'),
                   ('Portugal', 'pt_PT'),
                   ('Poland',   'pl_PL'),
                   ]

print '%20s %15s %20s' % ('Locale', 'Integer', 'Float')
for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)

    print '%20s' % name,
    print locale.format('%15d', 123456, grouping=True),
    print locale.format('%20.2f', 123456.78, grouping=True)

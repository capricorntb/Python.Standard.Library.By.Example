#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using getopt with longer option names.
"""

import getopt

opts, args = getopt.getopt([ '--noarg',
                             '--witharg', 'val',
                             '--witharg2=another',
                             ],
                           '',
                           [ 'noarg', 'witharg=', 'witharg2=' ])
for opt in opts:
    print opt
    

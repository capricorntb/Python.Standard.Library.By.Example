#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gettext import translation
import sys

t = translation('gettext_plural', 'locale', fallback=True)
num = int(sys.argv[1])
msg = t.ungettext('%(num)d means singular.',
                  '%(num)d means plural.',
                  num)

# Still need to add the values to the message ourself.
print msg % {'num':num}

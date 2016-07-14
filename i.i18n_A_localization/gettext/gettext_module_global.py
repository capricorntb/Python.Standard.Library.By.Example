#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gettext
t = gettext.translation('gettext_example', 'locale', fallback=True)
_ = t.ugettext
ngettext = t.ungettext

print _('This message is in the script.')

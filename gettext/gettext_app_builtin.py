#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gettext
gettext.install('gettext_example', 'locale',
                unicode=True, names=['ngettext'])

print _('This message is in the script.')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""All configuration variables.
"""

import sysconfig

print 'User base directory:', sysconfig.get_config_var('userbase')
print 'Unknown variable   :', sysconfig.get_config_var('NoSuchVariable')

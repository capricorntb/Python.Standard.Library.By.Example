#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using sys.stderr for the prompt lets us redirect stdout.

"""

import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print 'You entered:', p

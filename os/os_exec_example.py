#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using os.exec*().

"""

__module_id__ = "$Id$"

import os

child_pid = os.fork()
if child_pid:
    os.waitpid(child_pid, 0)
else:
    os.execlp('pwd', 'pwd', '-P')

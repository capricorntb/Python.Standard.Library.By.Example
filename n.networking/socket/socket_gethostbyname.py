#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convert hostname to IP address.
"""

import socket

for host in [ 'homer', 'www', 'www.python.org', 'nosuchname' ]:
    try:
        print '%s : %s' % (host, socket.gethostbyname(host))
    except socket.error, msg:
        print '%s : %s' % (host, msg)

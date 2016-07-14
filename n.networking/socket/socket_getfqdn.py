#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Look up the fully qualified domain name for a host.
"""

import socket

for host in [ 'homer', 'www' ]:
    print '%6s : %s' % (host, socket.getfqdn(host))

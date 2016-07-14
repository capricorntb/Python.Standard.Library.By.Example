#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
import imaplib_connect

c = imaplib_connect.open_connection()
try:
    c.select('INBOX', readonly=True)
    
    print 'BODY:'
    typ, msg_data = c.fetch('1', '(BODY.PEEK[TEXT])')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            print response_part[1]

finally:
    try:
        c.close()
    except:
        pass
    c.logout()

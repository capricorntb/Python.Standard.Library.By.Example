#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Cookie

c = Cookie.SimpleCookie()
c['mycookie'] = 'cookie_value'
c['another_cookie'] = 'second value'
print c.js_output()

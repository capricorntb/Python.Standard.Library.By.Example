#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sample of TextCalendar output.

"""

import calendar

c = calendar.HTMLCalendar(calendar.SUNDAY)
print c.formatmonth(2011, 7)

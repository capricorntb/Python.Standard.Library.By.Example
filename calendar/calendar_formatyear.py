#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Print entire year calendar.

"""

import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
print cal.formatyear(2011, 2, 1, 1, 3)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Query tasks in the database.
"""

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    # Change the row factory to use Row
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()

    cursor.execute("""
    select name, description, deadline from project
    where name = 'pymotw'
    """)
    name, description, deadline = cursor.fetchone()

    print 'Project details for %s (%s) due %s' % (
        description, name, deadline)

    cursor.execute("""
    select id, priority, status, deadline, details from task
    where project = 'pymotw' order by deadline
    """)

    print '\nNext 5 tasks:'
    for row in cursor.fetchmany(5):
        print '%2d {%d} %-25s [%-8s] (%s)' % (
            row['id'], row['priority'], row['details'],
            row['status'], row['deadline'],
            )

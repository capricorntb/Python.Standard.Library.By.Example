#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Creating and waiting for a process
"""

import multiprocessing
import multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
            target=multiprocessing_import_worker.worker,
            )
        jobs.append(p)
        p.start()

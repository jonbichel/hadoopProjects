#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None
tot_count = 0
for line in sys.stdin:
    line = line.rstrip()

    print line
    
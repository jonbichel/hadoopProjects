#!/usr/bin/env python
#mapper.py

import string
import sys
import random
count = 1

for line in sys.stdin:
    if count == 10:
        print line.strip()
        count = 1
    count += 1
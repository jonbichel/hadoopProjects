#!/usr/bin/env python
#mapper.py

import string
import sys
import random

for line in sys.stdin:
    if random.randint(1, 10) <= 1:
        print line.strip()

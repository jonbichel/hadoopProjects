#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None

for word in sys.stdin:
    word = line.rstrip()

    if prev_key == None:
        prev_key = word
        continue
    if prev_key == word:
        continue
    if prev_key != word:
        print prev_key
        prev_key = word

print prev_key

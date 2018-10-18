#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None
count = 0  # not used

for line in sys.stdin:
    line = line.rstrip()
    word, count = line.split('\t')

    if prev_key == None:
        prev_key = word
        continue
    if prev_key == word:
        continue
    if prev_key != word:
        print prev_key.replace(".", "")
        prev_key = word

print prev_key.replace(".", "")

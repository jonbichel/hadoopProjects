#!/usr/bin/env python
#reducer.py

import string
import sys

prev_words = None
tot_count = 0
tot_count_base = 0
for line in sys.stdin:
    line = line.rstrip()
    words, count = line.split('\t')
    word1, word2 = words.split(',')

    if prev_words == None:
        prev_words = words
        tot_count = int(count)
        continue
    if prev_words == words:
        tot_count = tot_count+int(count)
        continue

    # new word stop counting and emit
    if prev_words != words:
        # if we were counting base word emit base count
        if prev_words.split(',')[1] == '$':
            # print the base word total
            # print '%s\t%s' % (prev_words, tot_count)
            tot_count_base = tot_count
        # if we were counting a pair of words emit and reset the pair counter
        else:
            # print the total of the pair of words
            # print '%s\t%s' % (prev_words, tot_count)
            # print normalized value for each set of words
            print '%s\t%f' % (prev_words, float(tot_count)/float(tot_count_base))

        tot_count = int(count)
        prev_words = words

# send out last line
print '%s\t%s' % (prev_words, tot_count)
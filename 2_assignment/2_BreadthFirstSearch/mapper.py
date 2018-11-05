#!/usr/bin/env python
#mapper.py

import string
import sys

adj_list = []

for line in sys.stdin:
    line = line.strip()
    # line = line.lower()
    key, value = line.split()
    adj_list, distance, color, parent = value.split('|')
    if color == 'WHITE' or color == "BLACK":
        # send as is
        print(line)
    if color == 'GRAY':
        # print parent node
        print'%s\t%s|%s|%s|%s' % (key,adj_list,distance,'BLACK',parent)
        distance = int(distance) + 1
        # iterate through adjacency list
        for node in adj_list.split(','):
            # if node != None:
            print'%s\t%s|%s|GRAY|%s' % (node, None, distance, key)


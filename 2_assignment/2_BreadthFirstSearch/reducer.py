#!/usr/bin/env python
#reducer.py

import string
import sys

prev_node_gray = False
current_distance = sys.maxint

search_complete = True

for line in sys.stdin:
    line = line.strip()

    # split the node and node data
    key, value = line.split()

    # unpack node data
    adj_list, distance, color, parent = value.split('|')

    # if the node is black just send it again
    if color == 'BLACK':
        print line

    # if node is grey find grey node with shortest distance
    elif color == 'GRAY':
        #at least one grey node going to next round
        search_complete = False

        # multiple instances of this node # that are grey, shortest distance takes is kept
        if prev_node_gray == True:
            if distance < current_distance:
                current_distance = distance
                current_adj_list = adj_list
                current_parent = parent
        # no previous instance of this node number that is also grey
        else:
            current_distance = distance
            current_adj_list = adj_list
            current_parent = parent
            prev_node_gray = True

    elif color == 'WHITE':
        # if node is white check for any previously arrived grey nodes with the same node number and combine and emit
        if prev_node_gray == True:
            print'%s\t%s|%s|GRAY|%s' % (key, adj_list, current_distance, current_parent)
        # otherwise emit as is
        else:
            print(line)

        # set previous grey node to false
        prev_node_gray = False

if(search_complete):
    print('Search Complete')






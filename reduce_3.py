#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 3. Write a map-reduce program to compute the top 20 URLs tweeted 
# by the users.

#############################################################################
"""                   Reduce tweets from text file                     """

# to run in command prompt: python map_3.py < urls.txt | sort | python reduce_3.py

# reduce  portion
def wcount(prev_key,counts):
    if prev_key is not None:
        print prev_key + ' count is ' + str(counts)
        
prev_key = None
counts = 0

for line in sys.stdin:
    key, value = line.split('\t',1)
    if key != prev_key:
        wcount(prev_key, counts)
        prev_key = key
        counts = 0
    counts += eval(value)

wcount(prev_key, counts)
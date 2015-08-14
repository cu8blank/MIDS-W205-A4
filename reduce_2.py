#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 2. Write a map-reduce program to compute the tweet volume on 
# an hourly basis (i.e., number of tweets per hour).

#############################################################################
"""                   Reduce tweets from text file                     """

# to run in command prompt: python map_2.py < time.txt | sort | python reduce_2.py

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
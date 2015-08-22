#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 1. Write a map-reduce program that counts the number of words 
# with more than 10000 occurrences.

#############################################################################
"""                   Reduce tweets from text file                     """

# to run in command prompt: python map_1.py < tweet_text.txt | sort | python reduce_1.py

# reduce  portion
def wcount(prev_key,counts):
    if prev_key is not None:
        #print prev_key + ' count is ' + str(counts)
        if counts > 10000:             # only prints out words that occur more than 10,000 times
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
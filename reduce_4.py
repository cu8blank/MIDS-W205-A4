#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 4. Write a map-reduce program that for each word in the tweets' 
#  text, computes the occurrences of other words appear in every tweet that it appeared.
#  For example, assume that we have the following text as a tweet text..

#############################################################################
"""                   Reduce tweets from text file                     """

# to run in command prompt: python map_4.py < tweet_text.txt | sort | python reduce_4.py

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
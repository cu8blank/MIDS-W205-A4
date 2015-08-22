#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 3. Write a map-reduce program to compute the top 20 URLs tweeted 
# by the users.

#############################################################################
"""                    Map tweets from text file                        """

# to run in command prompt: python map_3.py < urls.txt | sort

# map portion
for line in sys.stdin:
    url = line.split()
    print url[0] +'\t'+str(1)
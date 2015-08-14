#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 2. Write a map-reduce program to compute the tweet volume on 
# an hourly basis (i.e., number of tweets per hour).

#############################################################################
"""                    Map tweets from text file                        """

# to run in command prompt: python map_2.py < time.txt | sort

# map portion
for line in sys.stdin:
    words=line.split(" ")
    date1 = words[0]
    time1 = words[1]
    time1pieces = time1.split(':')
    hour1 = time1pieces[0]
    
    date_hour = date1 + '_' + hour1
    
    print date_hour + '\t'+str(1)
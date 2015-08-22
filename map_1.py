#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 1. Write a map-reduce program that counts the number of words 
# with more than 10000 occurrences.

#############################################################################
"""                    Map tweets from text file                        """

# to run in command prompt: python map_1.py < tweet_text.txt | sort

char_count = 0
total_tweets = 124130
#country_hashtag = ['AUS','CHN','JPN','KOR','THA','CMR','CIV','NGA','CAN','CRC','MEX','USA','BRA','COL','ECU','NZL','ENG','FRA','GER','NED','NOR','ESP','SWE','SUI']
country_hashtag = ['aus','chn','jpn','kor','tha','cmr','civ','nga','can','crc','mex','usa','bra','col','ecu','nzl','eng','fra','ger','ned','nor','esp','swe','sui']

for line in sys.stdin:
    words=line.split(",")
    for word in words:
        words1=word.split()
        for word2 in words1:
            #char_count += len(str(word2))
            #average_char = char_count / total_tweets
            #print word2+'\t'+str(1)+'\t'+ str(average_char)   #### modification to answer Question #1 (run with no sorting)
            #word2 = word2.lower()
            #if word2 in country_hashtag:  #### modification to answer Question #2 (run with sorting)
            #    print word2+'\t'+str(1)                  
            print word2+'\t'+str(1)
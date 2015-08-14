#!/usr/bin/env python

import sys

#W205.3 - Al Byun
#Assignment 4
#Analysis Program 4. Write a map-reduce program that for each word in the tweets' 
#  text, computes the occurrences of other words appear in every tweet that it appeared.
#  For example, assume that we have the following text as a tweet text..

#############################################################################
"""                    Map tweets from text file                        """

# to run in command prompt: python map_4.py < tweet_text.txt | sort

# map portion
for line in sys.stdin:
    bag_o_words = []
    words=line.split(",")
    for word in words:
        total_words = word.split()
        for word2 in total_words:
            bag_o_words.append(word2)  ## parse tweet to find word corpus
            
    for word in bag_o_words:
        temp_bag = bag_o_words
        temp_bag.remove(word)
        for word1 in temp_bag:
            word_cat = ''
            word_cat = word + '---' + word1
            print word_cat +'\t'+str(1)  ## pair each word with another word in tweet
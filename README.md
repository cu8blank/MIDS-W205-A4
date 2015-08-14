# MIDS-W205-A4


W205.3 - Al Byun
MIDS-W205-A4 - Assignment 4

_______________________________________________________________

Section 1) Data Collection - Using Scrapy

"Write an acquisition program that can acquire the tweets between June 6th and July 5th of 2015 for the official FIFA Women World Cup hashtag (“#FIFAWWC”), as well as team code hashtags (e.g. “#USA” and “#GER”) and store them with appropriate structures in WC2015.csv on S3. You can find more information about teams here and the hashtags here. WC2015.csv will be used in the following tasks.

There is no hard requirement for the amount of tweets that you should gather. However, you should gather reasonable amount of tweets to be able to perform the analysis part. Note that you need to gather the historical data for which you need to design a strategy and use techniques such as web scrapping for the specified time frame (June 6th and July 5th of 2015)."

Deliverable:
Code - task1_acquire_for_submission.py
Data - WC2015.csv

Strategy:
1. Use Twitter Advanced Search website and identified two base URLs.
The first search URL was for all tweets between June 6 and July 5, 2015 that contained: #FIFAWWC AND (one of the Women's World Cup country three letter hashtags).
The second search URL was for all tweets between June 6 and July 5, 2015 that contained: #FIFAWWC.

2. Inspecting the Twitter webpage's XMLHttpRequest (XHR) revealed that the max_pos/min_pos updated for every 20 tweets on the results page.
Therefore, the script cycled through 6,250 results pages, with 20 results per page, to retrieve approximately 125,000 tweets.

3. As the tweets were scrapped from the webpage, data was parsed into separate fields.
The Scrapy class, FifawwcItem, stored data into the following fields:
	- tweet_text = Field() - text from tweet
	- url = Field() - text of url if any were listed in tweet
	- user_name = Field() - user_name of tweet author   
	- date_time = Field() - date and time of tweet    
	- hashtags = Field() - text of any hashtags referenced in tweet    
	- strong_hashtags = Field() - text of any hashtags that were bolded and matched the original search parameters

4. These fields were stored into columns of the WC2015.csv file.
The WC2015.csv file was then uploaded into an S3 bucket.




_______________________________________________________________

Section 2) Analysis Programs

Task 1. Write a map-reduce program that counts the number of words with more than 10000 occurrences.

Deliverable:
Code - map_1.py, reduce_1.py
Data - tweet_text.txt

Strategy:
1. The tweet text was extracted from the WC2015.csv file and placed into a text file.

2. The mapper script iterated through each line and parsed out each word.
The script then printed out each word with a count of 1.
This script was modified to count the number of characters and then find the average number of characters per tweet to answer Question 1.
This script was also modified to display the number of country hashtags and find the number of support messages (occurrences) for each to answer Question 2.
The mapper script was run and the results were sorted.

3. The reducer script took the sorted results of the mapper script and aggregated the number of occurrences of each to compute the word count.
If the count was greater than 10,000, then the word was printed.

4. The number of words with more than 10,000 occurrences were:
	- CAN count is 11521	
	- FIFAWWC count is 124246	
	- USA count is 32284	
	- and count is 14303	
	- in count is 25376	
	- the count is 53821	
	- ENG count is 26318	
	- a count is 24101	
	- GER count is 20896	
	- at count is 18985	
	- of count is 15674
	- on count is 23780	
	- is count is 12785	
	- for count is 20022	
	- to count is 36270



Task 2. Write a map-reduce program to compute the tweet volume on an hourly basis (i.e., number of tweets per hour)

Deliverable:
Code - map_2.py, reduce_2.py
Data - time.txt

Strategy:
1. The date and time for each tweet in the WC2015.csv file was extracted and placed into a text file.

2. The mapper script parsed out the date and the time in hours from each tweet.
The script then printed each date and hours combo with a count of 1.
The mapper script was run and the results were sorted.

3. The reducer script took the sorted results of the mapper script and aggregated the number of occurrences of each to compute the word count.

4. Sample of results include:
	- 6/13/2015_19 count is 33	
	- 6/13/2015_7 count is 58	
	- 6/14/2015_13 count is 18	
	- 6/14/2015_2 count is 13	
	- 6/14/2015_20 count is 13	
	- 6/14/2015_9 count is 30	
	- 6/15/2015_16 count is 557	



Task 3. Write a map-reduce program to compute the top 20 URLs tweeted by the users

Deliverable:
Code - map_3.py, reduce_3.py
Data - urls.txt

Strategy:
1. The urls present in tweets stored in the WC2015.csv file were extracted and placed into a text file.

2. The mapper script printed each url with a count of 1.
The mapper script was run and the results were sorted.

3. The reducer script took the sorted results of the mapper script and aggregated the number of occurrences of each to compute the word count.

4. The top 20 URLs tweeted by the users were:

	- http://totalsoccerproject.com/2015/07/photos-womens-world-cup-germany-vs-england/	1339
	- https://twitter.com/england/status/617460763490394112	1251
	- https://instagram.com/p/4u8eQUJc57/	1250
	- http://ift.tt/1BogwgX	492
	- http://WWW.FIFANEWS.CA	406
	- http://fifa.to/1H5ieWa	94
	- http://www.voxstadium.fr/football/canada-2015-le-podium-pour-langleterre-50581/	89
	- https://goo.gl/ksK82F	58
	- http://soccer-aloud.com	52
	- http://bbc.in/1mbSmuT	49
	- http://bit.ly/1JZZedN	41
	- http://bbc.in/1MzvS5F	35
	- http://bit.ly/1J9juJB	33
	- http://fifa.to/1eMW81u	28
	- http://fifa.to/1Kpov2F	27
	- http://the-local.com/sports/	25
	- http://bbc.in/1Jol6B7	23
	- http://bbc.in/1KnMXjj	20
	- http://www.lameta.com	19
	- http://bbc.in/1NtaSxJ	18




Task 4. Write a map-reduce program that for each word in the tweets' text, computes the occurrences of other words appear in every tweet that it appeared. 

Deliverable:
Code - map_4.py, reduce_4.py
Data - urls.txt

Strategy:
1. The tweet text was extracted from the WC2015.csv file and placed into a text file.

2. The mapper script iterated through each line and parsed out each word to create a corpus for each tweet.
The script then paired each word with each other word in the corpus.
The script then printed out the pair with a count of 1.
The mapper script was run and the results were sorted.

3. The reducer script took the sorted results of the mapper script and aggregated the number of occurrences of each pair of words to compute and to print the count.

4. Sample of results include:
	- all---me count is 10	
	- all---meet count is 3	
	- all---meetings count is 1	
	- all---mid count is 1	
	- all---might count is 3	
	- all---minute count is 2	
	- all---miss count is 1	
	- all---monster count is 2	



Task Questions. Using/modifying the above programs, answer the following questions:

1. What is the average length of tweets (in number of characters) in WC2015.csv?
The average length  of tweets in WC2015.csv is 74 characters.
This was calulated using a modified map_1.py script.

2. Draw a table with all the team support hashtags you can find and the number of support messages. What country did get apparently the most support?.
The results from running the modified map_1.py script show that USA has the most support.
	- aus count is 7508
	- bra count is 4057
	- can count is 16092
	- chn count is 4124
	- civ count is 2910
	- cmr count is 2392
	- col count is 5136
	- crc count is 2152
	- ecu count is 1549
	- eng count is 30057
	- esp count is 3024
	- fra count is 8462
	- ger count is 22121
	- jpn count is 9968
	- kor count is 2797
	- mex count is 3134
	- ned count is 3521
	- nga count is 2921
	- nor count is 4160
	- nzl count is 1943
	- sui count is 3123
	- swe count is 4540
	- tha count is 2306
	- usa count is 33325

3. How many times the word USA occur with the word Japan?
The results were found using the MapReduce in Task #4.
usa---japan and japan---usa count is 208

4. How many times the word champion occur with the word USA?
The results were found using the MapReduce in Task #4.
usa---champion and champion---usa count is 7
However, USA is also paired with similar words, like champions and championship.




_______________________________________________________________

Section 3) Twitter Archive Search

Deliverable:
Code - whoosh_task_for_submission.py
Data - WC2015.csv, hw4-whoosh-index directory

1. Write a python program that uses whoosh to index the archive (WC2015.csv) based on various fields. The fields are part of your design decisions.

Strategy:
1. The schema for the whoosh index directory matches the structure of the WC2015.csv.
The fields included in the whoosh index directory are:
	- id = ID(unique=True, stored=True)
	- url = TEXT(stored=True) 
	- strong_hashtags = TEXT(stored=True)
	- hashtags = TEXT(stored=True)
	- user_name = TEXT(stored=True)
	- date_time = TEXT(stored=True)
	- tweet_text = TEXT(stored=True)


2. Write a python program that takes queries (you need to design the supported queries) and search through the indexed archive using whoosh. Your program should handle at least 4 queries ( of your choice) similar to the sample query.

Strategy: This script runs through 5 different queries

Query 1. Player name search, ex. Tobin Heath
Result:
('# of hits:', 67)
('Best Match:', <Hit {'date_time': u'6/16/2015 15:57', 'strong_hashtags': u'USA,FIFAWWC', 'url': u'', 'hashtags': u'USAvNIG,WomensWorldCup,TeamUSA', 'tweet_text': u'Put Tobin Heath in!!!!!!!!!! , , , , , , ', 'user_name': u'/BriaQuesadilla', 'id': u'55703'}>)


Query 2. Player name search, ex. Alex Morgan
Result:
('# of hits:', 357)
('Best Match:', <Hit {'date_time': u'6/6/2015 17:59', 'strong_hashtags': u'FIFAWWC,USA', 'url': u'', 'hashtags': u'', 'tweet_text': u"I'm hype for the , for Alex Morgan and Alex Morgan only. ", 'user_name': u'/NCabreraaa', 'id': u'94255'}>)


Query 3. Key word search, ex. USA and JPN
Result:
('# of hits:', 1602)
('Best Match:', <Hit {'date_time': u'7/1/2015 17:57', 'strong_hashtags': u'JPN,USA,JPN,FIFAWWC,USA,USA', 'url': u'', 'hashtags': u'', 'tweet_text': u'So , and the , meet again in a final. , won , in 2011; , Olympic gold in London 2012. , favourites for me...', 'user_name': u'/SimonFudge74', 'id': u'4734'}>)


Query 4. Retweets with key word search, ex. RTs with USA
Result:
('# of hits:', 36)
('Best Match:', <Hit {'date_time': u'6/30/2015 15:00', 'strong_hashtags': u'FIFAWWC,USA', 'url': u'', 'hashtags': u'WWC,USWNT,onenationoneteam', 'tweet_text': u'RT to support TEAM USA! , ,  , , , ', 'user_name': u'/PSEGdelivers', 'id': u'16602'}>)


Query 5. Key word search, ex. score
Result:
query = Or([Term("strong_hastags","FIFAWWC"),Term("tweet_text","score")])
results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])



_______________________________________________________________

Section 4) Deliverables

1. A link to your collected tweets and the index directory created by whoosh on S3.
	- S3 link:
	- https://s3.amazonaws.com/w205_assignment4/
	- https://s3.amazonaws.com/w205_assignment4/WC2015.csv
	- https://s3.amazonaws.com/w205_assignment4/hw4-whoosh-index-dir
	- https://s3.amazonaws.com/w205_assignment4/hw4-whoosh-index-dir/MAIN_hgqw960hf3si9di4.seg
	- https://console.aws.amazon.com/s3/home?region=us-west-2&bucket=w205_assignment4&prefix=


2. Your source codes. Make sure you follow the assignment submission guidelines.
	- Source code uploaded to Github repository


3. You should answer to each of the questions in the architecture design file. You also need to explain how you used map-reduce to obtain the data you needed in each case as well as how the overall index/search structure is designed and describe the supported keyword search queries.
	- Question answers and architecture design explanation included in this README file.

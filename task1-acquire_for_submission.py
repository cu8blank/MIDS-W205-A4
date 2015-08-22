#W205.3 - Al Byun
#Assignment 4
#1. Write an acquisition program to pull the tweets for each hashtag and the tweets 
# that have both of the hashtags simultaneously with in a week. You also need to chunk 
# your data (using your design decisions) and give yourself the ability to re-run the 
# process reliable in case of failures (Resiliency).
#2. Organize the resulting raw data into a set of tweets and store these tweets into S3.

#############################################################################
"""                  Using Scrapy to retrieve tweets                      """

# to run in command prompt: scrapy crawl fifawwc -o WC2015.csv -t csv

from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from fifawwc.items import FifawwcItem

import urllib2
import json
import time

class MySpider(Spider):
    name = "fifawwc"
    allowed_domains = ["twitter.com"]   
    
    ##URLs with #FIFAWWC and a country hashtag 
    #web_url = "https://twitter.com/search?q=%23FIFAWWC%20%23AUS%20OR%20%23CHN%20OR%20%23JPN%20OR%20%23KOR%20OR%20%23THA%20OR%20%23CMR%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CAN%20OR%20%23CRC%20OR%20%23MEX%20OR%20%23USA%20OR%20%23BRA%20OR%20%23COL%20OR%20%23ECU%20OR%20%23NZL%20OR%20%23ENG%20OR%20%23FRA%20OR%20%23GER%20OR%20%23NED%20OR%20%23NOR%20OR%20%23ESP%20OR%20%23SWE%20OR%20%23SUI%20since%3A2015-06-06%20until%3A2015-07-05&src=typd&lang=en&max_position="
    #base_url = "https://twitter.com/i/search/timeline?q=%23FIFAWWC%20%23AUS%20OR%20%23CHN%20OR%20%23JPN%20OR%20%23KOR%20OR%20%23THA%20OR%20%23CMR%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CAN%20OR%20%23CRC%20OR%20%23MEX%20OR%20%23USA%20OR%20%23BRA%20OR%20%23COL%20OR%20%23ECU%20OR%20%23NZL%20OR%20%23ENG%20OR%20%23FRA%20OR%20%23GER%20OR%20%23NED%20OR%20%23NOR%20OR%20%23ESP%20OR%20%23SWE%20OR%20%23SUI%20since%3A2015-06-06%20until%3A2015-07-05&src=typd&vertical=default&include_available_features=1&include_entities=1&lang=en&last_note_ts=1432003055&max_position="
    #max_pos = "TWEET-617479430449971204-617483007482593281-BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    
    #URLs with just #FIFAWWC
    web_url = "https://twitter.com/search?q=%23FIFAWWC%20since%3A2015-06-06%20until%3A2015-07-05&src=typd&lang=en"
    base_url = "https://twitter.com/i/search/timeline?vertical=default&q=%23FIFAWWC%20since%3A2015-06-06%20until%3A2015-07-05&src=typd&include_available_features=1&include_entities=1&lang=en&last_note_ts=1432003070&max_position="
    max_pos = "TWEET-617481299293544448-617483016328228864-BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    
    scrape_urls = []    
    max_runs = 1250   #100,000 tweets total / 20 tweets per page = 5000  // #25,000 tweets / 20 = 1250
    for i in range(0,max_runs):
        scrape_target_url = web_url + max_pos
        scrape_urls.append(scrape_target_url)
        
        target_url = base_url + max_pos
        txt = urllib2.urlopen(target_url).read()
        json_data = json.loads(txt)
        max_pos = json_data['min_position']
        time.sleep(5)  #GET search/tweets limit 180 requests per 15 minutes (15*60/180 = 5 seconds)

    start_urls = scrape_urls
     
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        tweets = hxs.select("//div[@class='content']")
        items = []
        time.sleep(5)  #GET search/tweets limit 180 requests per 15 minutes (15*60/180 = 5 seconds)
      	for tweet in tweets:
      	    item = FifawwcItem()
            item["tweet_text"] = tweet.select("p/text()").extract()
            item["url"] = tweet.select("p/a/@data-expanded-url").extract()
            item["user_name"] = tweet.select("div[@class='stream-item-header']/a/@href").extract()
            item["date_time"] = tweet.select("div[@class='stream-item-header']/small/a/@title").extract()
            item["strong_hashtags"] = tweet.select("p/a/b/strong/text()").extract()
            item["hashtags"] = tweet.select("p/a/b/text()").extract()
            items.append(item)
      	return items


#############################################################################
"""                 Upload WC2015.csv file to S3 bucket                   """
# version to upload to Github will have AWS keys removed
AWS_KEY = ''
AWS_SECRET = ''

from boto.s3.connection import S3Connection
conn = S3Connection(AWS_KEY, AWS_SECRET)    
bucket = conn.create_bucket('w205_assignment4')

from boto.s3.key import Key

file_path = "C:\\Users\\Albert\\desktop\\github\\Assignment4\\WC2015.csv"
myKey = Key(bucket)
myKey.key = file_path
myKey.set_contents_from_filename(file_path)
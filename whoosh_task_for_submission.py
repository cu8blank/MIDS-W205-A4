#W205.3 - Al Byun
#Assignment 4
#Twitter Archive Search. Using Whoosh API to index the tweets in the dataset to 
# answer some standard queries.

# coding: utf-8

#############################################################################
"""                     Set up Whoosh for indexing                       """

# Write a python program that uses whoosh to index the archive (WC2015.csv) based 
# on various fields. The fields are part of your design decisions.

import os
import csv

from whoosh.fields import Schema, ID, TEXT
from whoosh.index import create_in, open_dir

my_schema = Schema(id = ID(unique=True, stored=True),
                    url = TEXT(stored=True), 
                    strong_hashtags = TEXT(stored=True),
                    hashtags = TEXT(stored=True),
                    user_name = TEXT(stored=True),
                    date_time = TEXT(stored=True),
                    tweet_text = TEXT(stored=True))
                    
if not os.path.exists("hw4_whoosh-index-dir"):
    os.mkdir("hw4-whoosh-index-dir")
    index = create_in("hw4-whoosh-index-dir", my_schema)

index = open_dir("hw4-whoosh-index-dir")

writer = index.writer()

f = open('WC2015.csv')
csv_f = csv.reader(f)

i=1
for row in csv_f: 
    tweet_data = [row[5]]
    writer.add_document(id = unicode(str(i),'utf-8'),
                        url = unicode(row[2],'utf-8'), 
                        strong_hashtags = unicode(row[1],'utf-8'),
                        hashtags = unicode(row[3],'utf-8'),
                        user_name = unicode(row[4],'utf-8'),
                        date_time = unicode(row[0],'utf-8'),
                        tweet_text = unicode(tweet_data[0],'utf-8'))
    i += 1
###

writer.commit()


#############################################################################
"""            Perform queries on Whoosh indexed data                    """

# Write a python program that takes queries (you need to design the supported queries) 
# and search through the indexed archive using whoosh. A sample query to the program 
# can be: RT:yes, keywords returns all the retweets that are related to the keywords. 
# Your program should handle at least 4 queries ( of your choice) similar to the sample query.

from whoosh.query import Term, And, Or
from whoosh.qparser import QueryParser
searcher = index.searcher()

parser = QueryParser("strong_hashtags", index.schema)
parser.parse("FIFAWWC USA JPN")


# Query 1: Player search
query = And([Term("tweet_text","tobin"),Term("tweet_text","heath")])
results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])

# Query 2: Player search
query = And([Term("tweet_text","alex"),Term("tweet_text","morgan")])
results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])

# Query 3: USA JPN 
parser = QueryParser("strong_hashtags", index.schema)
query = parser.parse("USA JPN")
results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])

# Query 4: RTs about USA
parser = QueryParser("tweet_text", index.schema)
query = parser.parse("RT USA")
results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])

# Query 5: score 
query = Or([Term("strong_hastags","FIFAWWC"),Term("tweet_text","score")])
results = searcher.search(query)
print('# of hits:', len(results))
print('Best Match:', results[0])


#############################################################################
"""            Upload Whoosh index directory to S3 bucket                 """

# version to upload to Github will have AWS keys removed
AWS_KEY = ''
AWS_SECRET = ''

from boto.s3.connection import S3Connection
conn = S3Connection(AWS_KEY, AWS_SECRET)    
bucket = conn.create_bucket('w205_assignment4')

from boto.s3.key import Key

file_path = "C:\\Users\\Albert\\desktop\\github\\Assignment4\\hw4-whoosh-index-dir"
for file in os.listdir(file_path):
    myKey = Key(bucket)
    myKey.key = file
    myKey.set_contents_from_filename('hw4-whoosh-index-dir'+'\\'+file)
    myKey.make_public()
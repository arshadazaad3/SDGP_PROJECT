from pytrends.request import TrendReq
import pandas as pd
import tweepy
import datetime
from datetime import date

# Authentication to twitter
auth = tweepy.OAuthHandler("OVTdS84lJEILeeldhGCUZYNqg", "6QRG9zAdezggILyzPcKH2wzpSHqmpsKSlNXTTPMADrGVQ6lKLr")
auth.set_access_token("405223959-hQfJbDlma2vxkF1YKVvOjFDhJPTIdLnxoNkmiipk",
                      "d18NNIPXQ3yixNB6j0bgaJ6ib6aAz8oHcP0TfmmABfbzn")

api = tweepy.API(auth)

# access google trends api
pytrend = TrendReq()

keywordToSearch = "corona"  # python keyword
user_keyword_list = [keywordToSearch]

# create timeframe from current date to 1 year ago
numdays = 7
numweeks = 52
numyears = 1
total_time_range = numdays * numweeks * numyears

end_date = date.today()
today_date = date.today()
begin_date = end_date - datetime.timedelta(days=total_time_range - 7)
user_timeframe = begin_date.strftime('%Y-%m-%d') + ' ' + end_date.strftime('%Y-%m-%d')

pytrend.build_payload(kw_list=user_keyword_list, cat=0, timeframe=user_timeframe, geo='')

# get related queries
related_queries_dict = pytrend.related_queries()

topValues = related_queries_dict[keywordToSearch]['top']
risingValues = related_queries_dict[keywordToSearch]['rising']

# filter out only 5 values from each queries
topValues = topValues.head(5)
risingValues = risingValues.head(5)

print(topValues)
print(risingValues)

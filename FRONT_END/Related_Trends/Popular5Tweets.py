import tweepy
import re

keyword = 'corona'

# Authentication to twitter
auth = tweepy.OAuthHandler("OVTdS84lJEILeeldhGCUZYNqg", "6QRG9zAdezggILyzPcKH2wzpSHqmpsKSlNXTTPMADrGVQ6lKLr")
auth.set_access_token("405223959-hQfJbDlma2vxkF1YKVvOjFDhJPTIdLnxoNkmiipk",
                      "d18NNIPXQ3yixNB6j0bgaJ6ib6aAz8oHcP0TfmmABfbzn")

api = tweepy.API(auth)

# for tweet in tweepy.Cursor(api.search, q=keyword, result_type='popular').items(5):
#     print(tweet.text)

tweets = tweepy.Cursor(api.search, q=keyword, result_type='popular').items(5)

# for tweet1 in tweets:
#     print (tweet1.text)

myfile = open('popular5.txt', 'w', encoding='utf-8')

for tweet1 in tweets:
    var = tweet1.text
    var = re.sub(r'https\S+', '', var)
    var.encode('ascii', 'ignore').decode('ascii')

    print (var)
    myfile.write("%s\n" % var)

myfile.close()

import tweepy
import re

# Authentication to twitter
auth = tweepy.OAuthHandler("OVTdS84lJEILeeldhGCUZYNqg", "6QRG9zAdezggILyzPcKH2wzpSHqmpsKSlNXTTPMADrGVQ6lKLr")
auth.set_access_token("405223959-hQfJbDlma2vxkF1YKVvOjFDhJPTIdLnxoNkmiipk",
                      "d18NNIPXQ3yixNB6j0bgaJ6ib6aAz8oHcP0TfmmABfbzn")

api = tweepy.API(auth)

# test authentication
userID = "bbcnews"

tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts=False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode='extended'
                           )

try:
    myfile = open('tweets.txt', 'w')

    for info in tweets[:100]:
        var = info.full_text
        myfile.write("%s\n" % var)
except:
    print("Char Error, Just ignore")
finally:
    myfile.close()
    myfile.close()



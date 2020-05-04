
#TOP 5 TWEETS

#returns the tweet of the given index
def get_tweet_from_index(index,dataframe):
    return dataframe[dataframe.index == index]["Text"].values[0]


def getTopTweets(data):
    # Create count matrix of the target column
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data["Text"])

    # Compute cosine similarity based on count_matrix
    cosine_sim = cosine_similarity(count_matrix)

    search_phrase_index = 0 #Target phrase

    # get similar ratio matrix
    similar_tweets = list(enumerate(cosine_sim[search_phrase_index]))
        # list -> [(0,0.998),(1,0.267),(2,0.777)......

    # Get a list of similar tweets in descending order of similarity score
    sorted_similar_tweets= sorted(similar_tweets, key=lambda x: x[1], reverse=True)
        # list -> [(0,0.998),(5,0.867),(2,0.777)......

    results = [] # to store top 5 tweets
    if (len(sorted_similar_tweets) > 6):
        num = 6
    else:
        num = len(sorted_similar_tweets)
    for i in range(1,num):
        tweet = sorted_similar_tweets[i]
        tweet = tweet[0]
        results.append(get_tweet_from_index(tweet,data))
    return results

# store top tweet in the Database
def store_top_tweet(category, user_phrase, toptweet):
    mydb = client[category]
    mycol = mydb["TopTweet"]

    #get the last index stored on the database
    prev = mycol.find_one({}, sort=[('_id', pymongo.DESCENDING)])
    latest_index = prev['index']

    #create the dict & insert to database
    result = {"index": latest_index + 1, "hashtag":user_phrase , "tweet": toptweet}
    mycol.insert_one(result)

# TOP TWEET RECOMMENDER MAIN CODE
def runTopTweet(user_phrase,category):
    #access database get All tweets
    mydb = client[user_phrase]
    mycol = mydb["Tweets"]
    df = pd.DataFrame(mycol.find())

    similarsearches_col = mydb["similarsearches"]
    similarsearches_df = pd.DataFrame(similarsearches_col.find())

    # to store all similar phrases
    allSimilarPhrases = ""
    for i in similarsearches_df["title"]:
        allSimilarPhrases += i+ " "

    target = {"index": 0, "text": allSimilarPhrases}
    df = df.append(target,ignore_index=True)

    top5tweets = getTopTweets(df) #get top 5 tweets

    store_top_tweet(category,user_phrase,top5tweets[0]) # store top tweet in the database under relevant category

    # store top 5 tweets in the database
    mycol = client[user_phrase]
    col = mycol["topfivetweets"]

    for x in range(1,len(top5tweets)+1):
        result = {"index": x, "tweet": top5tweets[x-1]}
        col.insert_one(result)


runTopTweet(keywordToSearch,category)

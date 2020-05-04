
#get the index of the given hashtag
def get_index_from_hashtag(hashtag,dataframe):
    return dataframe[dataframe.hashtag == hashtag]["index"].values[0]

#get hastag of the given index
def get_hashtag_from_index(index,dataframe):
    return dataframe[dataframe.index == index]["hashtag"].values[0]

# Create a column in DF which combines all target phrases
def combine_features(row):
    return row['hashtag'] + " " + row['tweet']

def getTopHashtag(dataframe, target_hashtag):

    dataframe["combined_features"] = dataframe.apply(combine_features, axis=1)

    # Create count matrix from this new combined column
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(dataframe["combined_features"])

    # Compute cosine similarity based on count_matrix
    cosine_sim = cosine_similarity(count_matrix)

    # Get Index of user Entered phrase
    hashtag_index = get_index_from_hashtag(target_hashtag,dataframe)

    # get similar ratio matrix
    similar_hashtags = list(enumerate(cosine_sim[hashtag_index]))

    # Get a list of similar hastags in descending order of similarity score
    sorted_similar_hashtags = sorted(similar_hashtags, key=lambda x: x[1], reverse=True)

    # store top 5 hastags in an array
    results = []
    if(len(sorted_similar_hashtags) >6):
        num = 6
    else:
        num = len(sorted_similar_hashtags)
    for i in range(0,num-1):
        tweet = sorted_similar_hashtags[i+1]
        results.append(get_hashtag_from_index(tweet[0],dataframe))
    return results

# TOP HASHTAG RECOMMENDER MAIN CODE
def runTopHashtag(category, target_Hashtag):
    #access database to get top tweets of the target category
    mydb = client[category]
    mycol = mydb["TopTweet"]
    df = mycol.find()
    df = pd.DataFrame(df)

    top5Hashtags =getTopHashtag(df,target_Hashtag) # get top 5 hashtags

    #store top 5 hastags in the database
    mycol = client[target_Hashtag]
    col = mycol["topfivehashtags"]
    for x in range(1, len(top5Hashtags)+1):
        result = {"index": x, "tweet": top5Hashtags[x - 1]}
        col.insert_one(result)

runTopHashtag(category,keywordToSearch)

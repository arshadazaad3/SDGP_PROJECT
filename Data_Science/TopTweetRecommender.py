from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Step 1: Read CSV file
df = pd.DataFrame(pd.read_excel('EnvironmentTweets.xlsx'))
df_selected = df.iloc[2:]


# def get_index_from_tweet(tweet):
#     return df[df.data == tweet]["index"].values[0]

def get_tweet_from_index(index):
    return df_selected[df_selected.index == index]["data"].values[0]


def getRecommendation():
    print(df_selected)

    # Step 4: Create count matrix from this new combined column
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df_selected["data"])

    # Step 5: Compute cosine similarity based on count_matrix
    cosine_sim = cosine_similarity(count_matrix)

    print(cosine_sim)
    search_phrase_index = 0

    similar_tweets = list(enumerate(cosine_sim[search_phrase_index]))

    # Step 7: Get a list of similar tweets in descending order of similarity score
    sorted_similar_tweets= sorted(similar_tweets, key=lambda x: x[1], reverse=True)

    print(sorted_similar_tweets)

    for tweet in sorted_similar_tweets:
        print(get_tweet_from_index(tweet[0]+2))

    toptweet = sorted_similar_tweets[1][0]
    return toptweet

def runTopTweetRecommender():
    toptweet = getRecommendation()
    record = [(df.iloc[1][1], get_tweet_from_index(toptweet + 2))]
    data_to_append = pd.DataFrame(record)
    data_to_append.to_csv("faz.csv", mode='a', header=False)

runTopTweetRecommender()


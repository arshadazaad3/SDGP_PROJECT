from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pymongo
import json

# Step 1: Read CSV file
# df = pd.DataFrame(pd.read_excel('EnvironmentHashtags.xlsx'))
#


def get_index_from_hashtag(hashtag):
    return df[df.hashtag == hashtag]["index"].values[0]

def get_hashtag_from_index(index):
    return df[df.index == index]["hashtag"].values[0]

# Step 3: Create a colum in DF which combines all selected features
def combine_features(row):
    return row['hashtag'] + " " + row['tweet']

def getRecommendation(input_hashtag):

    # Step 2: Select Features
    features = ['hashtag', 'tweet']

    df["combined_features"] = df.apply(combine_features, axis=1)

    pd.set_option('display.max_columns', None)
    # print(df)


    # Step 4: Create count matrix from this new combined column
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df["combined_features"])


    # Step 5: Compute cosine similarity based on count_matrix
    cosine_sim = cosine_similarity(count_matrix)

    # print(cosine_sim)

    hashtag_user_likes = input_hashtag

    # Step 6: Get Index of this hashtag from its title
    hashtag_index = get_index_from_hashtag(hashtag_user_likes)

    similar_hashtags = list(enumerate(cosine_sim[hashtag_index]))

    # Step 7: Get a list of similar movies in descending order of similarity score
    sorted_similar_hashtags = sorted(similar_hashtags, key=lambda x: x[1], reverse=True)

    # print(sorted_similar_hashtags)
    # Step 8: Print titles of first 50 movies

    results = []
    # for tweet in sorted_similar_hashtags:
    #     print(get_hashtag_from_index(tweet[0]))
    #
    for i in range(0,5):
        tweet = sorted_similar_hashtags[i]
        results.append(get_hashtag_from_index(tweet[0]))

    return results


def runTopHashtagRecommender(hashtag,category):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["SDGP"]
    mycol = mydb[category]

    global df
    df = mycol.find()
    df = pd.DataFrame(df)
    # print(df)

    top5Results = getRecommendation(hashtag)
    json_str = json.dumps(top5Results)
    return json_str



# runTopHashtagRecommender("SaveAustralia","Environment")


<<<<<<< HEAD:Data_Science/HashtagRecommender.py
getRecommendation("#coronaVirus")
=======
>>>>>>> 2e3b6d3ccb4fee8295f5a844763a19f737f39b95:Data_Science/SimilarHashtagsRecommender/TopHashtagRecommender.py


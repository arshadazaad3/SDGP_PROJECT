import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sklearn
import os
from random import randint

import pymongo
from pymongo import MongoClient
client =MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
db = client.test  # test connection if connected

db = client['newscategory']     #open database if not available will be created

TRAIN_MODEL_PATH = os.path.join("input/", "NewsTrain1.csv")
df = pd.read_csv(TRAIN_MODEL_PATH)
# Associate Category names with numerical index and save it in new column category_id
df['category_id'] = df['Category'].factorize()[0]
category_id_df = df[['Category', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Category']].values)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

features = tfidf.fit_transform(df.Text).toarray() # Remaps the words in the 1490 articles in the text column of 
                                                  # data frame into features (superset of words) with an importance assigned 
                                                  # based on each words frequency in the document and across documents

labels = df.category_id                           # represents the category of each of the 1490 articles
features.shape # How many features are there ? 
# category_to_id.items()
# df.groupby('Category').category_id.count()
from sklearn.feature_selection import chi2

N = 3  # We are going to look for top 3 categories

#For each category, find words that are highly corelated to it
for Category, category_id in sorted(category_to_id.items()):
    features_chi2 = chi2(features, labels == category_id)                   # Do chi2 analyses of all items in this category
    indices = np.argsort(features_chi2[0])                                  # Sorts the indices of features_chi2[0] - the chi-squared stats of each feature
    feature_names = np.array(tfidf.get_feature_names())[indices]            # Converts indices to feature names ( in increasing order of chi-squared stat values)
    unigrams = [v for v in feature_names if len(v.split(' ')) == 1]         # List of single word features ( in increasing order of chi-squared stat values)
    bigrams = [v for v in feature_names if len(v.split(' ')) == 2]          # List for two-word features ( in increasing order of chi-squared stat values)
#     print("# '{}':".format(Category))
#     print("  . Most correlated unigrams:\n       . {}".format('\n       . '.join(unigrams[-N:]))) # Print 3 unigrams with highest Chi squared stat
#     print("  . Most correlated bigrams:\n       . {}".format('\n       . '.join(bigrams[-N:]))) # Print 3 bigrams with highest Chi squared stat
from sklearn.manifold import TSNE

# Sampling a subset of our dataset because t-SNE is computationally expensive
SAMPLE_SIZE = int(len(features) * 0.3)
np.random.seed(0)
indices = np.random.choice(range(len(features)), size=SAMPLE_SIZE, replace=False)          # Randomly select 30 % of samples
projected_features = TSNE(n_components=2, random_state=0).fit_transform(features[indices]) # Array of all projected features of 30% of Randomly chosen samples 
my_id = 0 # Select a category_id
projected_features[(labels[indices] == my_id).values]
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.model_selection import cross_val_score


models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]
CV = 5  # Cross Validate with 5 different folds of 20% data ( 80-20 split with 5 folds )

#Create a data frame that will store the results for all 5 trials of the 3 different models
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = [] # Initially all entries are empty
for model in models:
    model_name = model.__class__.__name__
    # create 5 models with different 20% test sets, and store their accuracies
    accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
    # Append all 5 accuracies into the entries list ( after all 3 models are run, there will be 3x5 = 15 entries)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
        
# Store the entries into the results dataframe and name its columns    
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
from sklearn.model_selection import train_test_split

model = LogisticRegression(random_state=0)

#Split Data 
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.33, random_state=0)

#Train Algorithm
model.fit(X_train, y_train)

# Make Predictions
y_pred_proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)

texts = []
# importing requests package 
import requests      
  
def NewsFromBBC():
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
# fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
# getting all articles in a string article 
    article = open_bbc_page["articles"] 
# empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        texts.append(ar["title"]) 
                      
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  

#create list to append news after categorizing
sportLists=[]
techList=[]
entertainmentList=[]
healthList=[]
businessList=[]
politicsList=[]

#categorizing news based on topics
#And appending to list and declared Above
text_features = tfidf.transform(texts)
predictions = model.predict(text_features)
for text, predicted in zip(texts, predictions):
    
    if format(id_to_category[predicted])=='sport':
        sportText=format(text)
        sportLists.append(sportText)
    elif format(id_to_category[predicted])=='politics':
        politcsText=format(text)
        politicsList.append(politcsText)
    elif format(id_to_category[predicted])=='business':
        businessText=format(text)
        businessList.append(businessText)
    elif format(id_to_category[predicted])=='entertainment':
        entertainmentText=format(text)
        entertainmentList.append(entertainmentText)
    elif format(id_to_category[predicted])=='health':
        healthText=format(text)
        healthList.append(healthText)
    elif format(id_to_category[predicted])=='tech':
        techText=format(text)
        techList.append(techText)

##Test For Keyword If Prediction Works Fine

# texts = ["madrid"]
# text_features = tfidf.transform(texts)
# predictions = model.predict(text_features)
# for text, predicted in zip(texts, predictions):
#   print('"{}"'.format(text))
#   print("  - Predicted as: '{}'".format(id_to_category[predicted]))
#   print("")

#Establishing connection to MongoDB


#Health DB
healthCollection = db['healths']  # new collection for Health news according to Category

#Politics DB
politicsCollection = db['politics']  # new collection for Health news according to Category

#techs DB
techsCollection = db['techs']  # new collection for Health news according to Category

#Entertainment DB
entertainmentCollection = db['entertainments']  # new collection for Health news according to Category

#Business DB
# db.business.drop()  # delete collection to have fresh collection
businessCollection = db['business']  # new collection for Health news according to Category

#Sport DB
sportsCollection = db['sports']  # new collection for Health news according to Category

#create dictionary and Dataframe
businessListDict={}
column_names = ['Text']

businessdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
sportsListDict={}
sportsdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
entertainmentListDict={}
entertainmentdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
politicsListDict={}
politicsdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
healthListDict={}
healthdf = pd.DataFrame(columns = column_names)
#create dictionary and Dataframe

techListDict={}
techdf = pd.DataFrame(columns = column_names)

#iterate through list and append to dataframe then to list and then send to DB
if len(businessList)!=0:
    for item in businessList:
        businessdf = businessdf.append({'Text': item}, ignore_index=True)
    data = businessdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    businessCollection.insert_many(data_dict)
else:
    print('empty list of businessList')

    
#iterate through list and append to dataframe then to list and then send to DB
if len(sportLists)!=0:
    for item in sportLists:
        sportsdf = sportsdf.append({'Text': item}, ignore_index=True)
    data = sportsdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    sportsCollection.insert_many(data_dict)
else:
    print('empty list of sportsList')
    
#iterate through list and append to dataframe then to list and then send to DB
if len(techList)!=0:
    for item in techList:
        techdf = techdf.append({'Text': item}, ignore_index=True)
    data = techdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    techsCollection.insert_many(data_dict)
else:
    print('empty list of tech')
    
#iterate through list and append to dataframe then to list and then send to DB
if len(entertainmentList)!=0:
    for item in entertainmentList:
        entertainmentdf = entertainmentdf.append({'Text': item}, ignore_index=True)
    data = entertainmentdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    entertainmentCollection.insert_many(data_dict)
else:
    print('empty list of entertainment')
    
#iterate through list and append to dataframe then to list and then send to DB
if len(politicsList)!=0:
    for item in politicsList:
        politicsdf = politicsdf.append({'Text': item}, ignore_index=True)
    data = politicsdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    politicsCollection.insert_many(data_dict)
else:
    print('empty list of politicsCollection')

#iterate through list and append to dataframe then to list and then send to DB
if len(healthList)!=0:
    for item in healthList:
        healthdf = healthdf.append({'Text': item}, ignore_index=True)
    data = healthdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    healthCollection.insert_many(data_dict)
else:
    print('empty list of Health')



        

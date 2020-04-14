import pickle

import sklearn.datasets as skd

news_test = skd.load_files('E:\Studies\Give A Try\SDGP\Data Set\\Test BBC', encoding='ISO-8859-1')
print(news_test['target_names'])
listOfTopics = news_test['target_names']

# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
#
# text_clf = Pipeline([('vect', TfidfVectorizer()),
#                      ('clf', MultinomialNB())])

with open('text_classifier', 'rb') as training_model:
    model = pickle.load(training_model)

try:
    x = (model.predict(news_test.data))[0]
    print(listOfTopics[x])
except:
    print("SOME ERROR OCCURRED")

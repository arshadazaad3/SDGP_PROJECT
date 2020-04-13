import sklearn.datasets as skd


categories = ['entertainment', 'business', 'politics', 'sport', 'tech', 'space']
news_train = skd.load_files('E:\Studies\Give A Try\SDGP\Data Set\\News & BBC', categories=categories,
                            encoding='ISO-8859-1')
# news_test = skd.load_files('E:\Studies\Give A Try\SDGP\Data Set\\News-bydate-test', categories=categories,
#                            encoding='ISO-8859-1')

# CountVectorizer - provides a simple way to both tokenize a collection of text documents and
# build a vocabulary of known words
from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()
X_train_tf = count_vect.fit_transform(news_train.data)
print(X_train_tf.shape)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_tf)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB().fit(X_train_tfidf, news_train.target)
docs_new = ["astronaut works hard"]
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)

# for i in range(0, 6):
#     print((i), news_train['target_names'][i])

print(news_train['target_names'])
y = 0
for x in predicted:
    print(x, news_train['target_names'][x], "  :  ", docs_new[y])
    y += 1;
filename = 'tweets.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize

tokens = word_tokenize(text)
# # convert to lower case
tokens = [w.lower() for w in tokens]
# # remove punctuation from each word
import string
#
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# # remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# # filter out stop words

print(words[:100])


# with open('WITH HTTPS.txt', 'w') as f:
#     for item in words:
#         f.write("%s " % item)


for i in words:
    if i=="https":
        words.remove(i)
print (words)

with open('NO_HTTPS.txt', 'w') as f:
    for item in words:
        f.write("%s " % item)
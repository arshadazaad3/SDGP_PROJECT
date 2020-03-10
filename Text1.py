import random

import re


def review_generator():
    # text = ask_user()
    reviews = open("NO_HTTPS.txt", 'r')
    reviews = ''.join([i for i in reviews if not i.isdigit()]).replace("\n", " ").split(' ')

    index = 1
    chain = {}
    count = 50

    for word in reviews[index:]:
        key = reviews[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:

        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    print (message)
    return message


review_generator()

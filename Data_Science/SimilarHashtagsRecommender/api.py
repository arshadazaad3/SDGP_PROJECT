import flask
from flask import request, jsonify

import HashtagRecommender

app = flask.Flask(__name__)
app.config["DEBUG"] = True

""" README - GET METHOD 1
 Returns -> Top 5 similar Hash tags from the given Category (Only works if the given hash tag is from the same category)
 run this URL to get an idea about this route
 http://127.0.0.1:5000/api/v1/tophashtag?hashtag=SaveAustralia&category=Environment
 2 arguments are needed to run this Query.
 hashtag -> The target hash tag
 category -> The category of that hash tag """
@app.route('/api/v1/tophashtag', methods=['GET'])
def api_id():

    if 'hashtag' in request.args:
        hashtag = str(request.args['hashtag'])
    else:
        return "Error: No hashtag field provided. Please specify a hashtag."

    if 'category' in request.args:
        category = str(request.args['category'])
    else:
        return "Error: No category field provided. Please specify a category."

    results = HashtagRecommender.runTopHashtagRecommender(hashtag,category)

    return results



app.run()

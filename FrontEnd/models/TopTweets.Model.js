
const mongoose = require('mongoose')

const Schema = mongoose.Schema;

const Top5Tweets = new Schema({

    Text: {
        type: String,
        required: true

    }

},
);

const TopFiveTweetsSchema = mongoose.model('topfivetweets', Top5Tweets);

module.exports = TopFiveTweetsSchema;
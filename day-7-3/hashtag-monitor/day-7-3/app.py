from flask import Flask
from TwitterApi import TwitterApi
import json
import os

app = Flask(__name__)
twitter = TwitterApi()


@app.route('/search/<event>')
def search(event):
    my_tweets = twitter.get_tweets(count=1)
    payload = []
    for tweet in my_tweets:
        payload.append({'text': tweet.AsDict()['text'], 'tags': twitter.get_hash_tags(tweet)})
    matches = twitter.event_matches(event_types=[{'type': event, 'count': 1}], tweet_count=1)
    return json.dumps({
        'query': event,
        'tweet': payload,
        'matches': matches
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['REST_PORT'])

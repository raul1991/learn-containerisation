from flask import Flask
from TwitterApi import TwitterApi
import json
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean

# configuration for the connection
# mysql://user:password@host:port/databasename
databaseFile = "mysql://{0}:{1}@{2}:{3}/{4}".format('root', os.environ['DB_ROOT_PASSWORD'], os.environ['DB_HOST'],
                                                os.environ['DB_PORT'], os.environ['DB_NAME'])
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseFile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
twitter = TwitterApi()


class Tweets(db.Model):
    id = Column('id', Integer, primary_key=True)
    matches = Column('matches', Boolean)
    query = Column('query', String(100))
    tweet = Column('tweet', String(100))


def save_it_to_db(data):
    tweet = Tweets(matches=data['matches'], tweet=data['tweet'], query=data['query'])
    db.session.add(tweet)
    db.session.commit()


@app.route('/search/<event>')
def search(event):
    my_tweets = twitter.get_tweets(count=1)
    payload = []
    for tweet in my_tweets:
        payload.append({'text': tweet.AsDict()['text'], 'tags': twitter.get_hash_tags(tweet)})
    matches = twitter.event_matches(event_types=[{'type': event, 'count': 1}], tweet_count=1)
    data = {
        'query': event,
        'tweet': payload,
        'matches': matches
    }
    save_it_to_db(data)
    return json.dumps(data)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(host='0.0.0.0', port=os.environ['REST_PORT'])

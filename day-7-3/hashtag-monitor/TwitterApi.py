import twitter
import constants as api


class TwitterApi(object):
    def __init__(self) -> None:
        self.api = twitter.Api(consumer_key=api.consumer_key,
                               consumer_secret=api.consumer_secret,
                               access_token_key=api.access_token_key,
                               access_token_secret=api.access_token_secret)

    def get_tweets(self, screen_name=None, count=1):
        timeline = self.api.GetUserTimeline(screen_name=screen_name, count=count)
        return timeline

    def get_all_tweets(self, screen_name, count):
        timeline = self.api.GetUserTimeline(screen_name=screen_name, count=count)
        earliest_tweet = min(timeline, key=lambda x: x.id).id
        print("getting tweets before:", earliest_tweet)

        while True:
            tweets = self.api.GetUserTimeline(
                screen_name=screen_name, max_id=earliest_tweet, count=count)
            new_earliest = min(tweets, key=lambda x: x.id).id

            if not tweets or new_earliest == earliest_tweet:
                break
            else:
                earliest_tweet = new_earliest
                print("getting tweets before:", earliest_tweet)
                timeline += tweets
        return timeline

    def post_a_tweet(self, message):
        if len(message) > 160:
            raise NotImplementedError("Twitter does not support tweets with more than 160 characters.")
        else:
            model = self.api.PostUpdate(status=message)
            print(model.AsDict())

    def get_hash_tags(self, raw_tweet) -> {}:
        tags = {}
        for tag in raw_tweet.AsDict()['hashtags']:
            __tag = tag['text'].lower()
            curr_count = tags.get(__tag, 0)
            tags[__tag] = curr_count + 1
        return tags

    def event_matches(self, event_types: [], tweet_count: int) -> bool:
        """
        Tells if any event type(s) sent in the request payload exist in the last 'tweet_count' number of tweets'
        hash tags or not for the 'count' number of times or not.
        Example payload:

        {"event_types": [{"type": "earthquake", "count": 5}], "tweet_count": 5}

        If this method is being called with the above payload, it will return True if earthquake exists in any hash tag
        for 1 number of time or high alert exists for 5 times.
        :param event_types: list of type and count. For example
        [{'type': 'earthquake', 'count': 1}]
        :param tweet_count: the number of tweets to take into account
        :return: True/False
        """
        all_tweets = self.get_tweets(count=min(10, int(tweet_count)))
        events = {}
        for tw in all_tweets:
            all_tags = self.get_hash_tags(tw)
            # print("Tags: ", all_tags)
            for event_type in event_types:
                et = event_type['type']
                if all_tags.get(et.lower(), '') != '':
                    # event exists, increment its count
                    curr_count = events.get(et, 0)
                    events[et] = curr_count + 1
                    my_count = events[et]
                    # print("Current_count: %s", my_count)
                    if my_count >= event_type['count']:
                        return True
        return False

# uncomment for testing
# t = TwitterApi()
# my_tweets = t.get_tweets(count=7)
# payload = []
# for tweet in my_tweets:
#     payload.append({'text': tweet.AsDict()['text'], 'tags': t.get_hash_tags(tweet)})
# print(payload)
# print(t.event_matches(event_types=[{'type': '5G', 'count': 1}], tweet_count=8))
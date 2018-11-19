import tweepy
import TwitterKeys
import PythonMongo
import json
consumer_key= TwitterKeys.consumer_key
consumer_secret= TwitterKeys.consumer_secret
access_token= TwitterKeys.access_token
access_token_secret= TwitterKeys.access_token_secret
spain = [-6.6317490496,36.8911825246,-0.0331033866,42.7732057225]
class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        print(data)
        print("----------------------------------------------------------------------------------------------------")
        data_json = json.loads(data)
        PythonMongo.insertDB(data_json)
        return True

    # def on_data(self, data):
    #     # Decode the JSON data
    #     tweet = json.loads(data)
    #
    #     # Print out the Tweet
    #     print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":

    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit=True)
    bluthquotes_tweets = twitter_api.user_timeline(screen_name='elonmusk', count=100) #cambiar por el username de twitter
    for status in bluthquotes_tweets:
        print(status.text)
    stream = tweepy.Stream(auth, listener)

    stream.filter(track=['bendecir'], locations=spain)
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import TwitterKeys
import PythonMongo
import json
consumer_key= TwitterKeys.consumer_key
consumer_secret= TwitterKeys.consumer_secret
access_token= TwitterKeys.access_token
access_token_secret= TwitterKeys.access_token_secret
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        print("----------------------------------------------------------------------------------------------------")
        data_json = json.loads(data)
        PythonMongo.insertDB(data_json)
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":

    listener = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    stream = Stream(auth, listener)

    stream.filter(track=['china'])
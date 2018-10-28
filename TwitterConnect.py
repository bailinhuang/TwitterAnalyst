from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import TwitterKeys
 
consumer_key= TwitterKeys.consumer_key
consumer_secret= TwitterKeys.consumer_secret
access_token= TwitterKeys.access_token
access_token_secret= TwitterKeys.access_token_secret
file = open('tweets.txt', 'w')
listTweets = []
class StdOutListener(StreamListener):
    def on_data(self, data):
        #print(data)
        listTweets.append(data)
        global file
        file.write(data)
        file.write("\n \n")
        #print("----------------------------------------------------------------------------------------------------")
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


# class Connector():
def main():

    listener = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=['china'])

def connectUser():
    print("Escriba el username de twitter")
    username = input()

    #
    # def MineTimelineData(self, idToMine):
    #     cursor = tweepy.Cursor(twitterAPI.user_timeline, id=idToMine)
    #     while (tweepy.Cursor(twitterAPI.user_timeline).items() != None):
    #         try:
    #             for page in cursor.pages():
    #                 for tweet in page:
    #                     yield tweet
    #         except tweepy.RateLimitError:
    #             print("Rate limit reached! Waiting 15 minutes...")
    #             time.sleep(60 * 15)  # wait 15 minutes (900 seconds)

main()
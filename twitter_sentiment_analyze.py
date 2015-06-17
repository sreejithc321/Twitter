import json
from textblob import TextBlob
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Add twitter keys and tokens
from config import *

class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):
	
		# decode json
    	dict_data = json.loads(data)

        if dict_data.get('text', {}):
		
			# Get tweet text
			tweet = TextBlob(dict_data["text"])
		
			# output sentiment polarity
			print "Tweet : ", tweet
			print "Polarity : ",tweet.sentiment.polarity
		
			# determine if sentiment is positive, negative, or neutral
			if tweet.sentiment.polarity < 0:
				sentiment = "Negative"
			elif tweet.sentiment.polarity == 0:
				sentiment = "Neutral"
			else:
				sentiment = "Positive"
						
			# output sentiment
			print "Sentiment : ",sentiment
			print "\n"
		    
        return True

    # on failure
    def on_error(self, status):
        print status

if __name__ == '__main__':

    # tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)
    stream.userstream(_with='followings')


# Visualize Twitter Sentiment, Language and Location data

import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import API
from config import *
import json
from textblob import TextBlob
from pylab import *


if __name__ == '__main__':

	# Connection to Twitter Streaming API
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = API(auth)
	tweets_file = api.search(q=SEARCH_KEYWORD, count= TWEET_COUNT)
    
    # Sentiment Analysis
	pos = net = neg = 0
	for t in tweets_file:
		tweet = TextBlob(t.text)
		if tweet.sentiment.polarity > 0:
			pos = pos + 1
		if tweet.sentiment.polarity == 0:
			net = net + 1	
		if tweet.sentiment.polarity <0:
			neg = neg + 1
		print tweet,'\n', tweet.sentiment.polarity
		print '\n'
	print len(tweets_file)
	
    # Plot Sentiment	
	figure(1, figsize=(8,8))
	labels = 'Positive', 'Negative', 'Neutral'
	fracs = [pos,neg,net]
	explode=( 0.025, 0.025, 0.025)
	pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)                
	title(' Sentiment Analysis of \' ' + SEARCH_KEYWORD+' \' ', bbox={'facecolor':'0.6', 'pad':5})
	show()

    # Language
	tweets = pd.DataFrame()
	tweets['lang'] = map(lambda tweet: tweet.lang, tweets_file)
	tweets_by_lang = tweets['lang'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Languages', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
	#print tweets_by_lang[:5]
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
	plt.show()
	
	# Location
	tweets['places'] = map(lambda tweet: tweet.user.location.lower(), tweets_file)
	tweets_by_country = tweets['places'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Places', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 Locations', fontsize=15, fontweight='bold')
	#print tweets_by_country[1:6]
	tweets_by_country[1:6].plot(ax=ax, kind='bar', color='blue')
	plt.show()


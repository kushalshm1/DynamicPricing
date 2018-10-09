import tweepy
from textblob import TextBlob
import re 

def extractTweetsToCSV():
	consumer_key = '***************************'
	consumer_secret = '****************************************************'
	user_access_token = '**************************************************'
	user_access_secret = '************************************************'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


	auth.set_access_token(user_access_token,user_access_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True)


	def getTweets(name):
	    x = []
	    public_tweets = api.search(name)
	    for tweets in public_tweets:
	        x.append(tweets.text)
	    return x


	'''High Hype movies tweets collection'''
	print("Collecting Movie Tweets with high hype.....")
	f = open("data/mostHyped.txt","r")
	wordContents = f.read()
	wordList = re.split(r'[\n\r]+', wordContents)
	allTweetsHigh = []
	y = []
	for i in range(0,len(wordList)):
	    y = []
	    y = ((getTweets(wordList[i])))
	    for j in range(0,len(y)):
	        allTweetsHigh.append(y[j])
	print("Most Hyped Tweets Collected")
	#########################################



	'''Medium Hype movie tweets collection'''
	print("Collecting Movie Tweets with medium hype.....")
	f = open("data/mediumHyped.txt","r")
	wordContents = f.read()
	wordList = re.split(r'[\n\r]+', wordContents)
	allTweetsMedium = []
	y = []
	for i in range(0,len(wordList)):
	    y = []
	    y = ((getTweets(wordList[i])))
	    for j in range(0,len(y)):
	        allTweetsMedium.append(y[j])
	print("Done Medium Hyped tweet scraping")
	#########################################



	'''Low hype movies tweet collection'''
	print("Collecting Movie Tweets with low hype.....")
	f = open("data/lowHyped.txt","r")
	wordContents = f.read()
	wordList = re.split(r'[\n\r]+', wordContents)
	allTweetsLow = []
	y = []
	for i in range(0,len(wordList)):
	    y = []
	    y = ((getTweets(wordList[i])))
	    for j in range(0,len(y)):
	        allTweetsLow.append(y[j])
	print("Done Low Hyped tweet scraping")        
	########################################


	'''Defining Classes for data LowHype:0 | MediumHype:1 | HighHype:2'''
	allTweets = allTweetsLow + allTweetsMedium + allTweetsHigh
	allClasses = []
	allClasses = [0]*len(allTweetsLow) + [1]*len(allTweetsMedium) + [2]*len(allTweetsHigh)
	#####################################################################################


	'''Making DataFrame out of all Tweets and class and writing it into a CSV file'''
	dictTweets = {'tweet_txt':allTweets,'class':allClasses}
	import pandas as pd
	dataFrameTweets = pd.DataFrame(dictTweets)
	dataFrameTweets.to_csv('data/classifiedTweets.csv',encoding='utf-8')


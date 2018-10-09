import pandas as pd
import numpy as np 
import string
import re
from collections import Counter
import io
import requests


trainingData = pd.DataFrame(pd.read_csv('classifiedTweets.csv'))

'''Seperating all respective class tweets'''
classZeroTweets = trainingData[trainingData['class']==0]
classOneTweets = trainingData[trainingData['class']==1]
classTwoTweets = trainingData[trainingData['class']==2]


'''Keeping all tweets of single class in a single string for easy data processing'''
wholeClassZeroData = ''
wholeClassOneData = ''
wholeClassTwoData = ''
for i in range(0,len(classZeroTweets)):
    temp = classZeroTweets['tweet_txt'].iloc[i]
    temp.lower()
    temp = re.sub(r'[^\w\s]','',temp)
    wholeClassZeroData = wholeClassZeroData + " " + temp
for i in range(0,len(classOneTweets)):
    temp = classOneTweets['tweet_txt'].iloc[i]
    temp.lower()
    temp = re.sub(r'[^\w\s]','',temp)
    wholeClassOneData = wholeClassOneData + " " + temp
for i in range(0,len(classTwoTweets)):
    temp = classTwoTweets['tweet_txt'].iloc[i]
    temp.lower()
    temp = re.sub(r'[^\w\s]','',temp)
    wholeClassTwoData = wholeClassTwoData + " " + temp


'''Making a dictionary that contains frequencies of all unique words in tweet'''
zeroFreq = dict(Counter(wholeClassZeroData.split()))
oneFreq = dict(Counter(wholeClassOneData.split()))
twoFreq = dict(Counter(wholeClassTwoData.split()))
zeroFreqValues = list(zeroFreq.values())
oneFreqValues = list(oneFreq.values())
twoFreqValues = list(twoFreq.values())
zeroFreqKeys = list(zeroFreq.keys())
oneFreqKeys = list(oneFreq.keys())
twoFreqKeys = list(twoFreq.keys())
zeroFreqValues = np.array(zeroFreqValues)
zeroFreqValues  = zeroFreqValues/len(zeroFreqValues)
oneFreqValues = np.array(oneFreqValues)
oneFreqValues = oneFreqValues/len(oneFreqValues)
twoFreqValues = np.array(twoFreqValues)
twoFreqValues = twoFreqValues/len(twoFreqValues)

'''Making a dictionary that contains Relative frequencies of all unique words in tweet'''
zeroRF = dict(zip(zeroFreqKeys,zeroFreqValues))
oneRF = dict(zip(oneFreqKeys,oneFreqValues))
twoRF = dict(zip(twoFreqKeys,twoFreqValues))

return [zeroRF,oneRF,twoRF]

import pandas as pd
import numpy as np 
import string
import re
from collections import Counter
import io
import requests


mainData = pd.DataFrame(pd.read_csv('data/classifiedTweets.csv'))


trainingData,testData = np.split(mainData,[int(0.7*len(mainData))])



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



priorProbabilityZero = 0 
priorProbabilityOne = 0
priorProbabilityTwo = 0


answers = []
correct = 0

pZero = np.log(len(classZeroTweets)/len(trainingData))
pOne = np.log(len(classOneTweets)/len(trainingData))
pTwo = np.log(len(classTwoTweets)/len(trainingData))


for i in range(0,len(testData)):
    temp = testData['tweet_txt'].iloc[i]
    temp = temp.lower()
    temp = re.sub(r'[^\w\s]','',temp)
    temp = temp.split()
    
    commonZero = list(set(temp) & set(zeroRF.keys()))
    commonOne = list(set(temp) & set(oneRF.keys()))
    commonTwo = list(set(temp) & set(twoRF.keys()))

    
    for k in range(0,len(commonZero)):
        priorProbabilityZero = priorProbabilityZero + np.log(zeroRF[commonZero[k]])
    for a in range(0,len(commonOne)):
        priorProbabilityOne = priorProbabilityOne + np.log(oneRF[commonOne[a]])
    for b in range(0,len(commonTwo)):
        priorProbabilityTwo = priorProbabilityTwo + np.log(twoRF[commonTwo[b]])
        
    finalBayesZero = (priorProbabilityZero*pZero)/((priorProbabilityZero*pZero)+(priorProbabilityOne*pOne)+(priorProbabilityTwo*pTwo))
    finalBayesOne = (priorProbabilityOne*pOne)/((priorProbabilityZero*pZero)+(priorProbabilityOne*pOne)+(priorProbabilityTwo*pTwo))
    finalBayesTwo = (priorProbabilityTwo*pTwo)/((priorProbabilityZero*pZero)+(priorProbabilityOne*pOne)+(priorProbabilityTwo*pTwo))

    allBayes = [finalBayesZero,finalBayesOne,finalBayesTwo]
    maxIndex = allBayes.index(max(allBayes))
    if(maxIndex==0):    
        answers.append(0)
    elif(maxIndex==1):
        answers.append(1)
    else:
        answers.append(2)
        
        
for i in range(0,len(answers)):
    if(answers[i] == testData['class'].iloc[i]):
        correct = correct+1
        
        
print("=================================================")
print("Correct Answers: ",correct,"Out of:",len(answers))
print("=================================================")

accuracy = (correct/len(answers))*100
print("=================================")
print("TestingAccuracy: ",accuracy,"%")
print("=================================")
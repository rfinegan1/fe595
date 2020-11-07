#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:06:23 2020

@author: ryanfinegan
"""

#libraries
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import tokenize

#input a sentence as a string to get the output sentiment score of that statement
def sentiment(S):
    #calling vader sentiment 
    analyzer = SentimentIntensityAnalyzer()
    #returning the negative, neutral, positive, and neutral scores
    return analyzer.polarity_scores(S)

#input a long paragraph or string with many sentences as the input. Outputs each sentence compound score in descending order
def sentiment_ranker(S):
    #calling vader sentiment
    analyzer = SentimentIntensityAnalyzer()
    #results variable to append the sentences and scores of each sentence
    results = []
    #for loop through all the sentences
    for sentence in tokenize.sent_tokenize(S):
        #the compound score of each sentence
        score = analyzer.polarity_scores(sentence)['compound']
        #appending the sentences and the scores to the results list
        results.append([sentence.replace('\n',' '),score])
    return pd.DataFrame(results, columns = ['Sentence','Score']).sort_values('Score',ascending=False).set_index('Sentence')
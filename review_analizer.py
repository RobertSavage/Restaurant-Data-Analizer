import os
import sqlite3
import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import text
from pandas import DataFrame
from tqdm import tqdm
import joblib
import scipy
from scipy.spatial import distance
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import nltk
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import string
import matplotlib.pyplot as plt


#creating the dataframe
df = pd.read_csv('data_set_UoB.csv',names=["Rating", "Review Text", "Date"])
print(df.columns)

count =  df['Review Text'].str.split().str.len()
df = df[~(count < 5)]


#this makes a data set for the last year only
df['Date'] = pd.to_datetime(df['Date'])
start_date = '08-01-2020'
end_date = '07-01-2021'
mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
df = df.loc[mask]
print(len(df))

#this seperates low and high ratings into 2 datasets
df_high_review = df[df['Rating'] >= 4].copy()
df_low_review = df[df['Rating'] < 4].copy()


#this vectorizes the data
def token_words(sentence):
	lemmatizer = WordNetLemmatizer()
	tokenizer = RegexpTokenizer(r'\w+')
	return [lemmatizer.lemmatize(word) for word in tokenizer.tokenize(sentence) if not (word.isdigit() or len(word) == 1)]

vectorizer = CountVectorizer(tokenizer = token_words)
tfidf = TfidfVectorizer()
#vectorized_text = vectorizer.fit_transform(tqdm(df['Review Text'])).todense()

df_high_review_vectorized = vectorizer.fit_transform(tqdm(df_high_review['Review Text'])).todense()
df_low_review_vectorized = vectorizer.fit_transform(tqdm(df_low_review['Review Text'])).todense()


#------------------------------------HIGHEST--------------------------------------------------
#this makes a list of the distance between eveything
df_distances = pd.DataFrame(cosine_similarity(df_high_review_vectorized, dense_output = True))

#finding most similarites for highest
best_match_highest = [0,0]
for row in range(len(df_distances)):
	indexing = df_distances[df_distances[row] > 0.55].index
	if len(indexing) > best_match_highest[0]:
		best_match_highest = [len(indexing),row]
		

print('--------------------HIGHEST-------------------------------')
#finding the best matches for highest
row_to_check = best_match_highest[0] - 1
smallest_list = df_distances[row_to_check].nlargest(n=11)

# Word Cloud
text = " "
for rev in df_high_review['Review Text']:
	text = text+rev
for char in string.punctuation:
	text = text.replace(char, ' ')
wordcloud = WordCloud().generate(text)
wordcloud.to_file("high_review.png")

rows_used = []
comment_num = 0
for i in smallest_list:

	indexing = df_distances[df_distances[row_to_check] == i].index
	
	if len(indexing) > 1:
		for row in indexing:
			if row not in rows_used:
				#print('Column number: ',row)
				print('Review Match #: ',comment_num)
				print('Rating:',df_high_review.iloc[int(row)]['Rating'])
				print('Review: ',df_high_review.iloc[int(row)]['Review Text'])
				print('\n')
				rows_used.append(row)
				comment_num	+= 1
	else:
		if indexing[0] not in rows_used and i != 0:
			#print('Column number: ',indexing[0])
			print('Review Match #: ',comment_num)
			print('Rating:',df_high_review.iloc[int(indexing[0])]['Rating'])
			print('Review: ',df_high_review.iloc[int(indexing[0])]['Review Text'])
			rows_used.append(indexing[0])
			comment_num	+= 1
			print('\n')


#------------------------------------LOWEST--------------------------------------------------
#this makes a list of the distance between eveything
df_distances = pd.DataFrame(cosine_similarity(df_low_review_vectorized, dense_output = True))

#finding most similarites for lowest
best_match_lowest = [0,0]
for row in range(len(df_distances)):
	indexing = df_distances[df_distances[row] > 0.55].index
	if len(indexing) > best_match_lowest[0]:
		best_match_lowest = [len(indexing),row]

# Word Cloud
text = " "
for rev in df_low_review['Review Text']:
	text = text+rev
for char in string.punctuation:
	text = text.replace(char, ' ')
wordcloud = WordCloud().generate(text)
wordcloud.to_file("low_review.png")


#finding the best matches for lowest
print('--------------------LOWEST-------------------------------')
row_to_check = best_match_lowest[0] - 1
smallest_list = df_distances[row_to_check].nlargest(n=11)

comment_num = 0
rows_used = []
for i in smallest_list:

	indexing = df_distances[df_distances[row_to_check] == i].index
	
	if len(indexing) > 1:
		for row in indexing:
			if row not in rows_used:
				#print('Column number: ',row)
				print('Review Match #: ',comment_num)
				print('Rating:',df_low_review.iloc[int(row)]['Rating'])
				print('Review: ',df_low_review.iloc[int(row)]['Review Text'])
				print('\n')
				comment_num	+= 1
				rows_used.append(row)
	else:
		if indexing[0] not in rows_used and i != 0:
			#print('Column number: ',indexing[0])
			print('Review Match #: ',comment_num)
			print('Rating:',df_low_review.iloc[int(indexing[0])]['Rating'])
			print('Review: ',df_low_review.iloc[int(indexing[0])]['Review Text'])
			rows_used.append(indexing[0])
			comment_num	+= 1
			print('\n')
	

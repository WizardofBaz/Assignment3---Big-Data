import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Processing 1
#Pie chart

df = pd.read_csv('Top_Stories_NYT.csv')
#print(df.head())
#df['section'] = df['section'].astype('|S80')

df["section"].replace("", np.nan).value_counts(dropna=False).plot(kind="pie")
#plt.show()
plt.title("NEWS CATEGORIES")
plt.savefig("News_Categories_Pie_Chart.png")

#Processing 2
#Sentiment Analysis of Abstract

from textblob import TextBlob
""" nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
 """
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
  #print(text)
  return text

df['abstract'].apply(lambda x: get_sentiment(' '.join(x)))

for column in df:
    columnSeriesObj = df["abstract"]
    
with open('sentiment_analysis_results.txt', 'w') as file:
    for abstract in df["abstract"].values:
        blob = TextBlob(str(abstract))  #Convert to string
        sentiment = blob.sentiment
        file.write(f'Sentiment: {sentiment}\n')

#Processing 3
from nltk import ngrams, word_tokenize
from collections import Counter

# Tokenize the text data in the column
df['tokenized_text'] = df['title'].apply(word_tokenize)

def generate_ngrams(tokens, n):
    return list(ngrams(tokens, n))

#value of 'n' for n-grams
n = 2 

df['ngrams'] = df['tokenized_text'].apply(lambda x: generate_ngrams(x, n))

df['ngrams_frequency'] = df['ngrams'].apply(lambda x: Counter(x))

df.to_csv("Top_Stories_NYT_N-Grams.csv",index=False)

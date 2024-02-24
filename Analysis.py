import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Processing 1

df = pd.read_csv('Top_Stories_NYT.csv')
#print(df.head())
#df['section'] = df['section'].astype('|S80')

df["section"].replace("", np.nan).value_counts(dropna=False).plot(kind="pie")
#plt.show()
plt.savefig("News_Categories_Pie_Chart.png")

#Processing 2
#Sentiment Analysis of Abstract

from textblob import TextBlob
""" nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon') """
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_tweet_sentiment(text):
  #print(text)
  return text

df['abstract'].apply(lambda x: get_tweet_sentiment(' '.join(x)))

for column in df:
    columnSeriesObj = df["abstract"]
    
    # Open a file for writing
with open('sentiment_analysis_results.txt', 'w') as file:
    for abstract in df["abstract"].values:
        blob = TextBlob(str(abstract))  # Convert to string
        sentiment = blob.sentiment
        # Write the sentiment analysis result to the file
        file.write(f'Sentiment: {sentiment}\n')
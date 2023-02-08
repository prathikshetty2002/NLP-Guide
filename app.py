import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from goose3 import Goose
import plotly.express as px


st.title('Twitter sentimental analysis')
sentence = st.text_input('Enter your Topic','topic or text')

attributes_container = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(sentence).get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent])
    
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
print(tweets_df)
print(tweets_df['Tweets'][0])

if st.checkbox('show tweets'):
    st.write(tweets_df.head(10))


def sentiment_scores(sentence):

	
	sid_obj = SentimentIntensityAnalyzer()

	sentiment_dict = sid_obj.polarity_scores(sentence)

	print(sentiment_dict)

	
	if sentiment_dict['compound'] >= 0.05 :
		st.write("🙂 Positive")

	elif sentiment_dict['compound'] <= - 0.05 :
		st.write("☹️ Negative")

	else :
		st.write("😐 Neutral")

sentiment_scores(sentence)

# def sentiment_article(url):
#     senti=[]
    
#     goose = Goose()
#     articles = goose.extract(url)
#     sentence1 = articles.cleaned_text
#     sid_obj = SentimentIntensityAnalyzer()
#     sentiment_dict = sid_obj.polarity_scores([sentence1])
#     print(sentiment_dict['neg']*100, "% Negative")
#     print(sentiment_dict['pos']*100, "% Positive")
#     print("Review Overall Analysis", end = " ") 
#     if sentiment_dict['compound'] >= 0.05 :
#         senti.append("Positive")
#     elif sentiment_dict['compound'] <= -0.05 :
#         senti.append("Negative")
#     else :
#         senti.append("Neutral")
#     return senti

# result=sentiment_article(st.text_input('enter the article url'))
# st.write(result)
# print(result)



   

# def hate_speech(sentence):
#     sonar = Sonar()
#     detect=sonar.ping(sentence)
#     st.write(detect['top_class'])
# hate_speech(sentence)   


# print("\n1st statement :")
# sentence = "Vivek….congress has established PSUs airports ports not for Adani"

# sentiment_scores(sentence)

# print("\n2nd Statement :")
# sentence = "study is going on as usual"
# sentiment_scores(sentence)

# print("\n3rd Statement :")
# sentence = "I am very sad today."
# sentiment_scores(sentence)
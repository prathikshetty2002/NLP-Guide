import pandas as pd
import streamlit as st
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import snscrape.modules.twitter as sntwitter
from goose3 import Goose
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


st.title('Twitter sentimental analysis')
selected = option_menu(
            menu_title=None,  
            options=["Topic/Hashtag Analysis", "User Analysis"],  
            icons=["bar-chart", "info-circle"],  
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )

if(selected=='Topic/Hashtag Analysis'):
    # col1, col2, col3 = st.columns(3)
    # if col2.button('Analyse twitter topics'):
         st.subheader('Topic/Hashtag analyser')
         sentence = st.text_input('Enter Topic/Hashtag','War in ukraine')


         attributes_container = []

         for i,tweet in enumerate(sntwitter.TwitterSearchScraper(sentence).get_items()):
            if i==30:
                break
            attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent, tweet.lang])
            
         tweets_df1 = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets","Tweet_lang"])
        #  tweets_df=tweets_df1[tweets_df1["Tweet_lang"]=="en"]
        #  print(tweets_df)



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
         tweets=tweets_df1['Tweets']
         analyzer=SentimentIntensityAnalyzer()    
         tweetsWithSent = []
        
         for i in range(30):
            if i==30:
                break   
            text = (tweets[i])
            ps = analyzer.polarity_scores(text)
            if ps['compound'] >= 0.05 :
                sentiment="🙂 Positive"
                value=ps['compound']
                count=1

            elif ps['compound'] <= - 0.05 :
                sentiment="☹️ Negative"
                value=ps['compound']
                count=1
            else :
                sentiment="😐 Neutral"
                value=ps['compound']
                count=1
            
            tweetsWithSent.append([text,sentiment,value,count])
         print(tweetsWithSent)
         tweetsWithSent_df=pd.DataFrame(tweetsWithSent,columns=['Tweets','Sentiment','value','count'])
         sentiment_scores(sentence)
         col1, col2, col3 = st.columns(3)
         if col2.button('Analyse twitter topics'):
            #  if st.checkbox('show tweets'):
                 st.write(tweetsWithSent_df.head(10))  
            #  if st.checkbox('show visualization'):
                 draw=px.bar(tweetsWithSent_df,x='Sentiment',y='count',color='Sentiment',title='Sentiment graph of user tweets',hover_data=['value'])
                 st.plotly_chart(draw, use_container_width=True)
         

        
       
elif(selected=='User Analysis'):
    
        st.subheader('User profile analyser')

        username=st.text_input('Enter username','I_am_prathik')

        attributes_container1=[]
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:${username}').get_items()):
            if i==30:
                break
            attributes_container1.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent, tweet.lang,tweet.hashtags])
                
        tweets_df2 = pd.DataFrame(attributes_container1, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets","Tweet_lang","Hashtags"])
            
        print(tweets_df2)
        tweets=tweets_df2['Tweets']
        analyzer=SentimentIntensityAnalyzer()    
        tweetsWithSent = []
        
        for i in range(30):
            if i==30:
                break   
            text = (tweets[i])
            ps = analyzer.polarity_scores(text)
            if ps['compound'] >= 0.05 :
                sentiment="🙂 Positive"
                value=ps['compound']
                count=1

            elif ps['compound'] <= - 0.05 :
                sentiment="☹️ Negative"
                value=ps['compound']
                count=1
            else :
                sentiment="😐 Neutral"
                value=ps['compound']
                count=1
            
            tweetsWithSent.append([text,sentiment,value,count])
        print(tweetsWithSent)
        tweetsWithSent_df=pd.DataFrame(tweetsWithSent,columns=['Tweets','Sentiment','value','count'])


        # sentiment_scores(tweets_df2['Tweets'][7])
        col1, col2, col3 = st.columns(3)
        if col2.button('Analyse twitter user'):
            # if st.checkbox('show tweets1'):
                st.write(tweetsWithSent_df.head(10))
            # if st.checkbox('show visualization1'):
                draw=px.bar(tweetsWithSent_df,x='Sentiment',y='count',color='Sentiment',title='Sentiment graph of user tweets',hover_data=['value'])
                st.plotly_chart(draw, use_container_width=True)

    
    
    


    
# st.title('Twitter sentimental analysis')
# st.subheader('Topic/Hashtag analyser')
# sentence = st.text_input('Enter Topic/Hashtag','War in ukraine')


# attributes_container = []

# for i,tweet in enumerate(sntwitter.TwitterSearchScraper(sentence).get_items()):
#     if i>300:
#         break
#     attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent, tweet.lang])
    
# tweets_df1 = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets","Tweet_lang"])
# tweets_df=tweets_df1[tweets_df1["Tweet_lang"]=="en"]
# print(tweets_df)




# def sentiment_scores(sentence):

	
# 	sid_obj = SentimentIntensityAnalyzer()

# 	sentiment_dict = sid_obj.polarity_scores(sentence)

# 	print(sentiment_dict)

	
# 	if sentiment_dict['compound'] >= 0.05 :
# 		st.write("🙂 Positive")

# 	elif sentiment_dict['compound'] <= - 0.05 :
# 		st.write("☹️ Negative")

# 	else :
# 		st.write("😐 Neutral")



# analyzer1=SentimentIntensityAnalyzer()    
# tweetsWithSent1 = []
# tweetss=tweets_df['Tweets']
# for i in range(100):
#     if i>100:
#         break   
#     text1 = (tweetss[i])
#     ps = analyzer1.polarity_scores(text1)
#     if ps['compound'] >= 0.05 :
#         sentiment="🙂 Positive"
#         value=ps['compound']

#     elif ps['compound'] <= - 0.05 :
#         sentiment="☹️ Negative"
#         value=ps['compound']
#     else :
#         sentiment="😐 Neutral"
#         value=ps['compound']
    
#     tweetsWithSent1.append([text1,sentiment,value])
# print(tweetsWithSent1)
# tweetsWithSent_df1=pd.DataFrame(tweetsWithSent1,columns=['Tweets','Sentiment','value'])

# print(tweetsWithSent_df1['Sentiment'].value_counts()['🙂 Positive'])
# print(tweetsWithSent_df1['Sentiment'].value_counts()['☹️ Negative'])
# print(tweetsWithSent_df1['Sentiment'].value_counts()['😐 Neutral'])


# sentiment_scores(sentence)
# if st.checkbox('show tweets'):
#     st.write(tweets_df.head(10))
    
    

# st.subheader('User profile analyser')

# username=st.text_input('Enter username','I_am_prathik')

# attributes_container1=[]
# for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:${username}').get_items()):
#     if i>100:
#         break
#     attributes_container1.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent, tweet.lang,tweet.hashtags])
        
# tweets_df2 = pd.DataFrame(attributes_container1, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets","Tweet_lang","Hashtags"])
    
# print(tweets_df2)
# tweets=tweets_df2['Tweets']
# analyzer=SentimentIntensityAnalyzer()    
# tweetsWithSent = []
# for i in range(100):
#     if i>100:
#         break   
#     text = (tweets[i])
#     ps = analyzer.polarity_scores(text)
#     if ps['compound'] >= 0.05 :
#         sentiment="🙂 Positive"
#         value=ps['compound']

#     elif ps['compound'] <= - 0.05 :
#         sentiment="☹️ Negative"
#         value=ps['compound']
#     else :
#         sentiment="😐 Neutral"
#         value=ps['compound']
    
#     tweetsWithSent.append([text,sentiment,value])
# print(tweetsWithSent)
# tweetsWithSent_df=pd.DataFrame(tweetsWithSent,columns=['Tweets','Sentiment','value'])

# print(tweetsWithSent_df['Sentiment'].value_counts()['🙂 Positive'])
# print(tweetsWithSent_df['Sentiment'].value_counts()['☹️ Negative'])
# print(tweetsWithSent_df['Sentiment'].value_counts()['😐 Neutral'])



# sentiment_scores(tweets_df2['Tweets'][7])
# if st.checkbox('show tweets1'):
#     st.write(tweetsWithSent_df.head(10))

# tweetsWithSent_df.plot.bar(figsize=(15,5),width=1)

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
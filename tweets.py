import snscrape.modules.twitter as sntwitter
import pandas as pd
attributes_container1=[]
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('war in russia').get_items()):
    if i==30:
        break
    attributes_container1.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent, tweet.lang])
                
tweets_df2 = pd.DataFrame(attributes_container1, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets","Tweet_lang"])
            
print(tweets_df2)
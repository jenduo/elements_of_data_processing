import os
import json
import pandas as pd
import matplotlib.pyplot as plt 

def task5():
    #Opening our reviews file and extracting it into a dataframe
    folder = '/course/data/a1/'
    reviews_df = pd.read_json(folder +'reviews/HealthStory.json')

    #Opening our tweets file
    with open(folder + 'engagements/HealthStory.json') as json_file:
        tweet_json = json.load(json_file)
    
    #Creating rows for tweets dataframe
    df_rows = []

    #Looping through each article 
    for news_id in tweet_json:
        #finding the rating from the news id 
        rating = reviews_df.loc[reviews_df['news_id'] == news_id]['rating'].item()

        #Finding all unique tweets
        set_t = set()
        for tweets in tweet_json[news_id]["tweets"]:
            set_t.add(tweets)
        for tweets in tweet_json[news_id]["retweets"]:
            set_t.add(tweets)

        #Totaling the unique tweets
        total_tweets = len(set_t)

        #Appending this to our rows
        df_rows.append({
            'news_id':news_id,
            'rating':rating,
            'total_tweets':total_tweets
        })

    #Creating our dataframe
    df = pd.DataFrame(df_rows)

    #Our x values for our graph is all the ratings
    #ratings are all integers from 0 to 5
    x =[0,1,2,3,4,5]

    #Loop through all our x values
    #For every news id with x rating, find the mean of the tweets
    y =[df.loc[df['rating']==r]['total_tweets'].mean() for r in x]

    #Plot our bar graph
    plt.bar(x, y)

    #Naming our Axis and Title
    plt.xlabel('Rating')
    plt.ylabel('Average Number of tweets')
    plt.title('A bar graph showing Average Number of Tweets per each Rating group')

    #Saving our graph
    plt.savefig('task5.png')
    plt.show()
    plt.close()



    return

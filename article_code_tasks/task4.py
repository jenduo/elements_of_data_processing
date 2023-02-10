import os
import json
import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt 


def task4():
    #Opening our reviews file as a dataframe
    folder = '/course/data/a1/'
    articles_df = pd.read_json (folder + 'reviews/HealthStory.json')

    #Creating a series of number of articles
    num_articles_df = articles_df.groupby('news_source').size()

    #Creating a series of average rating of each sourse
    avg_rating_df=articles_df.groupby('news_source')['rating'].mean()

    #Making the credibility dataframe
    #This is done by concating the number of articles and the average rating for dataframe for each Source
    creds_df = pd.concat([num_articles_df,avg_rating_df], 
                    axis = 1, keys=["num_articles", "avg_rating"])

    #Removing the count with no news_source
    creds_df = creds_df.iloc[1: , :]

    #Saving new dataframe as a csv file
    creds_df.to_csv('task4a.csv')

    #Filtering news sources with at least 5 articles
    creds_graph_df = creds_df[creds_df.num_articles >= 5]

    #Plotting our graph
    x = creds_graph_df.index
    y = creds_graph_df['avg_rating']

    #Making our min and max different colours so that we can see it
    pallete = []
    for p in y:
        if (p==min(y)):
            pallete.append('red')
        elif (p==max(y)):
            pallete.append('green')
        else:
            pallete.append('blue')

    #Resizing our window to make sure it is readable
    plt.rcParams["figure.autolayout"] = True
    plt.figure(figsize=(8,6))

    #Plotting our graph
    plt.bar(x,y, color = pallete)

    #Rotating our x varibles because news_sources have very long names
    plt.xticks(rotation=90)

    #Naming our axis and title
    plt.xlabel('News Source')
    plt.ylabel('Average Rating')
    plt.title('A bar graph showing the Average Rating of each News Source')

    #Saving our graph
    plt.savefig('task4b.png')
    plt.show()
    plt.close()

    return

import os
import json

def task1():
    
    folder = '/course/data/a1/'
    
    #Making a list of all the file names of the articles
    list = os.listdir(folder + 'content/HealthStory')
    #Counting the number of articles
    no_article = len(list)

    #Opening the json file of the reviews
    with open(folder + 'reviews/HealthStory.json') as json_file:
        review_json = json.load(json_file)
    #Counting the number of reviews
    no_review = len(review_json)

    #Opening the tweets json file
    with open(folder + 'engagements/HealthStory.json') as json_file:
        tweet_json = json.load(json_file)

    #A unique tweet is every unique ID in each tweet, reply, retweet
    set_t = set()
    for articles in tweet_json:
        for tweets in tweet_json[articles]["tweets"]:
            set_t.add(tweets)
        for tweets in tweet_json[articles]["replies"]:
            set_t.add(tweets)
        for tweets in tweet_json[articles]["retweets"]:
            set_t.add(tweets)
    #Counting the number of unique tweets
    no_tweet = len(set_t)
    
    #Writing the data for our file
    data = {
        "Total number of articles": no_article,
        "Total number of reviews": no_review,
        "Total number of tweets": no_tweet
    }

    #Exporting our file to a json file
    with open("task1.json", "w") as fp:
        json.dump(data,fp,indent = 2)
    
    return

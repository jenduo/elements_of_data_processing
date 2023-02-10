import os
import csv
import json
import pandas as pd
import math
import matplotlib.pyplot as plt 

def task7():
    #Opening our reviews file and extracting as a dataframe
    folder = '/course/data/a1/'
    df = pd.read_json (folder + 'reviews/HealthStory.json')

    #Cutting our dataframe to only have news_id and rating
    df = df[['news_id', 'rating']]

    #Making a list of real and Fake Articles
    #real articles have a rating of 3 and above 
    real = list(df[df['rating']>=3]['news_id'])
    #fake articles have a rating below 3
    fake =list(df[df['rating']<3]['news_id'])

    #Counting the total number of real and fake articles
    num_real = len(real)
    num_fake = len(fake)

    #counting the totable of number of articles
    all_articles = num_fake + num_real

    #Creating an empty data frame 
    words_odds_df_rows = []

    #Opening our task6 file
    with open('task6.json') as json_file:
        words_json = json.load(json_file)

    #Looping through every word in our task6 file
    for word in words_json:

        #For every word, we count the number of real and fake articles
        #We check each article to see if it is in real or fake
        real_articles_with_word = len([w for w in words_json[word] if (w in real)])
        fake_articles_with_word = len([w for w in words_json[word] if (w in fake)])

        #This is the total articles it in
        tot_articles = len(words_json[word])

        #If the total articles is below 10, or if it is in all articles, we exclude it
        if(tot_articles < 10 or tot_articles == all_articles):
            continue
        
        #Calculating the probability if it is real or fake
        prob_real = real_articles_with_word/num_real
        prob_fake = fake_articles_with_word/num_fake

        #We discard all words will give us odds of 0 or inifinity
        if(prob_real == 0 or prob_real == 1):
            continue

        if(prob_fake == 0 or prob_fake == 1):
            continue
        
        #Calculating our odds
        odds_real = prob_real/(1-prob_real)
        odds_fake = prob_fake/(1-prob_fake)

        #Calulating our odds ratio
        odds_ratio = odds_fake/odds_real

        #Calculating our log oddds ratio
        log_odds_ratio = round(math.log10(odds_ratio), 5)

        #Appending our information to each row
        words_odds_df_rows.append({
            'word':word,
            'odds_ratio':odds_ratio,
            'log_odds_ratio':log_odds_ratio
        })
    #Creating a Dataframe
    words_odds_df = pd.DataFrame(words_odds_df_rows)

    #Creating a Dataframe with only the word and the log odds ratio
    #Saving it as a CSV file
    log_odds_ratio_df = words_odds_df[['word','log_odds_ratio']]
    log_odds_ratio_df.to_csv('task7a.csv', index= False)

    #Drawing graph 7B
    #Since we are drawing a Histogram we only need all the log odds ratio
    x = list(log_odds_ratio_df['log_odds_ratio'])

    #Choosing a bin of 25 so our data is readable
    plt.hist(x, bins=25)

    #Labeling our axis and title
    plt.xlabel('Log Odds Ratio')
    plt.ylabel('Frequency')
    plt.title('A Histogram showing distribution of Log Odds Ratio for all Words')

    #Saving it
    plt.savefig('task7b.png')
    plt.show()
    plt.close()

    #Drawing graph 7c

    #Sorting our values by the Odds Ratio
    words_odds_df = words_odds_df.sort_values(by='odds_ratio')

    #Cutting our lowest and highest 15 odds ratio
    low = words_odds_df.head(15)
    high = words_odds_df.tail(15)

    #Resizing our window to make sure it is readable
    plt.rcParams["figure.autolayout"] = True
    plt.figure(figsize=(8,6))

    #Declaring the first graph
    plt.subplot(1, 2, 1)

    #Drawing our lowest oddds bar graph
    plt.bar(low['word'], low['odds_ratio'])
    plt.xticks(rotation=90)
    plt.title("Top 15 (most likely) Real Words")
    plt.xlabel('Word')
    plt.ylabel('Odds Ratio')

    #Declaring our second graph
    plt.subplot(1, 2, 2)

    #Drawing our highest odds bar graph
    plt.bar(high['word'], high["odds_ratio"])
    plt.title("Top 15 (most likely) Fake Words")
    plt.xlabel('Word')
    plt.ylabel('Odds Ratio')

    #Rotating the words so that they are readable
    plt.xticks(rotation=90)

    #Saving our image
    plt.savefig('task7c.png')
    plt.show()
    plt.close()

    return

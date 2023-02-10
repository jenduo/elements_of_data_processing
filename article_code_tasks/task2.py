import os
import json
import csv
import pandas as pd

def task2():

    #Opening the reviews file
    folder = '/course/data/a1/'
    with open(folder + 'reviews/HealthStory.json') as json_file:
        review_json = json.load(json_file)
    
    #Sorting it by news id
    review_json = sorted(review_json, key=lambda x:x['news_id'])

    #Initializing our rows for our aggregated data frame
    agg_df_rows = []

    #Going through each review in our json file
    for review in review_json:

        #aggregating our data to our new column names
        news_id = review['news_id']
        news_title = review['original_title']
        review_title = review['title']
        rating = review['rating']

        #Counting the number of answers that are satisfactor in each review
        num_satisfactory = len([c for c in review['criteria'] if c['answer'] == 'Satisfactory'])

        #append our information to a row
        agg_df_rows.append({
            'news_id': news_id,
            'news_title': news_title,
            'review_title': review_title,
            'rating': rating,
            'num_satisfactory': num_satisfactory
        })
    
    #Turning this into a dataframe an exporting it as a csv file
    agg_df=pd.DataFrame(agg_df_rows)
    agg_df.to_csv('task2.csv',index=False)
    return

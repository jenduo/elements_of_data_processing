import os
import json
import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt 

def task3():
    #Making a list of article file names
    folder = '/course/data/a1/'
    news_id_files = os.listdir(folder + 'content/HealthStory')
    
    #Sorting the file names in ascesding order
    news_id_files = sorted(news_id_files)

    #Creating an empty list of rows for our data frame
    metadata_df_rows = []
    
    #Opening each file
    for a in news_id_files:
        with open(folder + 'content/HealthStory/'+ a) as json_file:
            article_json = json.load(json_file)

        #The news id is the file name without the .json
        news_id = a[0:-5]

        #Extracting the publish_date
        publish_date = article_json['publish_date']

        #If the publish date exist we convert it
        if(publish_date!=None):
            publish_date = datetime.datetime.fromtimestamp(publish_date)

            #Seperating the year, month and day and formatting them
            year=publish_date.year
            month='{:02d}'.format(publish_date.month)
            day='{:02d}'.format(publish_date.day)

            #Append our infortmation to the rows
            metadata_df_rows.append({
                'news_id':news_id,
                'year':year,
                'month':month,
                'day':day
            })

    #Making a data frame and exporting it as a CSV file
    #Since we dont need the index, we dont include it in our file
    metadata_df = pd.DataFrame(metadata_df_rows)
    metadata_df.to_csv('task3a.csv', index=False)

    #Making a new data frame of the Year vs the Freqeuncy of articles published
    metadata_graph_df=metadata_df.groupby('year').size().reset_index(name='freq')

    #Plotting the graph

    #Extracting the right columns for our x and y axis
    x = metadata_graph_df['year']
    y = metadata_graph_df['freq']

    #Ploting our graph and naming our axis and title
    plt.plot(x, y)
    plt.xlabel('Year')
    plt.ylabel('Number of Articles')
    plt.title('A line graph showing the Number of Articles published per Year')
    
    #Saving the graph
    plt.savefig('task3b.png')
    plt.show()
    plt.close()

    return

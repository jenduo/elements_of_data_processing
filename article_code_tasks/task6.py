import re
import nltk
import os
import json
from nltk.corpus import stopwords
import pandas as pd

#Defining a way to process the text
def process(text):

    #Replacing all characters that arent letters as a space
    #this also removes spacing characters, tabs and newlines
    text = re.sub(r'[^a-zA-Z]+'," ", text)

    #Making all the text lowercased
    text = text.lower()

    #Spliting the text into tokens based on a whitespace delimiter
    tokens = text.split(" ")

    #Creating all english stopwords
    stop_words = set(stopwords.words('english'))

    #Removing all the stop_words and words with only 1 letter
    no_stopwords = [w for w in tokens if ((w not in stop_words) and (len(w) >1))]

    #Returning a list of the set of no_stopwords
    return list(set(no_stopwords))

def task6():
    #Opening our directory and listing each filename
    folder = '/course/data/a1/content/HealthStory/'
    news_id_files = os.listdir(folder)

    #Sorting our filenames in order of the ID
    news_id_files = sorted(news_id_files)

    #Initilizing a dictionary for our words: [articles]
    unsorted_dict = {}
    
    #Opening each article
    for a in news_id_files:
        #Our news id is the article filename without the .json
        news_id = a[0:-5]
        with open(folder+a) as fp:
            #loading the text part of each article
            text = json.load(fp)['text']

            #Converting the text into a string and processing it
            text = process(str(text))
        
        #Looping through every word in the text
        for word in text:

            #If the word is our dictionary append it
            if word in unsorted_dict:
                unsorted_dict[word].append(news_id)
                continue
            #If the word isn't in our dictionary, create one
            #the first article in the list is this one
            unsorted_dict[word]=[news_id]

    #Sorting our words in alphabetical order
    dict_keys = sorted(unsorted_dict.keys())
    sorted_dict = {word:unsorted_dict[word] for word in dict_keys}

    #Saving our dictionary as a json file
    with open('task6.json', 'w') as fp:
        json.dump(sorted_dict, fp)

    return

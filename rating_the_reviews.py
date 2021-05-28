#!/usr/bin/env python
# coding: utf-8

# Categorizing positive and Negative Reviews on OpinRank Review Dataset

# In[21]:


#changing data from tag format into csv data

#import BeautifulSoup package

from bs4 import BeautifulSoup


# In[22]:


#data file to load the data
data_file = "2009_audi_/2009_audi_a5"
#csv file to convert data in tag format into csv format
csv_file = "2009_audi_/2009_audi_a5.csv"


# In[23]:


#loading data from the data file in text format
with open(data_file) as txt_file:
    data = txt_file.read()
#data


# In[24]:


#using Beautiful soup to get the data into html format
soup = BeautifulSoup(data, 'lxml')
#print("\nFind and print all the tags:\n")
#print(soup)

#taking list to load the data into csv format
csv_data = []
#headers for the csv format
csv_data.append(["date","author","text","favorite"])
#finding and printing the data of "doc" format
for doc_tag in soup.find_all("doc"):
    #print(doc_tag)
    #loading data in list to append the cummulated data to upper list
    raw_data = []
    #getting each values for a respective doc tag
    raw_data.append(doc_tag.find("date").text)
    raw_data.append(doc_tag.find("author").text)
    raw_data.append(doc_tag.find("text").text)
    raw_data.append(doc_tag.find("favorite").text)
    csv_data.append(raw_data)
#data in list of lists format
#csv_data


# In[25]:


import csv

#function to convert list of lists to csv format
def write_csv(file,data):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


# In[26]:


#loading the data into csv format
write_csv(csv_file,csv_data)


# In[12]:


import pandas as pd


# In[27]:


#loading the csv data into dataframe
df = pd.read_csv(csv_file)
df.head(5)


# In[15]:


#Using nltk to load the sentiment analyzer
import nltk
nltk.download('vader_lexicon')


# In[28]:


#lower and upper thresholds
threshold_lower = 0.4
threshold_upper = 0.85


# In[31]:


#using sentiment analyzer of nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#loading sentiment Analyzer
sid = SentimentIntensityAnalyzer()

#storing scores and rating
scores = []
rating = []

#iterating every review
for i in df["text"]:
    #print(i)
    #calculating the sentiment score and comparing threshold
    if sid.polarity_scores(i)["compound"] < threshold_lower:
        rating.append("Negative")
    elif sid.polarity_scores(i)["compound"] < threshold_upper:
        rating.append("Neutral")
        #print(sid.polarity_scores(i)["compound"])
    else:
        rating.append("Positive")
        #print(sid.polarity_scores(i)["compound"])
    #appending scores
    scores.append(sid.polarity_scores(i)["compound"])
    #print()
#print(scores)

#loading rating score and rating to dataframe
df["rating_score"] = scores
df["rating"] = rating
df.head(10)


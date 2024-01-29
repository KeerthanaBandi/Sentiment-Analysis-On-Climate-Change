#!/usr/bin/env python
# coding: utf-8

# ### Finding the subreddits which are related to climate change

# In[1]:


import praw
import csv
import time

# Set up the Reddit API
user_agent = 'MyApp/1.0 by climate change'
reddit = praw.Reddit(
    client_id = '4xIYX_X2iMiwGhP4aZtE2g',
    client_secret = 'xLymU0PVKlmS3cofzsEKG1fvsiWyrw',
    user_agent = user_agent
)

keywords = ['Global warming', 'Climate change']

# Search for subreddits related to the keywords
subreddits = []
for sr in reddit.subreddits.search(' OR '.join(keywords),limit = 10):
    subreddits.append(sr.display_name)

print(subreddits)


# ### Used PRAW to scrape the data from the subreddits and keywords

# In[2]:


import praw
import csv
import time

# Set up the Reddit API
user_agent = 'MyApp/1.0 by climate change'
reddit = praw.Reddit(
    client_id = '4xIYX_X2iMiwGhP4aZtE2g',
    client_secret = 'xLymU0PVKlmS3cofzsEKG1fvsiWyrw',
    user_agent = user_agent
)

# Define the subreddits and search keywords
subreddits = ["climatechange","globalwarming","climate", "environment","climate_science","climateskeptics","ClimateOffensive"]
keywords = ["climate change OR global warming"]

# Define the start and end dates
start_date = "2018-01-01"
end_date = "2022-12-31"

# Convert the dates to Unix timestamps
start_time = int(time.mktime(time.strptime(start_date, '%Y-%m-%d')))
end_time = int(time.mktime(time.strptime(end_date, '%Y-%m-%d'))) 

# Create a list to store the posts
posts_list = []

# Loop through each subreddit
for subreddit in subreddits:
    # Search for the posts that match the keywords within the date range
    for post in reddit.subreddit(subreddit).search(query=" OR ".join(keywords), time_filter='all', limit=None):
        if start_time <= post.created_utc <= end_time:
            # Add the post to the list
            posts_list.append([post.title, post.author.name if post.author else 'N/A', post.created_utc, post.ups, subreddit])

# Write the posts to a CSV file
with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile, delimiter=',')

    # Write headers for each column
    writer.writerow(['title', 'username', 'date', 'upvotes', 'subreddit'])

    # Write data for each post
    for post in posts_list:
        writer.writerow([post[0], post[1], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(post[2])), post[3], post[4]])


# ### Preprocessing - Removed lowercase, URL's and punctuations for better analysis

# In[3]:


import csv
import re
import string

# Open the posts.csv file and create a CSV reader object
with open('posts.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(reader)

    # Create a set to store the unique post titles
    titles_set = set()

    # Create a list to store the preprocessed posts
    preprocessed_posts_list = []

    # Loop through each row in the CSV file
    for row in reader:
        # Get the post title from the row
        title = row[0]

        # Preprocess the post title
        title = title.lower() # convert to lowercase
        title = re.sub(r'http\S+', '', title) # remove URLs
        #title = re.sub(r'[^\w\s]', '', title) # remove punctuations

        # Check if the preprocessed title contains any of the keywords
        if "climate change" in title or "global warming" in title:
            # Check if the title is already in the set
            if title not in titles_set:
                # Add the title to the set
                titles_set.add(title)
                # Add the preprocessed post to the list
                preprocessed_posts_list.append([title, row[1], row[2], row[3], row[4]])

# Write the preprocessed posts to a new CSV file
with open('preprocessed_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile, delimiter=',')

    # Write headers for each column
    writer.writerow(['title', 'username', 'date', 'upvotes', 'subreddit'])

    # Write data for each preprocessed post
    for post in preprocessed_posts_list:
        writer.writerow([post[0], post[1], post[2], post[3], post[4]])


# ### Displaying the first few rows of the data

# In[4]:


import pandas as pd

# Loading the CSV file
csv_file = 'preprocessed_posts.csv'
df = pd.read_csv(csv_file)

# Displaying the first five rows of the data
print(df.head())

print(df.describe())


# In[5]:


import nltk
nltk.download('vader_lexicon')


# ### Sentiment Analysis using Vader

# In[6]:


import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

# Load the preprocessed posts from the CSV file
df = pd.read_csv('preprocessed_posts.csv')

# Initialize the Vader sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Apply Vader sentiment analysis to each post
sentiment_scores = []
for post in df['title']:
    # Calculate the sentiment scores
    scores = analyzer.polarity_scores(post)
    sentiment_scores.append(scores)

# Add the sentiment scores to the DataFrame
df = pd.concat([df, pd.DataFrame(sentiment_scores)], axis=1)

# Categorize the compound score
df['sentiment'] = df['compound'].apply(lambda score: 'positive' if score > 0 else ('negative' if score < 0 else 'neutral'))

# Rename the columns
df = df.rename(columns={'neg': 'negative', 'neu': 'neutral', 'pos': 'positive', 'compound': 'compound_score'})

# Save the DataFrame to a CSV file
df.to_csv('vader.csv', index=False)


# ### Sentiment Analysis using Textblob

# In[7]:


# Importing the required libraries
from textblob import TextBlob
import pandas as pd

# Reading the input file into a pandas dataframe
df = pd.read_csv('preprocessed_posts.csv')

# Defining a function to get the sentiment score of each post using TextBlob
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

# Applying the function to each post in the dataframe
df['Sentiment Score'] = df['title'].apply(get_sentiment)

# Creating a new column to categorize the sentiment scores as positive, negative or neutral
df['Sentiment'] = df['Sentiment Score'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

# Writing the updated dataframe to the output file
df.to_csv('textblob.csv', index=False)


# In[ ]:





# In[ ]:





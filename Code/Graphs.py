#!/usr/bin/env python
# coding: utf-8

# ### PIE chart representation of polarity score distribution using Vader

# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns
labels = ['Positive', 'Negative', 'Neutral']
values = [312, 211, 50]
colors = sns.color_palette('pastel')[0:3]
fig, ax = plt.subplots()
ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')
ax.set_title('Sentiment Analysis - VADER')
plt.show()


# ### PIE chart representation of polarity score distribution using Textblob

# Sentiment	Count of Sentiment
# Neutral	236
# Positive	222
# Negative	120
# Grand Total	578

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
labels = ['Positive', 'Negative', 'Neutral']
values = [219, 120, 234]
colors = sns.color_palette('pastel')[0:3]
fig, ax = plt.subplots()
ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')
ax.set_title('Sentiment Analysis - TextBlob')
plt.show()


# ### Sentiment polarity distribution per year - Vader

# In[11]:


import pandas as pd

# Load your sentiment data into a pandas dataframe
df = pd.read_csv('vader.csv')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Create a function to count the number of sentiment values by year
def count_sentiment_by_year(df, year):
    year_df = df[df['date'].dt.year == year]  # Filter by year
    counts = year_df['sentiment'].value_counts()  # Count sentiment values
    return counts

# Loop through each year and count the sentiment values
years = df['date'].dt.year.unique()
for year in years:
    counts = count_sentiment_by_year(df, year)
    print(f"Sentiment counts for year {year}:")
    print(counts)


# In[12]:


import matplotlib.pyplot as plt
import pandas as pd

# Load the data from a CSV file
df = pd.read_csv('vader.csv')

# Extract the year from the timestamp column
df['year'] = pd.to_datetime(df['date']).dt.year

# Group the data by year and sentiment polarity, and count the number of posts in each group
df_grouped = df.groupby(['year', 'sentiment']).size().reset_index(name='count')

# Pivot the data to have the sentiment polarity as columns and the year as rows
df_pivot = df_grouped.pivot(index='year', columns='sentiment', values='count')

# Plot the bar chart
df_pivot.plot(kind='bar', stacked=True)
plt.title('Sentiment polarity distribution per year - Vader')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# ### Sentiment polarity distribution per year - Textblob

# In[13]:


import pandas as pd

# Load your sentiment data into a pandas dataframe
df = pd.read_csv('textblob.csv')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Create a function to count the number of sentiment values by year
def count_sentiment_by_year(df, year):
    year_df = df[df['date'].dt.year == year]  # Filter by year
    counts = year_df['Sentiment'].value_counts()  # Count sentiment values
    return counts

# Loop through each year and count the sentiment values
years = df['date'].dt.year.unique()
for year in years:
    counts = count_sentiment_by_year(df, year)
    print(f"Sentiment counts for year {year}:")
    print(counts)


# In[14]:


import matplotlib.pyplot as plt
import pandas as pd

# Load the data from a CSV file
df = pd.read_csv('textblob.csv')

# Extract the year from the timestamp column
df['year'] = pd.to_datetime(df['date']).dt.year

# Group the data by year and sentiment polarity, and count the number of posts in each group
df_grouped = df.groupby(['year', 'Sentiment']).size().reset_index(name='count')

# Pivot the data to have the sentiment polarity as columns and the year as rows
df_pivot = df_grouped.pivot(index='year', columns='Sentiment', values='count')

# Plot the bar chart
df_pivot.plot(kind='bar', stacked=True)
plt.title('Sentiment polarity distribution per year - TextBlob')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


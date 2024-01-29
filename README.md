**Read Me File: "Public Sentiment towards Climate Change on Reddit" (Spring'23)**

---

### Research Overview:

This study, aims to explore public sentiments towards climate change by conducting a sentiment analysis on posts and subreddits related to climate change on Reddit.

### Research Question:

How do public sentiments towards climate change differ across various subreddits, posts, and comments related to climate change on Reddit?

### Background:

Climate change is a critical global issue prompting discussions on social media platforms like Reddit. The proposal seeks to analyze Reddit posts and comments to understand public opinions and sentiments on climate change. The urgency to address climate change and the need for policy changes underscore the importance of gauging public sentiment (Sham, N. M., & Mohamed, A. H., 2022).

### Data:

- Data will be collected using Python and PRAW (Python Reddit API Wrapper) to scrape at least 500 data points related to climate change discussions.
- Focus on relevant subreddits like r/ClimateChange, r/GlobalWarming, and r/Environment, ensuring minimal spam activity.
- Data preprocessing involves removing irrelevant words and spam, using NLP techniques for tokenizing and stemming.

### Method:

- Cleaned data will undergo Natural Language Processing (NLP) techniques, including stop word removal and tokenization.
- VADER tool will be employed to assess the sentiment of comments (positive, negative, or neutral) based on tone, providing a score between -1 and +1.
- EMPATH Python library will categorize emotional content into specific topics for deeper sentiment analysis.
- Results will be visualized using various plots like bar charts to identify sentiment distribution.

### References:

1. Sham, N. M., & Mohamed, A. H. (2022). Climate Change Sentiment Analysis Using Lexicon, Machine Learning and Hybrid Approaches. Sustainability, 14(8), 4723. DOI: 10.3390/su14084723
2. Treen, K., Williams, H., O'Neill, S., & Coan, T. G. (2022). Discussion of Climate Change on Reddit: Polarized Discourse or Deliberative Debate?. Environmental Communication, 16(5), 680-698. DOI: 10.1080/17524032.2022.2050776

#!/usr/bin/env python
# coding: utf-8

# [Streaming With Tweepy](http://docs.tweepy.org/en/latest/streaming_how_to.html)

# In[3]:


get_ipython().system('pip install tweepy')


# In[4]:


#Slistener
import tweepy
from tweepy.streaming import StreamListener
import time

class SListener(StreamListener):
    def__init__(self, api = None):
        self.output = open('tweets_%s.json %
            time.strftime('%Y%m%d-%H%M%S'), 'w'')
                           self.api or API()


# In[9]:


#tweepy authentication
from tweepy import OAuthHandler
from tweepy import API
auth = OAuthHandler(consumer_Key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


# In[ ]:


# Collecting data with tweepy
from tweepy import Stream
listen = SListener(api)
stream = Stream(auth, listen)
stream.sample()


# In[10]:


# Collecting data on keywords
from tweepy import Stream

# Set up words to track
keywords_to_track = ['#rstats', '#python']

# Instantiate the SListener object 
listen = SListener(api)

# Instantiate the Stream object
stream = Stream(auth, listen)

# Begin collecting data
stream.filter(track = keywords_to_track)


# # Understanding Twitter JSON

# In[ ]:


# Contents of Twitter JSON
{
    "created_at": "Thu Apr 19 14:25:04 +0000 2018",
    "id": 986973961295720449,
    "id_str": "986973961295720449",
    "text": "Writing out the script of my @DataCamp class
        and I can't help but mentally read it back to myself in
        @hugobownes voice.",
    "retweet_count": 0,
    "favorite_count": 1,
}


# In[ ]:


{
    "user": {
        "id": 661613,
        "name":"Alex Hanna", "Data Witch",
        "screen_name": "alexhanna",
        "location": "Toronto, ON",
        ...
    }
}


# In[ ]:


import json
tweet_json = open('tweet-example.json', 'r').read()
tweet = json.loads(tweet_json)
tweet['text']


# In[ ]:


# Child tweet JSON
tweet['user']['screen_name']
tweet['user']['name']
twet['user']['created_at']


# In[ ]:


# Load JSON
import json

# Convert from JSON to Python object
tweet = json.loads(tweet_json)

# Print tweet text
print(tweet['text'])

# Print tweet id
print(tweet['id'])


# In[ ]:


# Print user handle
print(tweet['user']['screen_name'])

# Print user follower count
print(tweet['user']['followers_count'])

# Print user location
print(tweet['user']['location'])

# Print user description
print(tweet['user']['description'])


# In[11]:


# Print the text of the tweet
print(rt['text'])

# Print the text of tweet which has been retweeted
print(rt['retweeted_status']['text'])

# Print the user handle of the tweet
print(rt['user']['screen_name'])

# Print the user handle of the tweet which has been retweeted
print(rt['retweeted_status']['user']['screen_name'])


# In[ ]:


# Text in Twitter JSON
tweet_json = open('tweet-example.json', 'r').read()
tweet = json.loads(tweet_json)
tweet['text']
tweet['extended_tweet']['full_text']
tweet['quoted_status']['extended_tweet']['full_text']

# Text user information
tweet['user']['descrition']
tweet['user']['location']

#Flattening Twitter JSON
extended_tweet['extended_tweet-ull_text'] =
    extended_tweet['extended_tweet']['full_text']
    
tweet_list = []
with open('all_tweets.json', 'r') as fh:
    tweets_json = fh.read().split('\n')
    
    for tweet in tweets_json:
        tweet_obj = json.loads(tweet)
        
        if 'extended_tweet' in tweet_obj:
            tweet_obj['extended_tweet-full_text'] =
                tweet_obj['extendend_tweet']['full_text']
        ...
    tweet_list.append(tweet)
    
tweets = pd.DataFrame(tweet_list)


# In[ ]:


# Print the tweet text
print(quoted_tweet['text'])

# Print the quoted tweet text
print(quoted_tweet['quoted_status']['text'])

# Print the quoted tweet's extended (140+) text
print(quoted_tweet['quoted_status']['extended_tweet']['full_text'])

# Print the quoted user location
print(quoted_tweet['quoted_status']['user']['location'])


# In[ ]:


# Store the user screen_name in 'user-screen_name'
quoted_tweet['user-screen_name'] = quoted_tweet['user']['screen_name']

# Store the quoted_status text in 'quoted_status-text'
quoted_tweet['quoted_status-text'] = quoted_tweet['quoted_status']['text']

# Store the quoted tweet's extended (140+) text in 
# 'quoted_status-extended_tweet-full_text'
quoted_tweet['quoted_status-extended_tweet-full_text'] = quoted_tweet['quoted_status']['extended_tweet']['full_text']


# In[ ]:


# A tweet flattening function
def flatten_tweets(tweets_json):
    """ Flattens out tweet dictionaries so relevant JSON
        is in a top-level dictionary."""
    tweets_list = []
    
    # Iterate through each tweet
    for tweet in tweets_json:
        tweet_obj = json.loads(tweet)
    
        # Store the user screen name in 'user-screen_name'
        tweet_obj['user-screen_name'] = tweet_obj['user']['screen_name']
    
        # Check if this is a 140+ character tweet
        if 'extended_tweet' in tweet_obj:
            # Store the extended tweet text in 'extended_tweet-full_text'
            tweet_obj['extended_tweet-full_text'] = tweet_obj['extended_tweet']['full_text']
    
        if 'retweeted_status' in tweet_obj:
            # Store the retweet user screen name in 'retweeted_status-user-screen_name'
            tweet_obj['retweeted_status-user-screen_name'] = tweet_obj['retweeted_status']['user']['screen_name']

            # Store the retweet text in 'retweeted_status-text'
            tweet_obj['retweeted_status-text'] = tweet_obj['retweeted_status']['text']
            
        tweets_list.append(tweet_obj)
    return tweets_list


# In[ ]:


# Loading tweets into a DataFrame
# Import pandas
import pandas as pd

# Flatten the tweets and store in `tweets`
tweets = flatten_tweets(data_science_json)

# Create a DataFrame from `tweets`
ds_tweets = pd.DataFrame(tweets)

# Print out the first 5 tweets from this dataset
print(ds_tweets['text'].values[0:5])


# In[ ]:


# Counting words
import pandas as pd
tweets = pd.DataFrame(flatten_tweets(companies_json))
apple = tweets['text'].str.contains('apple', case = False)
print(np.sum(apple) / tweets.shape[0])

# Counting in multiple text fields
apple = tweets['text'].str.contains('apple', case = False)

for column in ['extended_tweet-full_text',
  'retweeted_status-text',
  'retweeted_status-extended_tweet-full_text']:
 apple = apple | tweets[column].str.contains('apple', case = False)

print(np.sum(apple) / tweets.shape[0])


# In[ ]:


# Finding keywords
# Flatten the tweets and store them
flat_tweets = flatten_tweets(data_science_json)

# Convert to DataFrame
ds_tweets = pd.DataFrame(flat_tweets)

# Find mentions of #python in 'text'
python = ds_tweets['text'].str.contains('#python', case = False)

# Print proportion of tweets mentioning #python
print("Proportion of #python tweets:", np.sum(python) / ds_tweets.shape[0])


# In[ ]:


# Looking for text in all the wrong places
def check_word_in_tweet(word, data):
    """Checks if a word is in a Twitter dataset's text. 
    Checks text and extended tweet (140+ character tweets) for tweets,
    retweets and quoted tweets.
    Returns a logical pandas Series.
    """
    contains_column = data['text'].str.contains(word, case = False)
    contains_column |= data['extended_tweet-full_text'].str.contains(word, case = False)
    contains_column |= data['quoted_status-text'].str.contains(word, case = False) 
    contains_column |= data['quoted_status-extended_tweet-full_text'].str.contains(word, case = False) 
    contains_column |= data['retweeted_status-text'].str.contains(word, case = False) 
    contains_column |= data['retweeted_status-extended_tweet-full_text'].str.contains(word, case = False)
    return contains_column


# In[ ]:


# Comparing #python to #rstats
# Find mentions of #python in all text fields
python = check_word_in_tweet("#python", ds_tweets)

# Find mentions of #rstats in all text fields
rstats = check_word_in_tweet("#rstats", ds_tweets)

# Print proportion of tweets mentioning #python
print("Proportion of #python tweets:", np.sum(python) / ds_tweets.shape[0])

# Print proportion of tweets mentioning #rstats
print("Proportion of #rstats tweets:", np.sum(rstats) / ds_tweets.shape[0])


# In[ ]:


# Time Series
print(tweets['created_at'])
tweets['created_at'] = pd.to_datetime(tweets['created_at'])
print(tweets['created_at'])
tweets = tweets.set_index('created_at')

# Keywords as time series metrics
tweets['google'] = check_word_in_tweet('google', tweets)
print(tweets['google'])

print(np.sum(tweets['google']))

# Generating keyword means
mean_google = tweets['google'].resample('1 min').mean()
print(mean_google)

# Plotting keyword means
import matplolib.pyplot as plt

plt.plot(means_facebook.index.minute, means_facebook, color = 'blue')
plt.plot(means_google.index.minute, means-google, color = 'grren')
plt.xlabel('Minute')
plt.title('Company mentions')
plt.legend(('facebook', 'google'))
plt.show()


# In[ ]:


# Creating time series data frame
# Print created_at to see the original format of datetime in Twitter data
print(ds_tweets['created_at'].head())

# Convert the created_at column to np.datetime object
ds_tweets['created_at'] = pd.to_datetime(ds_tweets['created_at'])

# Print created_at to see new format
print(ds_tweets['created_at'].head())

# Set the index of ds_tweets to created_at
ds_tweets = ds_tweets.set_index('created_at')


# In[ ]:


# Generating mean frequency
# Create a python column
ds_tweets['python'] = check_word_in_tweet('#python', ds_tweets)

# Create an rstats column
ds_tweets['rstats'] = check_word_in_tweet('#rstats', ds_tweets)


# In[ ]:


# Plotting mean frequency
# Average of python column by day
mean_python = ds_tweets['python'].resample('1 d').mean()

# Average of rstats column by day
mean_rstats = ds_tweets['rstats'].resample('1 d').mean()

# Plot mean python/rstats by day
plt.plot(mean_python.index.day, mean_python, color = 'green')
plt.plot(mean_rstats.index.day, mean_rstats, color = 'blue')

# Add labels and show
plt.xlabel('Day'); plt.ylabel('Frequency')
plt.title('Language mentions over time')
plt.legend(('#python', '#rstats'))
plt.show()


# In[ ]:


# Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sentiment_scores = tweets['text'].apply(sid.polarity_scores)

# Interpreting sentiment scores
tweet1 = 'RT @jeffrey_heer: Thanks for inviting me, and thanks for the lovely visualization of the talk! ...'
print(sid.polarity_scores(tweet1))
{'neg':0.0, 'neu': 0.496, 'pos': 0.504, 'compound': 0.9041}

tweet2 = 'i am having problemns with google play music'
print(sid.polarity_scores(tweet2))
{'neg': 0.267, 'neu': 0.495, 'pos':0.238, 'compound': -0.0772}

# Generating sentiment averages
sentiment = sentiment_scores.apply(lambda x: x['compound'])
sentiment_fb = sentiment[check_word_in_tweet('facebook', tweets)].resample('1 min').mean()
sentiment_gg = sentiment[check_word_in_tweet('google', tweets)].resample('1 min').mean()

# Plotting sentiment scores
plt.plot(sentiment_fb.index.minute, sentiment_fb, color = 'blue')
plt.plot(sentiment_gg.index.minute, sentiment_gg, color = 'green')

plt.xlabel('Minute')
plt.ylabel('Sentiment')
plt.title('Sentiment of companies')
plt.legend(('Facebook', 'Google'))
plt.show()


# In[ ]:


# Loading VADER
# Load SentimentIntensityAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Instantiate new SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# Generate sentiment scores
sentiment_scores = ds_tweets['text'].apply(sid.polarity_scores)


# In[ ]:


# Calculating sentiment scores
# Print out the text of a positive tweet
print(ds_tweets[sentiment > 0.6]['text'].values[0])

# Print out the text of a negative tweet
print(ds_tweets[sentiment < -0.6]['text'].values[0])

# Generate average sentiment scores for #python
sentiment_py = sentiment[ check_word_in_tweet('#python', ds_tweets) ].resample('1 d').mean()

# Generate average sentiment scores for #rstats
sentiment_r = sentiment[ check_word_in_tweet('#rstats', ds_tweets) ].resample('1 d').mean()


# In[ ]:


# Plotting sentiment scores
# Import matplotlib
import matplotlib.pyplot as plt

# Plot average #python sentiment per day
plt.plot(sentiment_py.index.day, sentiment_py, color = 'green')

# Plot average #rstats sentiment per day
plt.plot(sentiment_r.index.day, sentiment_r, color = 'blue')

plt.xlabel('Day')
plt.ylabel('Sentiment')
plt.title('Sentiment of data science languages')
plt.legend(('#python', '#rstats'))
plt.show()


# # Twitter Networks

# In[ ]:


# Importing and visualization Tweest Networks
import networkx as nx
## ... flatten and covert JSON
G_rt = nx.from_pandas_edgelist(tweets, source = 'user-screen_name', target = 'retweeted_status-user-screen_name', 
                               create_using = nx.DiGraph())

# Importing a quoted network
import networkx as nx
## ... flatten and covert JSON
G_reply = nx.from_pandas_edgelist(tweets, source = 'user-screen_name', target = 'in_reply_to_screen_name', 
                                  create_using = nx.DiGraph())

# Visualization
x.draw_networkx(T)
plt.axis('off')

sizes =
    [x[1]*100 for x in T.degree()]
nx.draw_network(T, node_size = sizes, with_labels = False, alpha = 0.6, width = 0.3)
plt.axis('off')

# Circular layout
circle_pos = nx.circular_layout(T)
nx.draw_networkx(T, pos = circle_pos, node_size = sizes, with_labels = False, alpha = 0.6, width = 0.3)
plt.axis('off')


# In[ ]:


# Creating retweet network
# Import networkx
import networkx as nx

# Create retweet network from edgelist
G_rt = nx.from_pandas_edgelist(
    sotu_retweets,
    source = 'user-screen_name',
    target = 'retweeted_status-user-screen_name',
    create_using = nx.DiGraph())
 
# Print the number of nodes
print('Nodes in RT network:', len(G_rt.nodes()))

# Print the number of edges
print('Edges in RT network:', len(G_rt.edges()))


# In[ ]:


# Creating reply network
# Import networkx
import networkx as nx

# Create reply network from edgelist
G_reply = nx.from_pandas_edgelist(
    sotu_replies,
    source = 'user-screen_name',
    target = 'in_reply_to_screen_name',
    create_using = nx.DiGraph())
    
# Print the number of nodes
print('Nodes in reply network:', len(G_reply.nodes()))

# Print the number of edges
print('Edges in reply network:', len(G_reply.edges()))


# In[ ]:


# Visualizing retweet network
# Create random layout positions
pos = nx.random_layout(G_rt)

# Create size list
sizes = [x[1] for x in G_rt.degree()]

# Draw the network
nx.draw_networkx(G_rt, pos, 
    with_labels = False, 
    node_size = sizes,
    width = 0.1, alpha = 0.7,
    arrowsize = 2, linewidths = 0)

# Turn axis off and show
plt.axis('off'); plt.show()


# In[ ]:


# Centrality: node importance
# Degree centrality
nx.in_degree_centrality(T)
nx.out_degree_centrality(T)

# Betweenness Centrality
nx.betweenness_centrality(T)

# Priting highest centrality
bc = nx.betweenness_centrality(T)

betweenness = pd.DataFrame(list(bc.items()), list(bc.items()), columns = ['Name', 'Cent'])
print(betweenness.sort_values('Cent', ascending = False).head())

#********************************************************************************************************************#
#                                           Centrality in different networks                                         #
# ------------------------------------------------------------------------------------------------------------------ #
#                                                                 Centrality                                         #
#                        ___________________________________________________________________________________________ #
#                            In-Degree          Out-Degree                          Betweeness                       #
# __________________________________________________________________________________________________________________ #
#          * Retweets  *  Gets retweets   *  Shares retweets     *   Bridges different topic/ideology communities    #
# Network  * _______________________________________________________________________________________________________ #
# Type     * Replies   *  Gets most       *  Participates in     *   Bridges different topic/ideology discussions    #
#          *           *  replies         *  many conversations  *                                                   #
#********************************************************************************************************************#

# The Ratio
degree_rt = pd.DataFrame(list(G_rt.in_degree()), columns = ['screen_name', 'degree'])
degree_reply = pd.DataFrame(list(G_reply.in_degree()), columns = ['screen_name', 'degree'])

ratio = degree_rt.merge(degree_reply, on = 'screen_name', suffixes = ('_rt', '_reply'))
ratio['ratio'] = ratio['degree_reply'] / ratio['degree_rt']


# In[ ]:


# In-degree centrality
# Generate in-degree centrality for retweets 
rt_centrality = nx.in_degree_centrality(G_rt)

# Generate in-degree centrality for replies 
reply_centrality = nx.in_degree_centrality(G_reply)

# Store centralities in DataFrame
rt = pd.DataFrame(list(rt_centrality.items()), columns = column_names)
reply = pd.DataFrame(list(reply_centrality.items()), columns = column_names)

# Print first five results in descending order of centrality
print(rt.sort_values('degree_centrality', ascending = False).head())

# Print first five results in descending order of centrality
print(reply.sort_values('degree_centrality', ascending = False).head())


# In[ ]:


# Betweenness Centrality
# Generate betweenness centrality for retweets 
rt_centrality = nx.betweenness_centrality(G_rt)

# Generate betweenness centrality for replies 
reply_centrality = nx.betweenness_centrality(G_reply)

# Store centralities in data frames
rt = pd.DataFrame(list(rt_centrality.items()), columns = column_names)
reply = pd.DataFrame(list(reply_centrality.items()), columns = column_names)

# Print first five results in descending order of centrality
print(rt.sort_values('betweenness_centrality', ascending = False).head())

# Print first five results in descending order of centrality
print(reply.sort_values('betweenness_centrality', ascending = False).head())


# In[ ]:


# Ratios
# Calculate in-degrees and store in DataFrame
degree_rt = pd.DataFrame(list(G_rt.in_degree()), columns = column_names)
degree_reply = pd.DataFrame(list(G_reply.in_degree()), columns = column_names)

# Merge the two DataFrames on screen name
ratio = degree_rt.merge(degree_reply, on = 'screen_name', suffixes = ('_rt', '_reply'))

# Calculate the ratio
ratio['ratio'] = ratio['degree_reply'] / ratio['degree_rt']

# Exclude any tweets with less than 5 retweets
ratio = ratio[ratio['degree_rt'] >= 5]

# Print out first five with highest ratio
print(ratio.sort_values('ratio', ascending = False).head())


# # Maps and Twitter Data

# In[ ]:


# Geographical Data in Twitter JSON
print(tweet['place'])

{'attributes': {},
    'bounding_box': {'coordinates':[[[-80.47611, 37.185195],
                                     [-80.47611, 37.273387],
                                     [-80.381618, 37.273387],
                                     [-80.381618, 37.185195]]],
                    'type': 'Polygon'},
                    'country': 'United States',
                    'country_code': 'US',
                    'full_name': 'Blacksburg',
                    'place_type': 'city',
                    ...}

# Calculating the centroid
coordinates = [
    [-80.47611, 37.185195],
    [-80.47611, 37.273387],
    [-80.381618, 37.273387],
    [-80.381618, 37.185195]]

longs = np.unique( [x[0] for x in coordinates] )
lats = np.unique( x[1] for x in coordinates] )

central_long = np.sum(longs) / 2
central_lat = np.sum(lats) / 2

# Coordinates JSON
print(tweet['coordinates'])

{'type': 'Point',
'coordintates': [-72.2833, 21.7833]}


# In[ ]:


# Accessing user-defined location
# Print out the location of a single tweet
print(tweet_json['user']['location'])

# Flatten and load the SOTU tweets into a dataframe
tweets_sotu = pd.DataFrame(flatten_tweets(tweets_sotu_json))

# Print out top five user-defined locations
print(tweets_sotu['user-location'].value_counts().head())


# In[ ]:


# Accessing bounding box
def getBoundingBox(place):
    """ Returns the bounding box coordinates."""
    return place['bounding_box']['coordinates']

# Apply the function which gets bounding box coordinates
bounding_boxes = tweets_sotu['place'].apply(getBoundingBox)

# Print out the first bounding box coordinates
print(bounding_boxes.values[0])


# In[ ]:


# Calculating the centroid
def calculateCentroid(place):
    """ Calculates the centroid from a bounding box."""
    # Obtain the coordinates from the bounding box.
    coordinates = place['bounding_box']['coordinates'][0]
        
    longs = np.unique( [x[0] for x in coordinates] )
    lats  = np.unique( [x[1] for x in coordinates] )

    if len(longs) == 1 and len(lats) == 1:
        # return a single coordinate
        return (longs[0], lats[0])
    elif len(longs) == 2 and len(lats) == 2:
        # If we have two longs and lats, we have a box.
        central_long = np.sum(longs) / 2
        central_lat  = np.sum(lats) / 2
    else:
        raise ValueError("Non-rectangular polygon not supported: %s" % 
            ",".join(map(lambda x: str(x), coordinates)) )

    return (central_long, central_lat)
    
# Calculate the centroids of place     
centroids = tweets_sotu['place'].apply(calculateCentroid)


# In[ ]:


# Creating Twitter maps
from mpl_toolkits.basemap import Basemap

m = Basemap(projection = 'merc', llcrnrlat = -35,62, llcrnrlon = -17,29, urcrnrlat = 37.73, urcrnrlon = 51.39)

m.fillcontinentes(color = 'white')
m.drawcoastlines(color = 'gray')
m.drawcountries(color = 'gray')

# Plotting points
africa = pd.read_cs('africa.csv')
longs = africa['CapitalLongtitude']
lats = africa['CapitalLatitude']

m = Basemap(...)

m.fillcontinents(color = 'white',zorder = 0)
m.drawcoastlines(color = 'gray')
m.drawcountries(color = 'gray')

m.scatter(longs.values, lats.values, latlon = True, alpha = 0.7)

# Using color
m.scatter(longs.values, lats.values, latlon = True, c = arabic.values, cmap = 'Paired' alpha = 1)


# In[ ]:


# Creating Basemap map
# Import Basemap
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Set up the US bounding box
us_boundingbox = [-125, 22, -64, 50] 

# Set up the Basemap object
m = Basemap(llcrnrlon = us_boundingbox[0],
            llcrnrlat = us_boundingbox[1],
            urcrnrlon = us_boundingbox[2],
            urcrnrlat = us_boundingbox[3],
            projection='merc')


# In[ ]:


# Creating Basemap map
# Import Basemap
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Set up the US bounding box
us_boundingbox = [-125, 22, -64, 50] 

# Set up the Basemap object
m = Basemap(llcrnrlon = us_boundingbox[0],
            llcrnrlat = us_boundingbox[1],
            urcrnrlon = us_boundingbox[2],
            urcrnrlat = us_boundingbox[3],
            projection='merc')

# Draw continents in white,
# coastlines and countries in gray
m.fillcontinents(color='white')
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')

# Draw the states and show the plot
m.drawstates(color='gray')
plt.show()


# In[ ]:


# Plotting centroid coordinates
# Calculate the centroids for the dataset 
# and isolate longitudue and latitudes
centroids = tweets_sotu['place'].apply(calculateCentroid)
lon = [x[0] for x in centroids]
lat = [x[1] for x in centroids]

# Draw continents, coastlines, countries, and states
m.fillcontinents(color='white', zorder = 0)
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# Draw the points and show the plot
m.scatter(lon, lat, latlon = True, alpha = 0.7)
plt.show()


# In[ ]:


# Coloring by sentiment
# Generate sentiment scores
sentiment_scores = tweets_sotu['text'].apply(sid.polarity_scores)

# Isolate the compound element
sentiment_scores = [x['compound'] for x in sentiment_scores]

# Draw the points
m.scatter(lon, lat, latlon = True, 
           c = sentiment_scores,
           cmap = 'coolwarm', alpha = 0.7)

# Show the plot
plt.show()


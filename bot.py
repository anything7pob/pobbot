import os
import time

import tweepy

class TwitterAPI:
    """
    Class for accessing the Twitter API.
    Requires API credentials to be available in environment
    variables. These will be set appropriately if the bot was created
    with init.sh included with the heroku-twitterbot-starter
    """
    def __init__(self):
        consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
       
    for tweet in tweepy.Cursor(self.api.search, q='romford''chelmsford''essex''roofing').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Follow the user who tweeted
        tweet.user.follow()
        print('Followed the user')
        
        time.sleep(3200)  
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break    
        
        
        

  

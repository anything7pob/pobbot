import tweepy
from time import sleep
class TwitterAPI:
    """
    Class for accessing the Twitter API.
    Requires API credentials to be available in environment
    variables. These will be set appropriately if the bot was created
    with init.sh included with the heroku-twitterbot-starter
    """

for tweet in tweepy.Cursor(api.search, q='#Romford','#Chelmsford','Roofing').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        if not tweet.user.following:
            # Don't forget to indent
            tweet.user.follow()
            print('Followed the user')
       
        

        sleep(3600)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

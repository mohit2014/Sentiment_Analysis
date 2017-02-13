import tweepy
from textblob import TextBlob

consumer_key = 'e1pMZaLgrRj9S8G7454Xd8R09'
consumer_secret = 'I2oCIXhrvIW0DWts7oIcy7KbJQnoA0vx5lrirgVBjRyfFbmvqJ'
access_token = '796037734213173248-8nCkbV4GTzF7U2Yi1Q4TP7PmcfsVTGJ'
access_token_secret = 'AdczcfKRnjGClp4Ro2rPCquTEO4Gbebwg8Ha8s6I6Yh17'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret) #to login twitter
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

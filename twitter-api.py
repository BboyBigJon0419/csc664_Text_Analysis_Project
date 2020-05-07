import tweepy
import json
import csv
import re
import time
import os

#Creates Authentication for accessing Twitter
auth = tweepy.OAuthHandler('ETFoosF3U6gc67uOwqd9Y9dZP', 'c6ILdm0GGl5HP2idBM8a9ByO4xXSplRJkNc4GkuUiRvzwUTzJP')
auth.set_access_token('826919244147200000-cvufmUfIuZ0M1IeAUhne5t0bEWhnf6c', 'hpzrDhOo7Ld6kowWeZHQGmbnEoI65KID2Z1h8SpJAnH9w')

#initialize Tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Prints tweets and retweets from users homepage and returns home timeline 
#and prints out the text of each tweet
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text).encode('utf-8')

for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)

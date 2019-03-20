
import tweepy
from config import *
import datetime



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
day = datetime.datetime.now()

api.update_status('@martinbreuss good morning it\'s {day}')


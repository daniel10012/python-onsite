'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import time
import tweepy
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def popularity(username):
    # ids = []
    # for page in tweepy.Cursor(api.followers_ids, screen_name=username).pages():
    #     ids.extend(page)
    # screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]
    # num_followers = len(screen_names)
    user = api.get_user(username)
    num_followers = user.followers_count

    if num_followers < 5:
        return "looser"
    elif num_followers < 10:
        return"semi looser"
    elif num_followers <100:
        return "normal"
    else:
        return "superstar"

print(popularity("mckenziecaden"))

user = api.get_user('martinbreuss')
num_friends = user.friends_count
num_followers = user.followers_count

ratio = num_friends/num_followers

if ratio > 1:
    print("not all your friends follow you !")
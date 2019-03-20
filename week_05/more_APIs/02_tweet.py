'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P

'''

import json
import tweepy
from config import *
from crontab import CronTab

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#api.update_status('Hello Ming!')

# with open("tweets.json", "r") as fin:
#     tweets = json.load(fin)
#     for tweet in tweets:
#         api.update_status(tweet["tweet"])


def main():
    users_cron = CronTab(user='danielwegmann')
    job = users_cron.new(command='python3 Documents/CodingNomads/python-onsite/week_05/more_APIs/morningtweet.py')
    job.setall('14 9 * * 1-5')
    users_cron.write()



if __name__ == "__main__":
    main()



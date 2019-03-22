'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]

We will continue to work with this data throughout the week, so make sure to complete it!

'''



import re
from config import SLACK_BOT_TOKEN
from slackclient import SlackClient
from pprint import pprint
from datetime import datetime
import json


slack_token = SLACK_BOT_TOKEN
sc = SlackClient(slack_token)

sc.api_call("conversations.list")
r = sc.api_call(
  "channels.history",
  channel="CGUDWETHR"
)

messages = r["messages"]
urls = []

list_messages = []


for m in messages:
  #print(m)
  time = float(m["ts"])
  dict_message = {}
  string = m["text"]
  url = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",string)
  if url != []:
    url = url[0]
    dict_message["msg_id"] = m["client_msg_id"]
    dict_message["link"] = url
    des = string.replace(url, "").strip("<>/'")
    dict_message["description"] = des
    dict_message["date added"] = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    dict_message["read"] = False
    dict_message["rating"]= 0
    try:
      if m['reply_users_count'] != 0:
        dict_message["comments"] = "there are comments"
    except KeyError:
      dict_message["comments"] = "there are no comments"
    try:
      if m["is_starred"] == True:
        dict_message["is_starred"] = True
    except KeyError:
      dict_message["is_starred"] = False
    list_messages.append(dict_message)

with open("info.json", "w") as fout:
  json.dump(list_messages,fout)







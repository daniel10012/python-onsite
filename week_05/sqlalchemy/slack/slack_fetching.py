import re
from config import SLACK_BOT_TOKEN
from slackclient import SlackClient
from pprint import pprint
from datetime import datetime


def get_list_messages():

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
  return list_messages

#print(get_list_messages())
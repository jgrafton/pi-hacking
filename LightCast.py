import time
import datetime
import json
from pprint import pprint
from twython import Twython


# Load our keys
twitter_key_file=open('tweetkey.json')
twitter_keys = json.load(twitter_key_file)

# Twitter application authentication
APP_KEY = twitter_keys['APP_KEY']
APP_SECRET = twitter_keys['APP_SECRET']
OAUTH_TOKEN = twitter_keys['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = twitter_keys['OAUTH_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

# Posting here for debug use only
green_value = 1
yellow_value = 0
red_value = 0

epoc_time = int(datetime.datetime.now().strftime("%s"))
payload={"green":green_value,"yellow":yellow_value,"red":red_value,"timestamp":epoc_time }

print json.dumps(payload)

# Create tweet post
try:
    #twitter.verify_credentials()
    twitter.update_status(status='twython is great')
except KeyboardInterrupt:
    pass





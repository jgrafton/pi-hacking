import time
import json
import RPi.GPIO as GPIO
from twython import TwythonStreamer
import random


# Search terms
TERMS = '#ebola'

# GPIO pin number of LED
RED=4
YELLOW=2
GREEN=3

def random_light():
	light = random.randint(2,5)
	GPIO.output(light, GPIO.HIGH)
	time.sleep(0.75)
	GPIO.output(light, GPIO.LOW)


# Load our keys
twitter_key_file=open('tweetkey.json')
twitter_keys = json.load(twitter_key_file)

# Twitter application authentication
APP_KEY = twitter_keys['APP_KEY']
APP_SECRET = twitter_keys['APP_SECRET']
OAUTH_TOKEN = twitter_keys['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = twitter_keys['OAUTH_TOKEN_SECRET']

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
		try:
        		print data['text'].encode('utf-8')
                        random_light()
		except:
			pass
# Setup GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.output(RED, GPIO.LOW)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.output(YELLOW, GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.output(GREEN, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

#!/usr/bin/python
import time
import json
import RPi.GPIO as GPIO
from twython import TwythonStreamer


# GPIO pin number of LED
LEDS = {"RED": 4, "YELLOW": 2, "GREEN": 3}


# Load our keys
twitter_key_file = open('tweetkey.json')
twitter_keys = json.load(twitter_key_file)

# Twitter application authentication
APP_KEY = twitter_keys['APP_KEY']
APP_SECRET = twitter_keys['APP_SECRET']
OAUTH_TOKEN = twitter_keys['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = twitter_keys['OAUTH_TOKEN_SECRET']


def toggle_light(light, state):
    if light in LEDS:
	if state == 1:
            GPIO.output(LEDS[light], GPIO.HIGH)
        elif state == 0:
	    GPIO.output(LEDS[light], GPIO.LOW)
        else:
	    pass


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            #try:
                payload = json.loads(data['text'])
        	print payload
		for key,value in payload:
                    toggle_light( key, value )
            #except Exception:
		#print "ignoring tweet: " + data['text']

    def on_error(self, status_code, data):
        print status_code, data

# Setup each light GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS["RED"], GPIO.OUT)
GPIO.output(LEDS["RED"], GPIO.LOW)
GPIO.setup(LEDS["YELLOW"], GPIO.OUT)
GPIO.output(LEDS["YELLOW"], GPIO.LOW)
GPIO.setup(LEDS["GREEN"], GPIO.OUT)
GPIO.output(LEDS["GREEN"], GPIO.LOW)

# Create streamer
try:
    toggle_light("RED", 1 )
    time.sleep(1)
    toggle_light("RED", 0 )
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.user()
except:
    GPIO.cleanup()


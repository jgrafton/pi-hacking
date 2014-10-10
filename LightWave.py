#!/usr/bin/env python

import json
import RPi.GPIO as GPIO
from twython import TwythonStreamer


# GPIO pin number of LED
LEDS = [{"RED": 4, "YELLOW": 2, "GREEN": 3}]


# Load our keys
twitter_key_file = open('tweetkey.json')
twitter_keys = json.load(twitter_key_file)

# Twitter application authentication
APP_KEY = twitter_keys['APP_KEY']
APP_SECRET = twitter_keys['APP_SECRET']
OAUTH_TOKEN = twitter_keys['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = twitter_keys['OAUTH_TOKEN_SECRET']


def toggle_light(light, state):
    if state == "ON":
        GPIO.output(light, GPIO.HIGH)
    else:
        GPIO.output(light, GPIO.LOW)


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                payload = json.loads(data['text'])
                print payload["RED"]
                print payload["YELLOW"]
                print payload["GREEN"]
            except:
                print "ignoring tweet"

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
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.user()
except KeyboardInterrupt:
    GPIO.cleanup()

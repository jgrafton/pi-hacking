#!/usr/bin/python
import time
import json
import RPi.GPIO as GPIO
from twython import TwythonStreamer


# GPIO pin number of LED
LEDS = {'RED': 4, 'YELLOW': 2, 'GREEN': 3}

# Setup each light GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS["RED"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEDS["YELLOW"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEDS["GREEN"], GPIO.OUT, initial=GPIO.LOW)


def toggle_light(light, state):
    if light in LEDS:
        if int(state) == 1:
            GPIO.output(LEDS[light], GPIO.HIGH)
        elif int(state) == 0:
            GPIO.output(LEDS[light], GPIO.LOW)
        else:
            print "Debug: unknown state found: " + state


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                payload = json.loads(data['text'].encode('utf-8'))
                print payload
                for key, value in payload.iteritems():
                    print "Payload info: " + key, value
                    toggle_light(key, value)
            except Exception:
                print "ignoring tweet: " + payload

    def on_error(self, status_code, data):
        print status_code, data


# Load our keys
twitter_key_file = open('tweetkey.json')
twitter_keys = json.load(twitter_key_file)

# Twitter application authentication
APP_KEY = twitter_keys['APP_KEY']
APP_SECRET = twitter_keys['APP_SECRET']
OAUTH_TOKEN = twitter_keys['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = twitter_keys['OAUTH_TOKEN_SECRET']


# Create streamer
try:
    print "GPIO RPI Revision: ", GPIO.RPI_REVISION
    print "GPIO Version: ", GPIO.VERSION
    print "Beginning Initilization sequence. Please standby"
    for key, value in LEDS.iteritems():
        print "Initilizing light ", key
        toggle_light(key, 1)
        time.sleep(1)
        toggle_light(key, 0)
    print "Initilization Complete.  Waiting for incoming data:"
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.user()
except:
    print "Exiting..."
    GPIO.cleanup()

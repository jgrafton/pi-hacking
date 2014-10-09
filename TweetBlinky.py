import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# Search terms
TERMS = '#ebola'

# GPIO pin number of LED
LED = 11

# Load our keys
twitter_key_file=open('tweetkey.json')
twitter_keys = json.load(twitter_key_file)

# Twitter application authentication
<<<<<<< HEAD
APP_KEY = twitter_keys['APP_KEY']
APP_SECRET = twitter_keys['APP_SECRET']
OAUTH_TOKEN = twitter_keys['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = twitter_keys['OAUTH_TOKEN_SECRET']
=======
APP_KEY = 'IIzoyEXAvLcNAR3OxK65dKqZm'
APP_SECRET = 'gm9do0neFtsQ8Iv8WVoLJE6duSJG5zdXvCfoKM7QOJcgVhP939'
OAUTH_TOKEN = '2840648905-q74EAyJoo5Q3racONYCx7QXGrFvQUMvz22phNSw'
OAUTH_TOKEN_SECRET = 'fbKmrRW9azsa5Do1mtRLjWRD36DSnyDEJapiQTCzEzuYd'
>>>>>>> 070c68e99c5cd36adab8742d9e9288dede5e958c

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LED, GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(LED, GPIO.LOW)

# Setup GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# Search terms
TERMS = '#ebola'

# GPIO pin number of LED
LED = 11

# Twitter application authentication
APP_KEY = 'WzpVxGq7GkBbhuFOHnhMxVtDZ'
APP_SECRET = 'emO0CQkB7sNAX4XSfMuf8DuLFMBp7viecLewy3OG8K2EMHmgY2'
OAUTH_TOKEN = '648983-weByKvXtqd9UMVcdPI41GANrV91vIW3miOd4GHBUFku'
OAUTH_TOKEN_SECRET = 'HbH3WEG4bsqo8qs0pcOboSCu6uHV0Jf8PibefaSHLmdoQ'

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

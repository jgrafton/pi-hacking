import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer


# Set the GPIO Channel
LED=11

# Twitter application authentication
APP_KEY = 'WzpVxGq7GkBbhuFOHnhMxVtDZ'
APP_SECRET = 'emO0CQkB7sNAX4XSfMuf8DuLFMBp7viecLewy3OG8K2EMHmgY2'
OAUTH_TOKEN = '648983-weByKvXtqd9UMVcdPI41GANrV91vIW3miOd4GHBUFku'
OAUTH_TOKEN_SECRET = 'HbH3WEG4bsqo8qs0pcOboSCu6uHV0Jf8PibefaSHLmdoQ'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1.0)
            GPIO.output(LED, GPIO.LOW)
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data

# Setup GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.user()
except KeyboardInterrupt:
    GPIO.cleanup()



import time
import json
import RPi.GPIO as GPIO
from twython import TwythonStreamer


# Set the GPIO Channel
LED=11

# Twitter application authentication
APP_KEY = 'IIzoyEXAvLcNAR3OxK65dKqZm'
APP_SECRET = 'gm9do0neFtsQ8Iv8WVoLJE6duSJG5zdXvCfoKM7QOJcgVhP939'
OAUTH_TOKEN = '2840648905-q74EAyJoo5Q3racONYCx7QXGrFvQUMvz22phNSw'
OAUTH_TOKEN_SECRET = 'fbKmrRW9azsa5Do1mtRLjWRD36DSnyDEJapiQTCzEzuYd'


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            try:
                payload = json.loads(data['text']) 
                print payload
                #GPIO.output(LED, GPIO.HIGH)
                #time.sleep(1.0)
                #GPIO.output(LED, GPIO.LOW)
	    except:
                print "ignoring tweet"
           
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



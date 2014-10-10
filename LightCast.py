#!/usr/bin/env python

import os
import sys
import datetime
try:
    import json
except:
    import simplejson as json
from twython import Twython
import optparse


def collect_command_args():
    # Collect the command line arguments to determine work to be performed.
    parser = optparse.OptionParser()
    parser.add_option("-r", "--red", action="store", type="string", dest="red", help='The State of the red light, options are ON or OFF')
    parser.add_option("-g", "--green", action="store", type="string", dest="green", help='The State of the green light, options are ON or OFF')
    parser.add_option("-y", "--yellow",  action="store", type="string", dest="yellow", help='The State of the yellow light, options are ON or OFF')

    if(len(sys.argv) < 2):
        parser.print_help()
        os._exit(0)

    return parser

# The actual RUN block for the whole script.
if __name__ == '__main__':

    # Collect the commandline arguments and print usage if necessary
    parser = collect_command_args()
    (options, args) = parser.parse_args()

    # Load our keys
    twitter_key_file = open('tweetkey.json')
    twitter_keys = json.load(twitter_key_file)

    # Twitter application authentication
    APP_KEY = twitter_keys['APP_KEY']
    APP_SECRET = twitter_keys['APP_SECRET']
    OAUTH_TOKEN = twitter_keys['OAUTH_TOKEN']
    OAUTH_TOKEN_SECRET = twitter_keys['OAUTH_TOKEN_SECRET']

    # Create the twitter object with our authentication
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    epoc_time = int(datetime.datetime.now().strftime("%s"))
    payload = {"GREEN": options.green, "YELLOW": options.yellow, "RED": options.red, "timestamp": epoc_time}

    print json.dumps(payload)

    # Create tweet post
    try:
        # twitter.verify_credentials()
        twitter.update_status(status=json.dumps(payload))
    except KeyboardInterrupt:
        pass

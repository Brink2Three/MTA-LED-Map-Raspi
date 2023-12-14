import time
#import board
#import neopixel
import os
from datetime import datetime, timedelta
from nyct_gtfs import NYCTFeed
from dotenv import load_dotenv
load_dotenv()

MTA_API_KEY = os.getenv('api_key')
line_id = "1"


def main():
    line = [line_id]
    feed = NYCTFeed(line_id, api_key=MTA_API_KEY)
    print(MTA_API_KEY)
    print_feed(feed, line)

#Trying to extrapolate data so I can feed the stopped train's stations into a variable. 
def print_feed(feed, line_id):
    for trip in feed.filter_trips(line_id):
        stop_check = str(trip)
        if stop_check.__contains__("STOPPED_AT"):
            print(stop_check)
        else:
            pass

if __name__ == '__main__':
    main()
    
else : 
    ()

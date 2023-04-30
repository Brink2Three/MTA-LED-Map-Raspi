import time
#import board
#import neopixel
import os
from datetime import datetime, timedelta
from nyct_gtfs import NYCTFeed
from dotenv import load_dotenv
load_dotenv()

MTA_API_KEY = os.getenv('api_key')



def main():
    line = ["1"]
    feed = NYCTFeed("1", api_key=MTA_API_KEY)
    print_feed(feed, line, "N")
    print_feed(feed, line, "S")

#Trying to extrapolate data so I can feed the stopped train's stations into a variable. 
def print_feed(feed, line_id, direction):
    for trip in feed.filter_trips(line_id, direction):
        stop_check = str(trip)
        if stop_check.__contains__("STOPPED_AT"):
            print(stop_check)
        else:
            print("")

if __name__ == '__main__':
    main()
else : 
    ()

import time
#import board
#import neopixel
import os
from datetime import datetime, timedelta
from nyct_gtfs import NYCTFeed
from dotenv import load_dotenv
load_dotenv()

MTA_API_KEY = os.getenv('api_key')



def print_feed(feed, line_id, direction):
    for trip in feed.filter_trips(line_id, direction):
        print(trip)

def main():
    line = ["1"]
    feed = NYCTFeed("1", api_key=MTA_API_KEY)
    print_feed(feed, line, "N")
    print_feed(feed, line, "S")

if __name__ == '__main__':
    main()
import os
from datetime import datetime, timedelta

from nyct_gtfs import NYCTFeed
from dotenv import load_dotenv
load_dotenv()

MTA_API_KEY = os.getenv('api_key')

# Switch the broken stops array to test stops.
#brokenstops = ["R60S", "R60N", "R65S", "R65N"]
brokenstops = [""]
def print_feed(feed, line_id, direction):
    for trip in feed.filter_trips(line_id, direction):
        if trip.location in brokenstops:
            pass
        else:
            print(trip)

def main():
    line = ["R"]
    feed = NYCTFeed("R", api_key=MTA_API_KEY)
    print_feed(feed, line, "N")
    print_feed(feed, line, "S")

if __name__ == '__main__':
    main()

import os
from datetime import datetime, timedelta

from nyct_gtfs import NYCTFeed

def print_feed(feed, line_id, direction):
    for trip in feed.filter_trips(line_id, direction):
        print(trip)

def main():
    line = ["1"]
    feed = NYCTFeed("1", api_key='API KEY HERE')
    print_feed(feed, line, "N")
    print_feed(feed, line, "S")

if __name__ == '__main__':
    main()
#Combined project, once all parts are complete.
import time
import board
import neopixel
import os
from datetime import datetime, timedelta
from nyct_gtfs import NYCTFeed
from dotenv import load_dotenv
load_dotenv()

MTA_API_KEY = os.getenv('api_key')

pixels1 = neopixel.NeoPixel(board.D18, 180, brightness=.15)

x=0

# Line colors so I don't have to type the codes out
line_123 = (127, 0, 0)
line_456 = (0, 127, 7)
line_ace = (6, 20, 127)
line_7 = (100, 0, 100)
line_bdfm = (255, 107, 0)
line_jz = (190, 50, 14)
line_nqrw = (252, 204, 10)
line_ls = (128, 129, 131)
bg = (5, 5, 5)


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
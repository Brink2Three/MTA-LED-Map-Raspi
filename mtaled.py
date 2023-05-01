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

#pixels1 = neopixel.NeoPixel(board.D18, 180, brightness=.15)

x=0

# Line colors so I don't have to type the codes out
line_123 = (127, 0, 0)
line_456 = (0, 127, 7)
line_7 = (100, 0, 100)
line_ace = (6, 20, 127)
line_bdfm = (255, 107, 0)
line_jz = (190, 50, 14)
line_nqrw = (252, 204, 10)
line_ls = (128, 129, 131)
bg = (5, 5, 5)

strings = ["1", "2", "3", "4", "5", "6", "7", "A", "C", "E", "B", "D", "F", "M", "N", "Q", "R", "W", "J", "Z", "L", "S"]

def process_lines(line_num):
    # do some processing on the string
    processed_lines = line_num
    return processed_lines

for line_num in strings:
    line_id = process_lines(line_num)

def main():
    for line_num in strings:
        line_id = process_lines(line_num)
        line = [line_id]
        feed = NYCTFeed(line_id, api_key=MTA_API_KEY)
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
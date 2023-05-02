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

lines = ["R"]

def process_lines(line_num):
    # do some processing on the string because it won't work without it. idk
    processed_lines = line_num
    return processed_lines

def main():
    for line_num in lines:
        line_id = process_lines(line_num)
        line = [line_id]
        feed = NYCTFeed(line_id, api_key=MTA_API_KEY)
        #This will randomly fail if a stop at R60N or R60S is detected... This SHOULD negate that. 
        try:
            print_feed(feed, line)
        except:
            pass

#Trying to extrapolate data so I can feed the stopped train's stations into a variable. 
def print_feed(feed, line_id):
    for trip in feed.filter_trips(line_id):
        #Stop check will randomly fail if R60N or R60S stop is stopped. the try in main should resolve this. 
        stop_check = str(trip)
        if stop_check.__contains__("STOPPED_AT"):
            print(stop_check)
        else:
            pass

if __name__ == '__main__':
    main()
    
else : 
    ()

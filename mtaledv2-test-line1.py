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


#NEOPIXEL SETTINGS MUST BE SET BELOW
#pixels1 = neopixel.NeoPixel(board.D18, 87, brightness=.15)
# Line colors so I don't have to type the codes out
line_123 = (127, 0, 0)
line_456 = (0, 127, 7)
line_7 = (100, 0, 100)
line_ace = (6, 20, 127)
line_bdfm = (255, 107, 0)
line_jz = (190, 50, 14)
line_nqrw = (252, 204, 10)
line_ls = (128, 129, 131)
line_g = (0, 127, 7)
line_h = (11, 11, 11)
bg = (5, 5, 5)

lines = ["1", "2", "3", "4", "5", "6", "7", "A", "C", "E", "B", "D", "F", "M", "N", "Q", "R", "W", "J", "Z", "L", "S"]
brokenstops = ["R70N", "R70S", "R60S", "R60N", "R65S", "R65N", "D23S", "D23N", "H17S", "H18S", "A29S"]
lines_array = []
stops_array = []
combined_array = []

def process_lines(line_num):
    processed_lines = line_num
    return processed_lines

# print the feed line by line
def main():
    for line_num in lines:
        line_id = process_lines(line_num)
        line = [line_id]
        feed = NYCTFeed(line_id, api_key=MTA_API_KEY)
        print_feed(feed, line)

def print_feed(feed, line_id):
    for trip in feed.filter_trips(line_id):
        if trip.location in brokenstops:
            pass
        else:
            stop_check = str(trip)
            if stop_check.__contains__("STOPPED_AT"):
                lines_array.append(stop_check[11:12])
                stop_ind = stop_check.find('STOPPED_AT') + len('STOPPED_AT ')
                last_ind = stop_check.find(', last update')
                stops_array.append(stop_check[stop_ind:last_ind])
                #print(stop_check[11:12] + " " + stop_check[stop_ind:last_ind])
            else:
                pass

if __name__ == '__main__':
    main()
    for i in range(len(lines_array)): 
        combined_array.append(str(lines_array[i] + " " + stops_array[i]))
    print(combined_array)
    #set all pixels to white
    pixels1 = neopixel.NeoPixel(board.D18, 87, brightness=.15)
    pixels1.fill((15, 15, 15))
    #mother of all regex edits
    if "1 66 St-Lincoln Center" in combined_array:
        pixels1[84]= line_123
    else:
        pass
    if "1 59 St-Columbus Circle" in combined_array:
        pixels1[82]= line_123
    else:
        pass
    if "1 50 St" in combined_array:
        pixels1[70]= line_123
    else:
        pass
    if "1 Times Sq-42 St" in combined_array:
        pixels1[67]= line_123
    else:
        pass
    if "1 34 St-Penn Station" in combined_array:
        pixels1[61]= line_123
    else:
        pass
    if "1 28 St" in combined_array:
        pixels1[58]= line_123
    else:
        pass
    if "1 23 St" in combined_array:
        pixels1[52]= line_123
    else:
        pass
    if "1 18 St" in combined_array:
        pixels1[50]= line_123
    else:
        pass
    if "1 14 St" in combined_array:
        pixels1[48]= line_123
    else:
        pass
    if "1 Christopher St-Sheridan Sq" in combined_array:
        pixels1[40]= line_123
    else:
        pass
    if "1 Houston St" in combined_array:
        pixels1[34]= line_123
    else:
        pass
    if "1 Canal St" in combined_array:
        pixels1[22]= line_123
    else:
        pass
    if "1 Franklin St" in combined_array:
        pixels1[21]= line_123
    else:
        pass
    if "1 Chambers St" in combined_array:
        pixels1[19]= line_123
    else:
        pass
    if "1 WTC Cortlandt" in combined_array:
        pixels1[0]= line_123
    else:
        pass
    if "1 Rector St" in combined_array:
        pixels1[5]= line_123
    else:
        pass
    if "1 South Ferry Loop" in combined_array:
        pixels1[2]= line_123
    else:
        pass
    if "1 South Ferry" in combined_array:
        pixels1[2]= line_123
    else:
        ()
    
    # temp while testing to not use extra power
    time.sleep(10)
    pixels1.fill((0, 0, 0))
    

else: 
    ()
## TO DO: Change if stop_check.__contains__("STOPPED_AT"): to include arriving at.
# Since trains are not stopped at stations very long, this will add more colors
#Combined project, once all parts are complete.
import time
import board
import neopixel
from datetime import datetime, timedelta
from nyct_gtfs import NYCTFeed

# Version 2 of nyct_gtfs removed the need for API keys: https://pypi.org/project/nyct-gtfs/

#NEOPIXEL SETTINGS MUST BE SET BELOW
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
stop_to_led_map = {
    # 1 Line
    "1 66 St-Lincoln Center": (84, line_123),
    "1 59 St-Columbus Circle": (82, line_123),
    "1 50 St": (70, line_123),
    "1 Times Sq-42 St": (67, line_123),
    "1 34 St-Penn Station": (61, line_123),
    "1 28 St": (58, line_123),
    "1 23 St": (52, line_123),
    "1 18 St": (50, line_123),
    "1 14 St": (48, line_123),
    "1 Christopher St-Sheridan Sq": (40, line_123),
    "1 Houston St": (34, line_123),
    "1 Canal St": (22, line_123),
    "1 Franklin St": (21, line_123),
    "1 Chambers St": (19, line_123),
    "1 WTC Cortlandt": (0, line_123),
    "1 Rector St": (5, line_123),
    "1 South Ferry Loop": (2, line_123),
    "1 South Ferry": (2, line_123),
    # 2 Line
    "2 Park Place": (15, line_123),
    "2 Fulton St": (13, line_123),
    "2 Wall St": (4, line_123),
    # 4 Line
    "4 Fulton St": (10, line_456),
    "4 Wall St": (7, line_456),
    "4 Bowling Green": (4, line_456),
    # 6 Line
    "6 68 St-Hunter College": (86, line_456),
    "6 59 St": (77, line_456),
    "6 51 St": (74, line_456),
    "6 Grand Central-42 St": (64, line_456),
    "6 33 St": (63, line_456),
    "6 28 St": (56, line_456),
    "6 23 St": (54, line_456),
    "6 14 St-Union Sq": (45, line_456),
    "6 Astor Pl": (42, line_456),
    "6 Bleecker St": (37, line_456),
    "6 Spring St": (32, line_456),
    "6 Canal St": (25, line_456),
    "6 Brooklyn Bridge-City Hall": (17, line_456),
    # 7 Line
    "7 Grand Central-42 St": (64, line_7),
    "7 5 Av": (65, line_7),
    "7 Times Sq-42 St": (67, line_7),
    "7 34 St-Hudson Yards": (59, line_7),
    # S Line
    "S Grand Central-42 St": (64, line_ls),
    "S Times Sq-42 St": (67, line_ls),
    # A Line
    "A 59 St-Columbus Circle": (83, line_ace),
    "A 50 St": (69, line_ace),
    "A 42 St-Port Authority Bus Terminal": (68, line_ace),
    "A 34 St-Penn Station": (60, line_ace),
    "A 23 St": (51, line_ace),
    "A 14 St": (49, line_ace),
    "A W 4 St-Wash Sq": (39, line_ace),
    "A Spring St": (33, line_ace),
    "A Canal St": (23, line_ace),
    "A Chambers St": (20, line_ace),
    "A Fulton St": (11, line_ace),
    # E Line
    "E World Trade Center": (14, line_ace),
    # B Line
    "B Lexington Av/63 St": (84, line_bdfm),
    "B 57 St": (79, line_bdfm),
    # D Line
    "D 7 Av": (80, line_bdfm),
    "D 47-50 Sts-Rockefeller Ctr": (72, line_bdfm),
    "D 42 St-Bryant Pk": (66, line_bdfm),
    "D 34 St-Herald Sq": (62, line_bdfm),
    "D 23 St": (53, line_bdfm),
    "D 14 St": (47, line_bdfm),
    "D W 4 St-Wash Sq": (39, line_bdfm),
    "D Broadway-Lafayette St": (36, line_bdfm),
    "D Grand St": (27, line_bdfm),
    # F Line
    "F Lexington Av/53 St": (75, line_bdfm),
    "F 5 Av/53 St": (73, line_bdfm),
    "F 2 Av": (38, line_bdfm),
    "F Delancey St-Essex St": (30, line_bdfm),
    "F East Broadway": (28, line_bdfm),
    # Not really M Line (J/Z legacy stops)
    "M Delancey St-Essex St": (29, line_jz),
    "M Bowery": (31, line_jz),
    "M Canal St": (26, line_jz),
    "M Chambers St": (18, line_jz),
    "M Fulton St": (12, line_jz),
    "M Broad St": (5, line_jz),
    # L Line
    "L 8 Av": (49, line_ls),
    "L 6 Av": (47, line_ls),
    "L 14 St-Union Sq": (45, line_ls),
    "L 3 Av": (44, line_ls),
    "L 1 Av": (43, line_ls),
    # Q Line
    "Q Canal St": (24, line_nqrw),
    # R Line
    "R Lexington Av/59 St": (76, line_nqrw),
    "R 5 Av/59 St": (78, line_nqrw),
    "R 57 St-7 Av": (81, line_nqrw),
    "R 49 St": (71, line_nqrw),
    "R Times Sq-42 St": (67, line_nqrw),
    "R 34 St-Herald Sq": (62, line_nqrw),
    "R 28 St": (57, line_nqrw),
    "R 23 St": (54, line_nqrw),
    "R 14 St-Union Sq": (46, line_nqrw),
    "R 8 St-NYU": (41, line_nqrw),
    "R Prince St": (35, line_nqrw),
    "R Canal St": (24, line_nqrw),
    "R City Hall": (16, line_nqrw),
    "R Cortlandt St": (9, line_nqrw),
    "R Rector St": (6, line_nqrw),
    "R Whitehall St-South Ferry": (3, line_nqrw),
}

def process_lines(line_num):
    processed_lines = line_num
    return processed_lines

# print the feed line by line
def main():
    for line_num in lines:
        line_id = process_lines(line_num)
        line = [line_id]
        print("Reading MTA Feed the " + line_id + " Trains...")
        feed = NYCTFeed(line_id)
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
    print("Feed Read Success!")
    #set all pixels to white
    pixels1 = neopixel.NeoPixel(board.D18, 87, brightness=.25)
    pixels1.fill((15, 15, 15))
    #mother of all regex edits
    # Process the mapping
    for stop, (led_index, color) in stop_to_led_map.items():
        if stop in combined_array:
            pixels1[led_index] = color

else: 
    ()
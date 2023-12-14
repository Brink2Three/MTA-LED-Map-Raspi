#Combined project, once all parts are complete.
import time
#import board
#import neopixel
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
            else:
                pass

if __name__ == '__main__':
    main()
    for i in range(len(lines_array)): 
        combined_array.append(str(lines_array[i] + " " + stops_array[i]))
    #print(combined_array)
    #set all pixels to white
    #pixels1 = neopixel.NeoPixel(board.D18, 87, brightness=.15)
    #pixels1.fill((15, 15, 15))
    ###### 1 Line ##########
    if "1 66 St-Lincoln Center" in combined_array:
        print(84)
    else:
        pass
    if "1 59 St-Columbus Circle" in combined_array:
        print(82)
    else:
        pass
    if "1 50 St" in combined_array:
        print(70)
    else:
        pass
    if "1 Times Sq-42 St" in combined_array:
        print(67)
    else:
        pass
    if "1 34 St-Penn Station" in combined_array:
        print(61)
    else:
        pass
    if "1 28 St" in combined_array:
        print(58)
    else:
        pass
    if "1 23 St" in combined_array:
        print(52)
    else:
        pass
    if "1 18 St" in combined_array:
        print(50)
    else:
        pass
    if "1 14 St" in combined_array:
        print(48)
    else:
        pass
    if "1 Christopher St-Sheridan Sq" in combined_array:
        print(40)
    else:
        pass
    if "1 Houston St" in combined_array:
        print(34)
    else:
        pass
    if "1 Canal St" in combined_array:
        print(22)
    else:
        pass
    if "1 Franklin St" in combined_array:
        print(21)
    else:
        pass
    if "1 Chambers St" in combined_array:
        print(19)
    else:
        pass
    if "1 WTC Cortlandt" in combined_array:
        print(0)
    else:
        pass
    if "1 Rector St" in combined_array:
        print(5)
    else:
        pass
    if "1 South Ferry Loop" in combined_array:
        print(2)
    else:
        pass
    if "1 South Ferry" in combined_array:
        print(2)
    else:
        pass
    ###### 2 Line #######
    if "2 Park Place" in combined_array:
        print(64)
    else:
        pass
    if "2 Fulton St" in combined_array:
        print(65)
    else:
        pass
    if "2 Wall St" in combined_array:
        print(4)
    else:
        pass
    ##### 4 Line ######
    if "4 Fulton St" in combined_array:
        print(10)
    else:
        pass
    if "4 Wall St" in combined_array:
        print(7)
    else:
        pass
    if "4 Bowling Green" in combined_array:
        print(4)
    else:
        pass
##### 6 Line #####
    if "6 68 St-Hunter College" in combined_array:
        print(86)
    else:
        pass
    if "6 59 St" in combined_array:
        print(77)
    else:
        pass
    if "6 51 St" in combined_array:
        print(74)
    else:
        pass
    if "6 Grand Central-42 St" in combined_array:
        print(64)
    else:
        pass
    if "6 33 St" in combined_array:
        print(63)
    else:
        pass
    if "6 28 St" in combined_array:
        print(56)
    else:
        pass
    if "6 23 St" in combined_array:
        print(54)
    else:
        pass
    if "6 14 St-Union Sq" in combined_array:
        print(45)
    else:
        pass
    if "6 Astor Pl" in combined_array:
        print(42)
    else:
        pass
    if "6 Bleecker St" in combined_array:
        print(37)
    else:
        pass
    if "6 Spring St" in combined_array:
        print(32)
    else:
        pass
    if "6 Canal St" in combined_array:
        print(25)
    else:
        pass
    if "6 Brooklyn Bridge-City Hall" in combined_array:
        print(17)
    else:
        pass
##### 7 Line #####   
    if "7 Grand Central-42 St" in combined_array:
        print(64)
    else:
        pass
    if "7 5 Av" in combined_array:
        print(65)
    else:
        pass
    if "7 Times Sq-42 St" in combined_array:
        print(67)
    else:
        pass
    if "7 34 St-Hudson Yards" in combined_array:
        print(59)
    else:
        pass
##### S line (Times-GCS Shuttle) #####    
    if "S Grand Central-42 St" in combined_array:
        print(64)
    else:
        pass
    if "S Times Sq-42 St" in combined_array:
        print(67)
    else:
        pass
##### A Line #####
    if "A 59 St-Columbus Circle" in combined_array:
        print(83)
    else:
        pass
    if "A 50 St" in combined_array:
        print(69)
    else:
        pass
    if "A 42 St-Port Authority Bus Terminal" in combined_array:
        print(68)
    else:
        pass
    if "A 34 St-Penn Station" in combined_array:
        print(60)
    else:
        pass
    if "A 23 St" in combined_array:
        print(51)
    else:
        pass
    if "A 14 St" in combined_array:
        print(49)
    else:
        pass
    if "A W 4 St-Wash Sq" in combined_array:
        print(39)
    else:
        pass
    if "A Spring St" in combined_array:
        print(33)
    else:
        pass
    if "A Canal St" in combined_array:
        print(23)
    else:
        pass
    if "A Chambers St" in combined_array:
        print(20)
    else:
        pass
    if "A Fulton St" in combined_array:
        print(11)
    else:
        pass
##### E Line #####
    if "E World Trade Center" in combined_array:
        print(14)
    else:
        pass
##### B Line
    if "B Lexington Av/63 St" in combined_array:
        print(84)
    else:
        pass
    if "B 57 St" in combined_array:
        print(79)
    else:
        pass
##### D Line 
    if "D 7 Av" in combined_array:
        print(80)
    else:
        pass
    if "D 47-50 Sts-Rockefeller Ctr" in combined_array:
        print(72)
    else:
        pass
    if "D 42 St-Bryant Pk" in combined_array:
        print(66)
    else:
        pass
    if "D 34 St-Herald Sq" in combined_array:
        print(62)
    else:
        pass
    if "D 23 St" in combined_array:
        print(53)
    else:
        pass
    if "D 14 St" in combined_array:
        print(47)
    else:
        pass
    if "D W 4 St-Wash Sq" in combined_array:
        print(39)
    else:
        pass
    if "D Broadway-Lafayette St" in combined_array:
        print(36)
    else:
        pass
    if "D Grand St" in combined_array:
        print(27)
    else:
        pass
##### F Line #####
    if "F Lexington Av/53 St" in combined_array:
        print(75)
    else:
        pass
    if "F 5 Av/53 St" in combined_array:
        print(73)
    else:
        pass
    if "F 2 Av" in combined_array:
        print(38)
    else:
        pass
    if "F Delancey St-Essex St" in combined_array:
        print(30)
    else:
        pass
    if "F East Broadway" in combined_array:
        print(28)
    else:
        pass
##### J or Z trains labeled as their old M stops #####
    if "M Delancey St-Essex St" in combined_array:
        print(29)
    else:
        pass
    if "M Bowery" in combined_array:
        print(31)
    else:
        pass
    if "M Canal St" in combined_array:
        print(26)
    else:
        pass
    if "M Chambers St" in combined_array:
        print(18)
    else:
        pass
    if "M Fulton St" in combined_array:
        print(12)
    else:
        pass
    if "M Broad St" in combined_array:
        print(5)
    else:
        pass
##### J Line #####
# None in manhattan

##### L Line #####
    if "L 8 Av" in combined_array:
        print(49)
    else:
        pass
    if "L 6 Av" in combined_array:
        print(47)
    else:
        pass
    if "L 14 St-Union Sq" in combined_array:
        print(45)
    else:
        pass
    if "L 3 Av" in combined_array:
        print(44)
    else:
        pass
    if "L 1 Av" in combined_array:
        print(43)
    else:
        pass
##### N Line #####    
## None in Manhattan

##### Q Line #####
    if "Q Canal St" in combined_array:
        print(24)
    else:
        pass
##### R Line #####
    if "R Lexington Av/59 St" in combined_array:
        print(76)
    else:
        pass
    if "R 5 Av/59 St" in combined_array:
        print(78)
    else:
        pass
    if "R 57 St-7 Av" in combined_array:
        print(81)
    else:
        pass
    if "R 49 St" in combined_array:
        print(71)
    else:
        pass
    if "R Times Sq-42 St" in combined_array:
        print(67)
    else:
        pass
    if "R 34 St-Herald Sq" in combined_array:
        print(62)
    else:
        pass
    if "R 28 St" in combined_array:
        print(57)
    else:
        pass
    if "R 23 St" in combined_array:
        print(54)
    else:
        pass
    if "R 14 St-Union Sq" in combined_array:
        print(46)
    else:
        pass
    if "R 8 St-NYU" in combined_array:
        print(41)
    else:
        pass
    if "R Prince St" in combined_array:
        print(35)
    else:
        pass
    if "R Canal St" in combined_array:
        print(24)
    else:
        pass
    if "R City Hall" in combined_array:
        print(16)
    else:
        pass
    if "R Cortlandt St" in combined_array:
        print(9)
    else:
        pass
    if "R Rector St" in combined_array:
        print(6)
    else:
        pass
    if "R Whitehall St-South Ferry" in combined_array:
        print(3)
    else:
        ()
##### SF Line #####
# None in Manhattan
    # temp while testing to not use extra power
    time.sleep(10)
    #pixels1.fill((0, 0, 0))
    

else: 
    ()
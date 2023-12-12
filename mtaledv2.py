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
#pixels1 = neopixel.NeoPixel(board.D18, 180, brightness=.15)
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
    pixels1 = neopixel.NeoPixel(board.D18, 180, brightness=.15)
    pixels1.fill((15, 15, 15))
    #mother of all regex edits
    if "1 Van Cortlandt Park-242 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 238 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 231 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 Marble Hill-225 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 215 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 207 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 Dyckman St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 191 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 181 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 168 St-Washington Hts" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 157 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 145 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 137 St-City College" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 125 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 116 St-Columbia University" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 Cathedral Pkwy (110 St)" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 103 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 96 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 86 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 79 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 72 St" in combined_array:
        pixels1[999]= line_123
    else:
        pass
    if "1 66 St-Lincoln Center" in combined_array:
        pixels1[83]= line_123
    else:
        pass
    if "1 59 St-Columbus Circle" in combined_array:
        pixels1[81]= line_123
    else:
        pass
    if "1 50 St" in combined_array:
        pixels1[69]= line_123
    else:
        pass
    if "1 Times Sq-42 St" in combined_array:
        pixels1[66]= line_123
    else:
        pass
    if "1 34 St-Penn Station" in combined_array:
        pixels1[60]= line_123
    else:
        pass
    if "1 28 St" in combined_array:
        pixels1[57]= line_123
    else:
        pass
    if "1 23 St" in combined_array:
        pixels1[51]= line_123
    else:
        pass
    if "1 18 St" in combined_array:
        pixels1[49]= line_123
    else:
        pass
    if "1 14 St" in combined_array:
        pixels1[47]= line_123
    else:
        pass
    if "1 Christopher St-Sheridan Sq" in combined_array:
        pixels1[39]= line_123
    else:
        pass
    if "1 Houston St" in combined_array:
        pixels1[33]= line_123
    else:
        pass
    if "1 Canal St" in combined_array:
        pixels1[21]= line_123
    else:
        pass
    if "1 Franklin St" in combined_array:
        pixels1[20]= line_123
    else:
        pass
    if "1 Chambers St" in combined_array:
        pixels1[18]= line_123
    else:
        pass
    if "1 WTC Cortlandt" in combined_array:
        pixels1[36]= line_123
    else:
        pass
    if "1 Rector St" in combined_array:
        pixels1[5]= line_123
    else:
        pass
    if "1 South Ferry Loop" in combined_array:
        pixels1[1]= line_123
    else:
        pass
    if "1 South Ferry" in combined_array:
        pixels1[1]= line_123
    else:
        pass
    if "2 Wakefield-241 St" in combined_array:
        pixels1[40]= line_123
    else:
        pass
    if "2 Nereid Av" in combined_array:
        pixels1[41]= line_123
    else:
        pass
    if "2 233 St" in combined_array:
        pixels1[42]= line_123
    else:
        pass
    if "2 225 St" in combined_array:
        pixels1[43]= line_123
    else:
        pass
    if "2 219 St" in combined_array:
        pixels1[44]= line_123
    else:
        pass
    if "2 Gun Hill Rd" in combined_array:
        pixels1[45]= line_123
    else:
        pass
    if "2 Burke Av" in combined_array:
        pixels1[46]= line_123
    else:
        pass
    if "2 Allerton Av" in combined_array:
        pixels1[47]= line_123
    else:
        pass
    if "2 Pelham Pkwy" in combined_array:
        pixels1[48]= line_123
    else:
        pass
    if "2 Bronx Park East" in combined_array:
        pixels1[49]= line_123
    else:
        pass
    if "2 E 180 St" in combined_array:
        pixels1[50]= line_123
    else:
        pass
    if "2 West Farms Sq-E Tremont Av" in combined_array:
        pixels1[51]= line_123
    else:
        pass
    if "2 174 St" in combined_array:
        pixels1[52]= line_123
    else:
        pass
    if "2 Freeman St" in combined_array:
        pixels1[53]= line_123
    else:
        pass
    if "2 Simpson St" in combined_array:
        pixels1[54]= line_123
    else:
        pass
    if "2 Intervale Av" in combined_array:
        pixels1[55]= line_123
    else:
        pass
    if "2 Prospect Av" in combined_array:
        pixels1[56]= line_123
    else:
        pass
    if "2 Jackson Av" in combined_array:
        pixels1[57]= line_123
    else:
        pass
    if "2 3 Av-149 St" in combined_array:
        pixels1[58]= line_123
    else:
        pass
    if "2 149 St-Grand Concourse" in combined_array:
        pixels1[59]= line_123
    else:
        pass
    if "2 135 St" in combined_array:
        pixels1[60]= line_123
    else:
        pass
    if "2 125 St" in combined_array:
        pixels1[61]= line_123
    else:
        pass
    if "2 116 St" in combined_array:
        pixels1[62]= line_123
    else:
        pass
    if "2 Central Park North (110 St)" in combined_array:
        pixels1[63]= line_123
    else:
        pass
    if "2 Park Place" in combined_array:
        pixels1[64]= line_123
    else:
        pass
    if "2 Fulton St" in combined_array:
        pixels1[65]= line_123
    else:
        pass
    if "2 Wall St" in combined_array:
        pixels1[4]= line_123
    else:
        pass
    if "2 Clark St" in combined_array:
        pixels1[67]= line_123
    else:
        pass
    if "2 Borough Hall" in combined_array:
        pixels1[68]= line_123
    else:
        pass
    if "2 Hoyt St" in combined_array:
        pixels1[69]= line_123
    else:
        pass
    if "2 Nevins St" in combined_array:
        pixels1[70]= line_123
    else:
        pass
    if "2 Atlantic Av-Barclays Ctr" in combined_array:
        pixels1[71]= line_123
    else:
        pass
    if "2 Bergen St" in combined_array:
        pixels1[72]= line_123
    else:
        pass
    if "2 Grand Army Plaza" in combined_array:
        pixels1[73]= line_123
    else:
        pass
    if "2 Eastern Pkwy-Brooklyn Museum" in combined_array:
        pixels1[74]= line_123
    else:
        pass
    if "2 Franklin Av-Medgar Evers College" in combined_array:
        pixels1[75]= line_123
    else:
        pass
    if "2 President St-Medgar Evers College" in combined_array:
        pixels1[76]= line_123
    else:
        pass
    if "2 Sterling St" in combined_array:
        pixels1[77]= line_123
    else:
        pass
    if "2 Winthrop St" in combined_array:
        pixels1[78]= line_123
    else:
        pass
    if "2 Church Av" in combined_array:
        pixels1[79]= line_123
    else:
        pass
    if "2 Beverly Rd" in combined_array:
        pixels1[80]= line_123
    else:
        pass
    if "2 Newkirk Av-Little Haiti" in combined_array:
        pixels1[81]= line_123
    else:
        pass
    if "2 Flatbush Av-Brooklyn College" in combined_array:
        pixels1[82]= line_123
    else:
        pass
    if "2 Nostrand Av" in combined_array:
        pixels1[83]= line_123
    else:
        pass
    if "2 Kingston Av" in combined_array:
        pixels1[84]= line_123
    else:
        pass
    if "2 Crown Hts-Utica Av" in combined_array:
        pixels1[85]= line_123
    else:
        pass
    if "2 Sutter Av-Rutland Rd" in combined_array:
        pixels1[86]= line_123
    else:
        pass
    if "2 Saratoga Av" in combined_array:
        pixels1[87]= line_123
    else:
        pass
    if "2 Rockaway Av" in combined_array:
        pixels1[88]= line_123
    else:
        pass
    if "2 Junius St" in combined_array:
        pixels1[89]= line_123
    else:
        pass
    if "2 Pennsylvania Av" in combined_array:
        pixels1[90]= line_123
    else:
        pass
    if "2 Van Siclen Av" in combined_array:
        pixels1[91]= line_123
    else:
        pass
    if "2 New Lots Av" in combined_array:
        pixels1[92]= line_123
    else:
        pass
    if "3 Harlem-148 St" in combined_array:
        pixels1[93]= line_123
    else:
        pass
    if "3 145 St" in combined_array:
        pixels1[94]= line_123
    else:
        pass
    if "4 Woodlawn" in combined_array:
        pixels1[95]= line_456
    else:
        pass
    if "4 Mosholu Pkwy" in combined_array:
        pixels1[96]= line_456
    else:
        pass
    if "4 Bedford Park Blvd-Lehman College" in combined_array:
        pixels1[97]= line_456
    else:
        pass
    if "4 Kingsbridge Rd" in combined_array:
        pixels1[98]= line_456
    else:
        pass
    if "4 Fordham Rd" in combined_array:
        pixels1[99]= line_456
    else:
        pass
    if "4 183 St" in combined_array:
        pixels1[100]= line_456
    else:
        pass
    if "4 Burnside Av" in combined_array:
        pixels1[101]= line_456
    else:
        pass
    if "4 176 St" in combined_array:
        pixels1[102]= line_456
    else:
        pass
    if "4 Mt Eden Av" in combined_array:
        pixels1[103]= line_456
    else:
        pass
    if "4 170 St" in combined_array:
        pixels1[104]= line_456
    else:
        pass
    if "4 167 St" in combined_array:
        pixels1[105]= line_456
    else:
        pass
    if "4 161 St-Yankee Stadium" in combined_array:
        pixels1[106]= line_456
    else:
        pass
    if "4 149 St-Grand Concourse" in combined_array:
        pixels1[107]= line_456
    else:
        pass
    if "4 138 St-Grand Concourse" in combined_array:
        pixels1[108]= line_456
    else:
        pass
    if "4 Fulton St" in combined_array:
        pixels1[109]= line_456
    else:
        pass
    if "4 Wall St" in combined_array:
        pixels1[6]= line_456
    else:
        pass
    if "4 Bowling Green" in combined_array:
        pixels1[3]= line_456
    else:
        pass
    if "4 Borough Hall" in combined_array:
        pixels1[112]= line_456
    else:
        pass
    if "5 Eastchester-Dyre Av" in combined_array:
        pixels1[113]= line_456
    else:
        pass
    if "5 Baychester Av" in combined_array:
        pixels1[114]= line_456
    else:
        pass
    if "5 Gun Hill Rd" in combined_array:
        pixels1[115]= line_456
    else:
        pass
    if "5 Pelham Pkwy" in combined_array:
        pixels1[116]= line_456
    else:
        pass
    if "5 Morris Park" in combined_array:
        pixels1[117]= line_456
    else:
        pass
    if "6 Pelham Bay Park" in combined_array:
        pixels1[118]= line_456
    else:
        pass
    if "6 Buhre Av" in combined_array:
        pixels1[119]= line_456
    else:
        pass
    if "6 Middletown Rd" in combined_array:
        pixels1[120]= line_456
    else:
        pass
    if "6 Westchester Sq-E Tremont Av" in combined_array:
        pixels1[121]= line_456
    else:
        pass
    if "6 Zerega Av" in combined_array:
        pixels1[122]= line_456
    else:
        pass
    if "6 Castle Hill Av" in combined_array:
        pixels1[123]= line_456
    else:
        pass
    if "6 Parkchester" in combined_array:
        pixels1[124]= line_456
    else:
        pass
    if "6 St Lawrence Av" in combined_array:
        pixels1[125]= line_456
    else:
        pass
    if "6 Morrison Av-Soundview" in combined_array:
        pixels1[126]= line_456
    else:
        pass
    if "6 Elder Av" in combined_array:
        pixels1[127]= line_456
    else:
        pass
    if "6 Whitlock Av" in combined_array:
        pixels1[128]= line_456
    else:
        pass
    if "6 Hunts Point Av" in combined_array:
        pixels1[129]= line_456
    else:
        pass
    if "6 Longwood Av" in combined_array:
        pixels1[130]= line_456
    else:
        pass
    if "6 E 149 St" in combined_array:
        pixels1[131]= line_456
    else:
        pass
    if "6 E 143 St-St Mary's St" in combined_array:
        pixels1[132]= line_456
    else:
        pass
    if "6 Cypress Av" in combined_array:
        pixels1[133]= line_456
    else:
        pass
    if "6 Brook Av" in combined_array:
        pixels1[134]= line_456
    else:
        pass
    if "6 3 Av-138 St" in combined_array:
        pixels1[135]= line_456
    else:
        pass
    if "6 125 St" in combined_array:
        pixels1[136]= line_456
    else:
        pass
    if "6 116 St" in combined_array:
        pixels1[137]= line_456
    else:
        pass
    if "6 110 St" in combined_array:
        pixels1[138]= line_456
    else:
        pass
    if "6 103 St" in combined_array:
        pixels1[139]= line_456
    else:
        pass
    if "6 96 St" in combined_array:
        pixels1[140]= line_456
    else:
        pass
    if "6 86 St" in combined_array:
        pixels1[141]= line_456
    else:
        pass
    if "6 77 St" in combined_array:
        pixels1[142]= line_456
    else:
        pass
    if "6 68 St-Hunter College" in combined_array:
        pixels1[143]= line_456
    else:
        pass
    if "6 59 St" in combined_array:
        pixels1[144]= line_456
    else:
        pass
    if "6 51 St" in combined_array:
        pixels1[145]= line_456
    else:
        pass
    if "6 Grand Central-42 St" in combined_array:
        pixels1[146]= line_456
    else:
        pass
    if "6 33 St" in combined_array:
        pixels1[147]= line_456
    else:
        pass
    if "6 28 St" in combined_array:
        pixels1[148]= line_456
    else:
        pass
    if "6 23 St" in combined_array:
        pixels1[149]= line_456
    else:
        pass
    if "6 14 St-Union Sq" in combined_array:
        pixels1[150]= line_456
    else:
        pass
    if "6 Astor Pl" in combined_array:
        pixels1[151]= line_456
    else:
        pass
    if "6 Bleecker St" in combined_array:
        pixels1[152]= line_456
    else:
        pass
    if "6 Spring St" in combined_array:
        pixels1[153]= line_456
    else:
        pass
    if "6 Canal St" in combined_array:
        pixels1[154]= line_456
    else:
        pass
    if "6 Brooklyn Bridge-City Hall" in combined_array:
        pixels1[155]= line_456
    else:
        pass
    if "7 Flushing-Main St" in combined_array:
        pixels1[156]= line_7
    else:
        pass
    if "7 Mets-Willets Point" in combined_array:
        pixels1[157]= line_7
    else:
        pass
    if "7 111 St" in combined_array:
        pixels1[158]= line_7
    else:
        pass
    if "7 103 St-Corona Plaza" in combined_array:
        pixels1[159]= line_7
    else:
        pass
    if "7 Junction Blvd" in combined_array:
        pixels1[160]= line_7
    else:
        pass
    if "7 90 St-Elmhurst Av" in combined_array:
        pixels1[161]= line_7
    else:
        pass
    if "7 82 St-Jackson Hts" in combined_array:
        pixels1[162]= line_7
    else:
        pass
    if "7 74 St-Broadway" in combined_array:
        pixels1[163]= line_7
    else:
        pass
    if "7 69 St" in combined_array:
        pixels1[164]= line_7
    else:
        pass
    if "7 61 St-Woodside" in combined_array:
        pixels1[165]= line_7
    else:
        pass
    if "7 52 St" in combined_array:
        pixels1[166]= line_7
    else:
        pass
    if "7 46 St-Bliss St" in combined_array:
        pixels1[167]= line_7
    else:
        pass
    if "7 40 St-Lowery St" in combined_array:
        pixels1[168]= line_7
    else:
        pass
    if "7 33 St-Rawson St" in combined_array:
        pixels1[169]= line_7
    else:
        pass
    if "7 Queensboro Plaza" in combined_array:
        pixels1[170]= line_7
    else:
        pass
    if "7 Court Sq" in combined_array:
        pixels1[171]= line_7
    else:
        pass
    if "7 Hunters Point Av" in combined_array:
        pixels1[172]= line_7
    else:
        pass
    if "7 Vernon Blvd-Jackson Av" in combined_array:
        pixels1[173]= line_7
    else:
        pass
    if "7 Grand Central-42 St" in combined_array:
        pixels1[174]= line_7
    else:
        pass
    if "7 5 Av" in combined_array:
        pixels1[175]= line_7
    else:
        pass
    if "7 Times Sq-42 St" in combined_array:
        pixels1[176]= line_7
    else:
        pass
    if "7 34 St-Hudson Yards" in combined_array:
        pixels1[58]= line_7
    else:
        pass
    if "S Grand Central-42 St" in combined_array:
        pixels1[178]= line_ls
    else:
        pass
    if "S Times Sq-42 St" in combined_array:
        pixels1[179]= line_ls
    else:
        pass
    if "A Inwood-207 St" in combined_array:
        pixels1[180]= line_ace
    else:
        pass
    if "A Dyckman St" in combined_array:
        pixels1[181]= line_ace
    else:
        pass
    if "A 190 St" in combined_array:
        pixels1[182]= line_ace
    else:
        pass
    if "A 181 St" in combined_array:
        pixels1[183]= line_ace
    else:
        pass
    if "A 175 St" in combined_array:
        pixels1[184]= line_ace
    else:
        pass
    if "A 168 St" in combined_array:
        pixels1[185]= line_ace
    else:
        pass
    if "A 163 St-Amsterdam Av" in combined_array:
        pixels1[186]= line_ace
    else:
        pass
    if "A 155 St" in combined_array:
        pixels1[187]= line_ace
    else:
        pass
    if "A 145 St" in combined_array:
        pixels1[188]= line_ace
    else:
        pass
    if "A 135 St" in combined_array:
        pixels1[189]= line_ace
    else:
        pass
    if "A 125 St" in combined_array:
        pixels1[190]= line_ace
    else:
        pass
    if "A 116 St" in combined_array:
        pixels1[191]= line_ace
    else:
        pass
    if "A Cathedral Pkwy (110 St)" in combined_array:
        pixels1[192]= line_ace
    else:
        pass
    if "A 103 St" in combined_array:
        pixels1[193]= line_ace
    else:
        pass
    if "A 96 St" in combined_array:
        pixels1[194]= line_ace
    else:
        pass
    if "A 86 St" in combined_array:
        pixels1[195]= line_ace
    else:
        pass
    if "A 81 St-Museum of Natural History" in combined_array:
        pixels1[196]= line_ace
    else:
        pass
    if "A 72 St" in combined_array:
        pixels1[197]= line_ace
    else:
        pass
    if "A 59 St-Columbus Circle" in combined_array:
        pixels1[198]= line_ace
    else:
        pass
    if "A 50 St" in combined_array:
        pixels1[199]= line_ace
    else:
        pass
    if "A 42 St-Port Authority Bus Terminal" in combined_array:
        pixels1[200]= line_ace
    else:
        pass
    if "A 34 St-Penn Station" in combined_array:
        pixels1[59]= line_ace
    else:
        pass
    if "A 23 St" in combined_array:
        pixels1[202]= line_ace
    else:
        pass
    if "A 14 St" in combined_array:
        pixels1[203]= line_ace
    else:
        pass
    if "A W 4 St-Wash Sq" in combined_array:
        pixels1[204]= line_ace
    else:
        pass
    if "A Spring St" in combined_array:
        pixels1[205]= line_ace
    else:
        pass
    if "A Canal St" in combined_array:
        pixels1[206]= line_ace
    else:
        pass
    if "A Chambers St" in combined_array:
        pixels1[207]= line_ace
    else:
        pass
    if "A Fulton St" in combined_array:
        pixels1[208]= line_ace
    else:
        pass
    if "A High St" in combined_array:
        pixels1[209]= line_ace
    else:
        pass
    if "A Jay St-MetroTech" in combined_array:
        pixels1[210]= line_ace
    else:
        pass
    if "A Hoyt-Schermerhorn Sts" in combined_array:
        pixels1[211]= line_ace
    else:
        pass
    if "A Lafayette Av" in combined_array:
        pixels1[212]= line_ace
    else:
        pass
    if "A Clinton-Washington Avs" in combined_array:
        pixels1[213]= line_ace
    else:
        pass
    if "A Franklin Av" in combined_array:
        pixels1[214]= line_ace
    else:
        pass
    if "A Nostrand Av" in combined_array:
        pixels1[215]= line_ace
    else:
        pass
    if "A Kingston-Throop Avs" in combined_array:
        pixels1[216]= line_ace
    else:
        pass
    if "A Utica Av" in combined_array:
        pixels1[217]= line_ace
    else:
        pass
    if "A Ralph Av" in combined_array:
        pixels1[218]= line_ace
    else:
        pass
    if "A Rockaway Av" in combined_array:
        pixels1[219]= line_ace
    else:
        pass
    if "A Broadway Junction" in combined_array:
        pixels1[220]= line_ace
    else:
        pass
    if "A Liberty Av" in combined_array:
        pixels1[221]= line_ace
    else:
        pass
    if "A Van Siclen Av" in combined_array:
        pixels1[222]= line_ace
    else:
        pass
    if "A Shepherd Av" in combined_array:
        pixels1[223]= line_ace
    else:
        pass
    if "A Euclid Av" in combined_array:
        pixels1[224]= line_ace
    else:
        pass
    if "A Grant Av" in combined_array:
        pixels1[225]= line_ace
    else:
        pass
    if "A 80 St" in combined_array:
        pixels1[226]= line_ace
    else:
        pass
    if "A 88 St" in combined_array:
        pixels1[227]= line_ace
    else:
        pass
    if "A Rockaway Blvd" in combined_array:
        pixels1[228]= line_ace
    else:
        pass
    if "A 104 St" in combined_array:
        pixels1[229]= line_ace
    else:
        pass
    if "A 111 St" in combined_array:
        pixels1[230]= line_ace
    else:
        pass
    if "A Ozone Park-Lefferts Blvd" in combined_array:
        pixels1[231]= line_ace
    else:
        pass
    if "B 21 St-Queensbridge" in combined_array:
        pixels1[232]= line_bdfm
    else:
        pass
    if "B Roosevelt Island" in combined_array:
        pixels1[233]= line_bdfm
    else:
        pass
    if "B Lexington Av/63 St" in combined_array:
        pixels1[234]= line_bdfm
    else:
        pass
    if "B 57 St" in combined_array:
        pixels1[235]= line_bdfm
    else:
        pass
    if "B 9 Av" in combined_array:
        pixels1[236]= line_bdfm
    else:
        pass
    if "B Fort Hamilton Pkwy" in combined_array:
        pixels1[237]= line_bdfm
    else:
        pass
    if "B 50 St" in combined_array:
        pixels1[238]= line_bdfm
    else:
        pass
    if "B 55 St" in combined_array:
        pixels1[239]= line_bdfm
    else:
        pass
    if "B 62 St" in combined_array:
        pixels1[240]= line_bdfm
    else:
        pass
    if "B 71 St" in combined_array:
        pixels1[241]= line_bdfm
    else:
        pass
    if "B 79 St" in combined_array:
        pixels1[242]= line_bdfm
    else:
        pass
    if "B 18 Av" in combined_array:
        pixels1[243]= line_bdfm
    else:
        pass
    if "B 20 Av" in combined_array:
        pixels1[244]= line_bdfm
    else:
        pass
    if "B Bay Pkwy" in combined_array:
        pixels1[245]= line_bdfm
    else:
        pass
    if "B 25 Av" in combined_array:
        pixels1[246]= line_bdfm
    else:
        pass
    if "B Bay 50 St" in combined_array:
        pixels1[247]= line_bdfm
    else:
        pass
    if "D Norwood-205 St" in combined_array:
        pixels1[248]= line_bdfm
    else:
        pass
    if "D Bedford Park Blvd" in combined_array:
        pixels1[249]= line_bdfm
    else:
        pass
    if "D Kingsbridge Rd" in combined_array:
        pixels1[250]= line_bdfm
    else:
        pass
    if "D Fordham Rd" in combined_array:
        pixels1[251]= line_bdfm
    else:
        pass
    if "D 182-183 Sts" in combined_array:
        pixels1[252]= line_bdfm
    else:
        pass
    if "D Tremont Av" in combined_array:
        pixels1[253]= line_bdfm
    else:
        pass
    if "D 174-175 Sts" in combined_array:
        pixels1[254]= line_bdfm
    else:
        pass
    if "D 170 St" in combined_array:
        pixels1[255]= line_bdfm
    else:
        pass
    if "D 167 St" in combined_array:
        pixels1[256]= line_bdfm
    else:
        pass
    if "D 161 St-Yankee Stadium" in combined_array:
        pixels1[257]= line_bdfm
    else:
        pass
    if "D 155 St" in combined_array:
        pixels1[258]= line_bdfm
    else:
        pass
    if "D 145 St" in combined_array:
        pixels1[259]= line_bdfm
    else:
        pass
    if "D 7 Av" in combined_array:
        pixels1[260]= line_bdfm
    else:
        pass
    if "D 47-50 Sts-Rockefeller Ctr" in combined_array:
        pixels1[261]= line_bdfm
    else:
        pass
    if "D 42 St-Bryant Pk" in combined_array:
        pixels1[262]= line_bdfm
    else:
        pass
    if "D 34 St-Herald Sq" in combined_array:
        pixels1[263]= line_bdfm
    else:
        pass
    if "D 23 St" in combined_array:
        pixels1[264]= line_bdfm
    else:
        pass
    if "D 14 St" in combined_array:
        pixels1[265]= line_bdfm
    else:
        pass
    if "D W 4 St-Wash Sq" in combined_array:
        pixels1[266]= line_bdfm
    else:
        pass
    if "D Broadway-Lafayette St" in combined_array:
        pixels1[267]= line_bdfm
    else:
        pass
    if "D Grand St" in combined_array:
        pixels1[268]= line_bdfm
    else:
        pass
    if "D Atlantic Av-Barclays Ctr" in combined_array:
        pixels1[269]= line_bdfm
    else:
        pass
    if "D Prospect Park" in combined_array:
        pixels1[270]= line_bdfm
    else:
        pass
    if "D Parkside Av" in combined_array:
        pixels1[271]= line_bdfm
    else:
        pass
    if "D Church Av" in combined_array:
        pixels1[272]= line_bdfm
    else:
        pass
    if "D Beverley Rd" in combined_array:
        pixels1[273]= line_bdfm
    else:
        pass
    if "D Cortelyou Rd" in combined_array:
        pixels1[274]= line_bdfm
    else:
        pass
    if "D Newkirk Plaza" in combined_array:
        pixels1[275]= line_bdfm
    else:
        pass
    if "D Avenue H" in combined_array:
        pixels1[276]= line_bdfm
    else:
        pass
    if "D Avenue J" in combined_array:
        pixels1[277]= line_bdfm
    else:
        pass
    if "D Avenue M" in combined_array:
        pixels1[278]= line_bdfm
    else:
        pass
    if "D Kings Hwy" in combined_array:
        pixels1[279]= line_bdfm
    else:
        pass
    if "D Avenue U" in combined_array:
        pixels1[280]= line_bdfm
    else:
        pass
    if "D Neck Rd" in combined_array:
        pixels1[281]= line_bdfm
    else:
        pass
    if "D Sheepshead Bay" in combined_array:
        pixels1[282]= line_bdfm
    else:
        pass
    if "D Brighton Beach" in combined_array:
        pixels1[283]= line_bdfm
    else:
        pass
    if "D Ocean Pkwy" in combined_array:
        pixels1[284]= line_bdfm
    else:
        pass
    if "D W 8 St-NY Aquarium" in combined_array:
        pixels1[285]= line_bdfm
    else:
        pass
    if "D Coney Island-Stillwell Av" in combined_array:
        pixels1[286]= line_bdfm
    else:
        pass
    if "E World Trade Center" in combined_array:
        pixels1[287]= line_ace
    else:
        pass
    if "F Jamaica-179 St" in combined_array:
        pixels1[288]= line_bdfm
    else:
        pass
    if "F 169 St" in combined_array:
        pixels1[289]= line_bdfm
    else:
        pass
    if "F Parsons Blvd" in combined_array:
        pixels1[290]= line_bdfm
    else:
        pass
    if "F Sutphin Blvd" in combined_array:
        pixels1[291]= line_bdfm
    else:
        pass
    if "F Briarwood" in combined_array:
        pixels1[292]= line_bdfm
    else:
        pass
    if "F Kew Gardens-Union Tpke" in combined_array:
        pixels1[293]= line_bdfm
    else:
        pass
    if "F 75 Av" in combined_array:
        pixels1[294]= line_bdfm
    else:
        pass
    if "F Court Sq-23 St" in combined_array:
        pixels1[295]= line_bdfm
    else:
        pass
    if "F Lexington Av/53 St" in combined_array:
        pixels1[296]= line_bdfm
    else:
        pass
    if "F 5 Av/53 St" in combined_array:
        pixels1[297]= line_bdfm
    else:
        pass
    if "F 2 Av" in combined_array:
        pixels1[298]= line_bdfm
    else:
        pass
    if "F Delancey St-Essex St" in combined_array:
        pixels1[299]= line_bdfm
    else:
        pass
    if "F East Broadway" in combined_array:
        pixels1[300]= line_bdfm
    else:
        pass
    if "F York St" in combined_array:
        pixels1[301]= line_bdfm
    else:
        pass
    if "F Bergen St" in combined_array:
        pixels1[302]= line_bdfm
    else:
        pass
    if "F Carroll St" in combined_array:
        pixels1[303]= line_bdfm
    else:
        pass
    if "F Smith-9 Sts" in combined_array:
        pixels1[304]= line_bdfm
    else:
        pass
    if "F 4 Av-9 St" in combined_array:
        pixels1[305]= line_bdfm
    else:
        pass
    if "F 7 Av" in combined_array:
        pixels1[306]= line_bdfm
    else:
        pass
    if "F 15 St-Prospect Park" in combined_array:
        pixels1[307]= line_bdfm
    else:
        pass
    if "F Fort Hamilton Pkwy" in combined_array:
        pixels1[308]= line_bdfm
    else:
        pass
    if "F Church Av" in combined_array:
        pixels1[309]= line_bdfm
    else:
        pass
    if "F Ditmas Av" in combined_array:
        pixels1[310]= line_bdfm
    else:
        pass
    if "F 18 Av" in combined_array:
        pixels1[311]= line_bdfm
    else:
        pass
    if "F Avenue I" in combined_array:
        pixels1[312]= line_bdfm
    else:
        pass
    if "F Bay Pkwy" in combined_array:
        pixels1[313]= line_bdfm
    else:
        pass
    if "F Avenue N" in combined_array:
        pixels1[314]= line_bdfm
    else:
        pass
    if "F Avenue P" in combined_array:
        pixels1[315]= line_bdfm
    else:
        pass
    if "F Kings Hwy" in combined_array:
        pixels1[316]= line_bdfm
    else:
        pass
    if "F Avenue U" in combined_array:
        pixels1[317]= line_bdfm
    else:
        pass
    if "F Avenue X" in combined_array:
        pixels1[318]= line_bdfm
    else:
        pass
    if "F Neptune Av" in combined_array:
        pixels1[319]= line_bdfm
    else:
        pass
    if "G Jamaica Center-Parsons/Archer" in combined_array:
        pixels1[320]= line_g
    else:
        pass
    if "G Sutphin Blvd-Archer Av-JFK Airport" in combined_array:
        pixels1[321]= line_g
    else:
        pass
    if "G Jamaica-Van Wyck" in combined_array:
        pixels1[322]= line_g
    else:
        pass
    if "G Forest Hills-71 Av" in combined_array:
        pixels1[323]= line_g
    else:
        pass
    if "G 67 Av" in combined_array:
        pixels1[324]= line_g
    else:
        pass
    if "G 63 Dr-Rego Park" in combined_array:
        pixels1[325]= line_g
    else:
        pass
    if "G Woodhaven Blvd" in combined_array:
        pixels1[326]= line_g
    else:
        pass
    if "G Grand Av-Newtown" in combined_array:
        pixels1[327]= line_g
    else:
        pass
    if "G Elmhurst Av" in combined_array:
        pixels1[328]= line_g
    else:
        pass
    if "G Jackson Hts-Roosevelt Av" in combined_array:
        pixels1[329]= line_g
    else:
        pass
    if "G 65 St" in combined_array:
        pixels1[330]= line_g
    else:
        pass
    if "G Northern Blvd" in combined_array:
        pixels1[331]= line_g
    else:
        pass
    if "G 46 St" in combined_array:
        pixels1[332]= line_g
    else:
        pass
    if "G Steinway St" in combined_array:
        pixels1[333]= line_g
    else:
        pass
    if "G 36 St" in combined_array:
        pixels1[334]= line_g
    else:
        pass
    if "G Queens Plaza" in combined_array:
        pixels1[335]= line_g
    else:
        pass
    if "G Court Sq" in combined_array:
        pixels1[336]= line_g
    else:
        pass
    if "G 21 St" in combined_array:
        pixels1[337]= line_g
    else:
        pass
    if "G Greenpoint Av" in combined_array:
        pixels1[338]= line_g
    else:
        pass
    if "G Nassau Av" in combined_array:
        pixels1[339]= line_g
    else:
        pass
    if "G Metropolitan Av" in combined_array:
        pixels1[340]= line_g
    else:
        pass
    if "G Broadway" in combined_array:
        pixels1[341]= line_g
    else:
        pass
    if "G Flushing Av" in combined_array:
        pixels1[342]= line_g
    else:
        pass
    if "G Myrtle-Willoughby Avs" in combined_array:
        pixels1[343]= line_g
    else:
        pass
    if "G Bedford-Nostrand Avs" in combined_array:
        pixels1[344]= line_g
    else:
        pass
    if "G Classon Av" in combined_array:
        pixels1[345]= line_g
    else:
        pass
    if "G Clinton-Washington Avs" in combined_array:
        pixels1[346]= line_g
    else:
        pass
    if "G Fulton St" in combined_array:
        pixels1[347]= line_g
    else:
        pass
    if "H Aqueduct Racetrack" in combined_array:
        pixels1[348]= line_h
    else:
        pass
    if "H Aqueduct-N Conduit Av" in combined_array:
        pixels1[349]= line_h
    else:
        pass
    if "H Howard Beach-JFK Airport" in combined_array:
        pixels1[350]= line_h
    else:
        pass
    if "H Broad Channel" in combined_array:
        pixels1[351]= line_h
    else:
        pass
    if "H Beach 67 St" in combined_array:
        pixels1[352]= line_h
    else:
        pass
    if "H Beach 60 St" in combined_array:
        pixels1[353]= line_h
    else:
        pass
    if "H Beach 44 St" in combined_array:
        pixels1[354]= line_h
    else:
        pass
    if "H Beach 36 St" in combined_array:
        pixels1[355]= line_h
    else:
        pass
    if "H Beach 25 St" in combined_array:
        pixels1[356]= line_h
    else:
        pass
    if "H Far Rockaway-Mott Av" in combined_array:
        pixels1[357]= line_h
    else:
        pass
    if "H Beach 90 St" in combined_array:
        pixels1[358]= line_h
    else:
        pass
    if "H Beach 98 St" in combined_array:
        pixels1[359]= line_h
    else:
        pass
    if "H Beach 105 St" in combined_array:
        pixels1[360]= line_h
    else:
        pass
    if "H Rockaway Park-Beach 116 St" in combined_array:
        pixels1[361]= line_h
    else:
        pass
    if "J 121 St" in combined_array:
        pixels1[362]= line_jz
    else:
        pass
    if "J 111 St" in combined_array:
        pixels1[363]= line_jz
    else:
        pass
    if "J 104 St" in combined_array:
        pixels1[364]= line_jz
    else:
        pass
    if "J Woodhaven Blvd" in combined_array:
        pixels1[365]= line_jz
    else:
        pass
    if "J 85 St-Forest Pkwy" in combined_array:
        pixels1[366]= line_jz
    else:
        pass
    if "J 75 St-Elderts Ln" in combined_array:
        pixels1[367]= line_jz
    else:
        pass
    if "J Cypress Hills" in combined_array:
        pixels1[368]= line_jz
    else:
        pass
    if "J Crescent St" in combined_array:
        pixels1[369]= line_jz
    else:
        pass
    if "J Norwood Av" in combined_array:
        pixels1[370]= line_jz
    else:
        pass
    if "J Cleveland St" in combined_array:
        pixels1[371]= line_jz
    else:
        pass
    if "J Van Siclen Av" in combined_array:
        pixels1[372]= line_jz
    else:
        pass
    if "J Alabama Av" in combined_array:
        pixels1[373]= line_jz
    else:
        pass
    if "J Broadway Junction" in combined_array:
        pixels1[374]= line_jz
    else:
        pass
    if "J Chauncey St" in combined_array:
        pixels1[375]= line_jz
    else:
        pass
    if "J Halsey St" in combined_array:
        pixels1[376]= line_jz
    else:
        pass
    if "J Gates Av" in combined_array:
        pixels1[377]= line_jz
    else:
        pass
    if "J Kosciuszko St" in combined_array:
        pixels1[378]= line_jz
    else:
        pass
    if "L 8 Av" in combined_array:
        pixels1[379]= line_ls
    else:
        pass
    if "L 6 Av" in combined_array:
        pixels1[380]= line_ls
    else:
        pass
    if "L 14 St-Union Sq" in combined_array:
        pixels1[381]= line_ls
    else:
        pass
    if "L 3 Av" in combined_array:
        pixels1[382]= line_ls
    else:
        pass
    if "L 1 Av" in combined_array:
        pixels1[383]= line_ls
    else:
        pass
    if "L Bedford Av" in combined_array:
        pixels1[384]= line_ls
    else:
        pass
    if "L Lorimer St" in combined_array:
        pixels1[385]= line_ls
    else:
        pass
    if "L Graham Av" in combined_array:
        pixels1[386]= line_ls
    else:
        pass
    if "L Grand St" in combined_array:
        pixels1[387]= line_ls
    else:
        pass
    if "L Montrose Av" in combined_array:
        pixels1[388]= line_ls
    else:
        pass
    if "L Morgan Av" in combined_array:
        pixels1[389]= line_ls
    else:
        pass
    if "L Jefferson St" in combined_array:
        pixels1[390]= line_ls
    else:
        pass
    if "L DeKalb Av" in combined_array:
        pixels1[391]= line_ls
    else:
        pass
    if "L Myrtle-Wyckoff Avs" in combined_array:
        pixels1[392]= line_ls
    else:
        pass
    if "L Halsey St" in combined_array:
        pixels1[393]= line_ls
    else:
        pass
    if "L Wilson Av" in combined_array:
        pixels1[394]= line_ls
    else:
        pass
    if "L Bushwick Av-Aberdeen St" in combined_array:
        pixels1[395]= line_ls
    else:
        pass
    if "L Broadway Junction" in combined_array:
        pixels1[396]= line_ls
    else:
        pass
    if "L Atlantic Av" in combined_array:
        pixels1[397]= line_ls
    else:
        pass
    if "L Sutter Av" in combined_array:
        pixels1[398]= line_ls
    else:
        pass
    if "L Livonia Av" in combined_array:
        pixels1[399]= line_ls
    else:
        pass
    if "L New Lots Av" in combined_array:
        pixels1[400]= line_ls
    else:
        pass
    if "L East 105 St" in combined_array:
        pixels1[401]= line_ls
    else:
        pass
    if "L Canarsie-Rockaway Pkwy" in combined_array:
        pixels1[402]= line_ls
    else:
        pass
    if "M Middle Village-Metropolitan Av" in combined_array:
        pixels1[403]= line_bdfm
    else:
        pass
    if "M Fresh Pond Rd" in combined_array:
        pixels1[404]= line_bdfm
    else:
        pass
    if "M Forest Av" in combined_array:
        pixels1[405]= line_bdfm
    else:
        pass
    if "M Seneca Av" in combined_array:
        pixels1[406]= line_bdfm
    else:
        pass
    if "M Myrtle-Wyckoff Avs" in combined_array:
        pixels1[407]= line_bdfm
    else:
        pass
    if "M Knickerbocker Av" in combined_array:
        pixels1[408]= line_bdfm
    else:
        pass
    if "M Central Av" in combined_array:
        pixels1[409]= line_bdfm
    else:
        pass
    if "M Myrtle Av" in combined_array:
        pixels1[410]= line_bdfm
    else:
        pass
    if "M Flushing Av" in combined_array:
        pixels1[411]= line_bdfm
    else:
        pass
    if "M Lorimer St" in combined_array:
        pixels1[412]= line_bdfm
    else:
        pass
    if "M Hewes St" in combined_array:
        pixels1[413]= line_bdfm
    else:
        pass
    if "M Marcy Av" in combined_array:
        pixels1[414]= line_bdfm
    else:
        pass
    if "M Delancey St-Essex St" in combined_array:
        pixels1[415]= line_bdfm
    else:
        pass
    if "M Bowery" in combined_array:
        pixels1[416]= line_bdfm
    else:
        pass
    if "M Canal St" in combined_array:
        pixels1[417]= line_bdfm
    else:
        pass
    if "M Chambers St" in combined_array:
        pixels1[418]= line_bdfm
    else:
        pass
    if "M Fulton St" in combined_array:
        pixels1[419]= line_bdfm
    else:
        pass
    if "M Broad St" in combined_array:
        pixels1[420]= line_bdfm
    else:
        pass
    if "N 8 Av" in combined_array:
        pixels1[421]= line_nqrw
    else:
        pass
    if "N Fort Hamilton Pkwy" in combined_array:
        pixels1[422]= line_nqrw
    else:
        pass
    if "N New Utrecht Av" in combined_array:
        pixels1[423]= line_nqrw
    else:
        pass
    if "N 18 Av" in combined_array:
        pixels1[424]= line_nqrw
    else:
        pass
    if "N 20 Av" in combined_array:
        pixels1[425]= line_nqrw
    else:
        pass
    if "N Bay Pkwy" in combined_array:
        pixels1[426]= line_nqrw
    else:
        pass
    if "N Kings Hwy" in combined_array:
        pixels1[427]= line_nqrw
    else:
        pass
    if "N Avenue U" in combined_array:
        pixels1[428]= line_nqrw
    else:
        pass
    if "N 86 St" in combined_array:
        pixels1[429]= line_nqrw
    else:
        pass
    if "N S.B. Coney Island" in combined_array:
        pixels1[430]= line_nqrw
    else:
        pass
    if "Q Canal St" in combined_array:
        pixels1[431]= line_nqrw
    else:
        pass
    if "Q 72 St" in combined_array:
        pixels1[432]= line_nqrw
    else:
        pass
    if "Q 86 St" in combined_array:
        pixels1[433]= line_nqrw
    else:
        pass
    if "Q 96 St" in combined_array:
        pixels1[434]= line_nqrw
    else:
        pass
    if "R Astoria-Ditmars Blvd" in combined_array:
        pixels1[435]= line_nqrw
    else:
        pass
    if "R Astoria Blvd" in combined_array:
        pixels1[436]= line_nqrw
    else:
        pass
    if "R 30 Av" in combined_array:
        pixels1[437]= line_nqrw
    else:
        pass
    if "R Broadway" in combined_array:
        pixels1[438]= line_nqrw
    else:
        pass
    if "R 36 Av" in combined_array:
        pixels1[439]= line_nqrw
    else:
        pass
    if "R 39 Av-Dutch Kills" in combined_array:
        pixels1[440]= line_nqrw
    else:
        pass
    if "R Queensboro Plaza" in combined_array:
        pixels1[441]= line_nqrw
    else:
        pass
    if "R Lexington Av/59 St" in combined_array:
        pixels1[442]= line_nqrw
    else:
        pass
    if "R 5 Av/59 St" in combined_array:
        pixels1[443]= line_nqrw
    else:
        pass
    if "R 57 St-7 Av" in combined_array:
        pixels1[444]= line_nqrw
    else:
        pass
    if "R 49 St" in combined_array:
        pixels1[445]= line_nqrw
    else:
        pass
    if "R Times Sq-42 St" in combined_array:
        pixels1[446]= line_nqrw
    else:
        pass
    if "R 34 St-Herald Sq" in combined_array:
        pixels1[447]= line_nqrw
    else:
        pass
    if "R 28 St" in combined_array:
        pixels1[448]= line_nqrw
    else:
        pass
    if "R 23 St" in combined_array:
        pixels1[449]= line_nqrw
    else:
        pass
    if "R 14 St-Union Sq" in combined_array:
        pixels1[450]= line_nqrw
    else:
        pass
    if "R 8 St-NYU" in combined_array:
        pixels1[451]= line_nqrw
    else:
        pass
    if "R Prince St" in combined_array:
        pixels1[452]= line_nqrw
    else:
        pass
    if "R Canal St" in combined_array:
        pixels1[453]= line_nqrw
    else:
        pass
    if "R City Hall" in combined_array:
        pixels1[454]= line_nqrw
    else:
        pass
    if "R Cortlandt St" in combined_array:
        pixels1[455]= line_nqrw
    else:
        pass
    if "R Rector St" in combined_array:
        pixels1[456]= line_nqrw
    else:
        pass
    if "R Whitehall St-South Ferry" in combined_array:
        pixels1[2]= line_nqrw
    else:
        pass
    if "R Court St" in combined_array:
        pixels1[458]= line_nqrw
    else:
        pass
    if "R Jay St-MetroTech" in combined_array:
        pixels1[459]= line_nqrw
    else:
        pass
    if "R DeKalb Av" in combined_array:
        pixels1[460]= line_nqrw
    else:
        pass
    if "R Atlantic Av-Barclays Ctr" in combined_array:
        pixels1[461]= line_nqrw
    else:
        pass
    if "R Union St" in combined_array:
        pixels1[462]= line_nqrw
    else:
        pass
    if "R 4 Av-9 St" in combined_array:
        pixels1[463]= line_nqrw
    else:
        pass
    if "R Prospect Av" in combined_array:
        pixels1[464]= line_nqrw
    else:
        pass
    if "R 25 St" in combined_array:
        pixels1[465]= line_nqrw
    else:
        pass
    if "R 36 St" in combined_array:
        pixels1[466]= line_nqrw
    else:
        pass
    if "R 45 St" in combined_array:
        pixels1[467]= line_nqrw
    else:
        pass
    if "R 53 St" in combined_array:
        pixels1[468]= line_nqrw
    else:
        pass
    if "R 59 St" in combined_array:
        pixels1[469]= line_nqrw
    else:
        pass
    if "R Bay Ridge Av" in combined_array:
        pixels1[470]= line_nqrw
    else:
        pass
    if "R 77 St" in combined_array:
        pixels1[471]= line_nqrw
    else:
        pass
    if "R 86 St" in combined_array:
        pixels1[472]= line_nqrw
    else:
        pass
    if "R Bay Ridge-95 St" in combined_array:
        pixels1[473]= line_nqrw
    else:
        pass
    if "S Franklin Av" in combined_array:
        pixels1[474]= line_ls
    else:
        pass
    if "S Park Pl" in combined_array:
        pixels1[475]= line_ls
    else:
        pass
    if "S Botanic Garden" in combined_array:
        pixels1[476]= line_ls
    else:
        pass
    if "S Tottenville" in combined_array:
        pixels1[477]= line_ls
    else:
        pass
    if "S Arthur Kill" in combined_array:
        pixels1[478]= line_ls
    else:
        pass
    if "S Richmond Valley" in combined_array:
        pixels1[479]= line_ls
    else:
        pass
    if "S Pleasant Plains" in combined_array:
        pixels1[480]= line_ls
    else:
        pass
    if "S Prince's Bay" in combined_array:
        pixels1[481]= line_ls
    else:
        pass
    if "S Huguenot" in combined_array:
        pixels1[482]= line_ls
    else:
        pass
    if "S Annadale" in combined_array:
        pixels1[483]= line_ls
    else:
        pass
    if "S Eltingville" in combined_array:
        pixels1[484]= line_ls
    else:
        pass
    if "S Great Kills" in combined_array:
        pixels1[485]= line_ls
    else:
        pass
    if "S Bay Terrace" in combined_array:
        pixels1[486]= line_ls
    else:
        pass
    if "S Oakwood Heights" in combined_array:
        pixels1[487]= line_ls
    else:
        pass
    if "S New Dorp" in combined_array:
        pixels1[488]= line_ls
    else:
        pass
    if "S Grant City" in combined_array:
        pixels1[489]= line_ls
    else:
        pass
    if "S Jefferson Av" in combined_array:
        pixels1[490]= line_ls
    else:
        pass
    if "S Dongan Hills" in combined_array:
        pixels1[491]= line_ls
    else:
        pass
    if "S Old Town" in combined_array:
        pixels1[492]= line_ls
    else:
        pass
    if "S Grasmere" in combined_array:
        pixels1[493]= line_ls
    else:
        pass
    if "S Clifton" in combined_array:
        pixels1[494]= line_ls
    else:
        pass
    if "S Stapleton" in combined_array:
        pixels1[495]= line_ls
    else:
        pass
    if "S Tompkinsville" in combined_array:
        pixels1[496]= line_ls
    else:
        pass
    if "S St George" in combined_array:
        pixels1[497]= line_ls
    else:
        ()
    
    # temp while testing to not use extra power
    time.sleep(10)
    pixels1.fill((0, 0, 0))
    

else: 
    ()
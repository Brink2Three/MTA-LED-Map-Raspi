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

lines = ["1", "2", "3", "4", "5", "6", "7", "A", "C", "E", "B", "D", "F", "M", "N", "Q", "R", "W", "J", "Z", "L", "S"]
brokenstops = ["R70N", "R70S", "R60S", "R60N", "R65S", "R65N", "D23S", "D23N", "H17S", "H18S"]
lines_array = []
stops_array = []
active_stops = 0
# Unduplicated stops in stops.txt file... Probably not all of the mta stops. 
possible_stops = ["Van Cortlandt Park-242 St", "238 St", "231 St", "Marble Hill-225 St", "215 St", "207 St", "Dyckman St", "191 St", "181 St", "168 St-Washington Hts", "157 St", "145 St", "137 St-City College", "125 St", "116 St-Columbia University", "Cathedral Pkwy (110 St)", "103 St", "96 St", "86 St", "79 St", "72 St", "66 St-Lincoln Center", "59 St-Columbus Circle", "50 St", "Times Sq-42 St", "34 St-Penn Station", "28 St", "23 St", "18 St", "14 St", "Christopher St-Sheridan Sq", "Houston St", "Canal St", "Franklin St", "Chambers St", "WTC Cortlandt", "Rector St", "South Ferry Loop", "South Ferry", "Wakefield-241 St", "Nereid Av", "233 St", "225 St", "219 St", "Gun Hill Rd", "Burke Av", "Allerton Av", "Pelham Pkwy", "Bronx Park East", "E 180 St", "West Farms Sq-E Tremont Av", "174 St", "Freeman St", "Simpson St", "Intervale Av", "Prospect Av", "Jackson Av", "3 Av-149 St", "149 St-Grand Concourse", "135 St", "116 St", "Central Park North (110 St)", "Park Place", "Fulton St", "Wall St", "Clark St", "Borough Hall", "Hoyt St", "Nevins St", "Atlantic Av-Barclays Ctr", "Bergen St", "Grand Army Plaza", "Eastern Pkwy-Brooklyn Museum", "Franklin Av-Medgar Evers College", "President St-Medgar Evers College", "Sterling St", "Winthrop St", "Church Av", "Beverly Rd", "Newkirk Av-Little Haiti", "Flatbush Av-Brooklyn College", "Nostrand Av", "Kingston Av", "Crown Hts-Utica Av", "Sutter Av-Rutland Rd", "Saratoga Av", "Rockaway Av", "Junius St", "Pennsylvania Av", "Van Siclen Av", "New Lots Av", "Harlem-148 St", "Woodlawn", "Mosholu Pkwy", "Bedford Park Blvd-Lehman College", "Kingsbridge Rd", "Fordham Rd", "183 St", "Burnside Av", "176 St", "Mt Eden Av", "170 St", "167 St", "161 St-Yankee Stadium", "138 St-Grand Concourse", "Bowling Green", "Eastchester-Dyre Av", "Baychester Av", "Morris Park", "Pelham Bay Park", "Buhre Av", "Middletown Rd", "Westchester Sq-E Tremont Av", "Zerega Av", "Castle Hill Av", "Parkchester", "St Lawrence Av", "Morrison Av-Soundview", "Elder Av", "Whitlock Av", "Hunts Point Av", "Longwood Av", "E 149 St", "E 143 St-St Mary's St", "Cypress Av", "Brook Av", "3 Av-138 St", "110 St", "77 St", "68 St-Hunter College", "59 St", "51 St", "Grand Central-42 St", "33 St", "14 St-Union Sq", "Astor Pl", "Bleecker St", "Spring St", "Brooklyn Bridge-City Hall", "Flushing-Main St", "Mets-Willets Point", "111 St", "103 St-Corona Plaza", "Junction Blvd", "90 St-Elmhurst Av", "82 St-Jackson Hts", "74 St-Broadway", "69 St", "61 St-Woodside", "52 St", "46 St-Bliss St", "40 St-Lowery St", "33 St-Rawson St", "Queensboro Plaza", "Court Sq", "Hunters Point Av", "Vernon Blvd-Jackson Av", "5 Av", "34 St-Hudson Yards", "Inwood-207 St", "190 St", "175 St", "168 St", "163 St-Amsterdam Av", "155 St", "81 St-Museum of Natural History", "42 St-Port Authority Bus Terminal", "W 4 St-Wash Sq", "High St", "Jay St-MetroTech", "Hoyt-Schermerhorn Sts", "Lafayette Av", "Clinton-Washington Avs", "Franklin Av", "Kingston-Throop Avs", "Utica Av", "Ralph Av", "Broadway Junction", "Liberty Av", "Shepherd Av", "Euclid Av", "Grant Av", "80 St", "88 St", "Rockaway Blvd", "104 St", "Ozone Park-Lefferts Blvd", "21 St-Queensbridge", "Roosevelt Island", "Lexington Av/63 St", "57 St", "9 Av", "Fort Hamilton Pkwy", "55 St", "62 St", "71 St", "18 Av", "20 Av", "Bay Pkwy", "25 Av", "Bay 50 St", "Norwood-205 St", "Bedford Park Blvd", "182-183 Sts", "Tremont Av", "174-175 Sts", "7 Av", "47-50 Sts-Rockefeller Ctr", "42 St-Bryant Pk", "34 St-Herald Sq", "Broadway-Lafayette St", "Grand St", "Prospect Park", "Parkside Av", "Beverley Rd", "Cortelyou Rd", "Newkirk Plaza", "Avenue H", "Avenue J", "Avenue M", "Kings Hwy", "Avenue U", "Neck Rd", "Sheepshead Bay", "Brighton Beach", "Ocean Pkwy", "W 8 St-NY Aquarium", "Coney Island-Stillwell Av", "World Trade Center", "Jamaica-179 St", "169 St", "Parsons Blvd", "Sutphin Blvd", "Briarwood", "Kew Gardens-Union Tpke", "75 Av", "Court Sq-23 St", "Lexington Av/53 St", "5 Av/53 St", "2 Av", "Delancey St-Essex St", "East Broadway", "York St", "Carroll St", "Smith-9 Sts", "4 Av-9 St", "15 St-Prospect Park", "Ditmas Av", "Avenue I", "Avenue N", "Avenue P", "Avenue X", "Neptune Av", "Jamaica Center-Parsons/Archer", "Sutphin Blvd-Archer Av-JFK Airport", "Jamaica-Van Wyck", "Forest Hills-71 Av", "67 Av", "63 Dr-Rego Park", "Woodhaven Blvd", "Grand Av-Newtown", "Elmhurst Av", "Jackson Hts-Roosevelt Av", "65 St", "Northern Blvd", "46 St", "Steinway St", "36 St", "Queens Plaza", "21 St", "Greenpoint Av", "Nassau Av", "Metropolitan Av", "Broadway", "Flushing Av", "Myrtle-Willoughby Avs", "Bedford-Nostrand Avs", "Classon Av", "Aqueduct Racetrack", "Aqueduct-N Conduit Av", "Howard Beach-JFK Airport", "Broad Channel", "Beach 67 St", "Beach 60 St", "Beach 44 St", "Beach 36 St", "Beach 25 St", "Far Rockaway-Mott Av", "Beach 90 St", "Beach 98 St", "Beach 105 St", "Rockaway Park-Beach 116 St", "121 St", "85 St-Forest Pkwy", "75 St-Elderts Ln", "Cypress Hills", "Crescent St", "Norwood Av", "Cleveland St", "Alabama Av", "Chauncey St", "Halsey St", "Gates Av", "Kosciuszko St", "8 Av", "6 Av", "3 Av", "1 Av", "Bedford Av", "Lorimer St", "Graham Av", "Montrose Av", "Morgan Av", "Jefferson St", "DeKalb Av", "Myrtle-Wyckoff Avs", "Wilson Av", "Bushwick Av-Aberdeen St", "Atlantic Av", "Sutter Av", "Livonia Av", "East 105 St", "Canarsie-Rockaway Pkwy", "Middle Village-Metropolitan Av", "Fresh Pond Rd", "Forest Av", "Seneca Av", "Knickerbocker Av", "Central Av", "Myrtle Av", "Hewes St", "Marcy Av", "Bowery", "Broad St", "New Utrecht Av", "S.B. Coney Island", "Astoria-Ditmars Blvd", "Astoria Blvd", "30 Av", "36 Av", "39 Av-Dutch Kills", "Lexington Av/59 St", "5 Av/59 St", "57 St-7 Av", "49 St", "8 St-NYU", "Prince St", "City Hall", "Cortlandt St", "Whitehall St-South Ferry", "Court St", "Union St", "25 St", "45 St", "53 St", "Bay Ridge Av", "Bay Ridge-95 St", "Park Pl", "Botanic Garden", "Tottenville", "Arthur Kill", "Richmond Valley", "Pleasant Plains", "Prince's Bay", "Huguenot", "Annadale", "Eltingville", "Great Kills", "Bay Terrace", "Oakwood Heights", "New Dorp", "Grant City", "Jefferson Av", "Dongan Hills", "Old Town", "Grasmere", "Clifton", "Stapleton", "Tompkinsville", "St George"]
# Assign LED number to position of stops. Simplest way could be 0 is northernmost or southernmost stop.

def process_lines(line_num):
    processed_lines = line_num
    return processed_lines


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
    print("Current stop: " + stops_array[10])
    print("Current Line: " + lines_array[10])
    for possible_stops in stops_array:
        if possible_stops in stops_array:
            active_stops += 1
    print("Number of stopped trains: ")
    print(active_stops)
else : 
    ()
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

#pixels1 = neopixel.NeoPixel(board.D18, 497, brightness=.15)
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
possible_stops = ["1 Van Cortlandt Park-242 St" ,"1 238 St" ,"1 231 St" ,"1 Marble Hill-225 St" ,"1 215 St" ,"1 207 St" ,"1 Dyckman St" ,"1 191 St" ,"1 181 St" ,"1 168 St-Washington Hts" ,"1 157 St" ,"1 145 St" ,"1 137 St-City College" ,"1 125 St" ,"1 116 St-Columbia University" ,"1 Cathedral Pkwy (110 St)" ,"1 103 St" ,"1 96 St" ,"1 86 St" ,"1 79 St" ,"1 72 St" ,"1 66 St-Lincoln Center" ,"1 59 St-Columbus Circle" ,"1 50 St" ,"1 Times Sq-42 St" ,"1 34 St-Penn Station" ,"1 28 St" ,"1 23 St" ,"1 18 St" ,"1 14 St" ,"1 Christopher St-Sheridan Sq" ,"1 Houston St" ,"1 Canal St" ,"1 Franklin St" ,"1 Chambers St" ,"1 WTC Cortlandt" ,"1 Rector St" ,"1 South Ferry Loop" ,"1 South Ferry" ,"2 Wakefield-241 St" ,"2 Nereid Av" ,"2 233 St" ,"2 225 St" ,"2 219 St" ,"2 Gun Hill Rd" ,"2 Burke Av" ,"2 Allerton Av" ,"2 Pelham Pkwy" ,"2 Bronx Park East" ,"2 E 180 St" ,"2 West Farms Sq-E Tremont Av" ,"2 174 St" ,"2 Freeman St" ,"2 Simpson St" ,"2 Intervale Av" ,"2 Prospect Av" ,"2 Jackson Av" ,"2 3 Av-149 St" ,"2 149 St-Grand Concourse" ,"2 135 St" ,"2 125 St" ,"2 116 St" ,"2 Central Park North (110 St)" ,"2 Park Place" ,"2 Fulton St" ,"2 Wall St" ,"2 Clark St" ,"2 Borough Hall" ,"2 Hoyt St" ,"2 Nevins St" ,"2 Atlantic Av-Barclays Ctr" ,"2 Bergen St" ,"2 Grand Army Plaza" ,"2 Eastern Pkwy-Brooklyn Museum" ,"2 Franklin Av-Medgar Evers College" ,"2 President St-Medgar Evers College" ,"2 Sterling St" ,"2 Winthrop St" ,"2 Church Av" ,"2 Beverly Rd" ,"2 Newkirk Av-Little Haiti" ,"2 Flatbush Av-Brooklyn College" ,"2 Nostrand Av" ,"2 Kingston Av" ,"2 Crown Hts-Utica Av" ,"2 Sutter Av-Rutland Rd" ,"2 Saratoga Av" ,"2 Rockaway Av" ,"2 Junius St" ,"2 Pennsylvania Av" ,"2 Van Siclen Av" ,"2 New Lots Av" ,"3 Harlem-148 St" ,"3 145 St" ,"4 Woodlawn" ,"4 Mosholu Pkwy" ,"4 Bedford Park Blvd-Lehman College" ,"4 Kingsbridge Rd" ,"4 Fordham Rd" ,"4 183 St" ,"4 Burnside Av" ,"4 176 St" ,"4 Mt Eden Av" ,"4 170 St" ,"4 167 St" ,"4 161 St-Yankee Stadium" ,"4 149 St-Grand Concourse" ,"4 138 St-Grand Concourse" ,"4 Fulton St" ,"4 Wall St" ,"4 Bowling Green" ,"4 Borough Hall" ,"5 Eastchester-Dyre Av" ,"5 Baychester Av" ,"5 Gun Hill Rd" ,"5 Pelham Pkwy" ,"5 Morris Park" ,"6 Pelham Bay Park" ,"6 Buhre Av" ,"6 Middletown Rd" ,"6 Westchester Sq-E Tremont Av" ,"6 Zerega Av" ,"6 Castle Hill Av" ,"6 Parkchester" ,"6 St Lawrence Av" ,"6 Morrison Av-Soundview" ,"6 Elder Av" ,"6 Whitlock Av" ,"6 Hunts Point Av" ,"6 Longwood Av" ,"6 E 149 St" ,"6 E 143 St-St Mary's St" ,"6 Cypress Av" ,"6 Brook Av" ,"6 3 Av-138 St" ,"6 125 St" ,"6 116 St" ,"6 110 St" ,"6 103 St" ,"6 96 St" ,"6 86 St" ,"6 77 St" ,"6 68 St-Hunter College" ,"6 59 St" ,"6 51 St" ,"6 Grand Central-42 St" ,"6 33 St" ,"6 28 St" ,"6 23 St" ,"6 14 St-Union Sq" ,"6 Astor Pl" ,"6 Bleecker St" ,"6 Spring St" ,"6 Canal St" ,"6 Brooklyn Bridge-City Hall" ,"7 Flushing-Main St" ,"7 Mets-Willets Point" ,"7 111 St" ,"7 103 St-Corona Plaza" ,"7 Junction Blvd" ,"7 90 St-Elmhurst Av" ,"7 82 St-Jackson Hts" ,"7 74 St-Broadway" ,"7 69 St" ,"7 61 St-Woodside" ,"7 52 St" ,"7 46 St-Bliss St" ,"7 40 St-Lowery St" ,"7 33 St-Rawson St" ,"7 Queensboro Plaza" ,"7 Court Sq" ,"7 Hunters Point Av" ,"7 Vernon Blvd-Jackson Av" ,"7 Grand Central-42 St" ,"7 5 Av" ,"7 Times Sq-42 St" ,"7 34 St-Hudson Yards" ,"S Grand Central-42 St" ,"S Times Sq-42 St" ,"A Inwood-207 St" ,"A Dyckman St" ,"A 190 St" ,"A 181 St" ,"A 175 St" ,"A 168 St" ,"A 163 St-Amsterdam Av" ,"A 155 St" ,"A 145 St" ,"A 135 St" ,"A 125 St" ,"A 116 St" ,"A Cathedral Pkwy (110 St)" ,"A 103 St" ,"A 96 St" ,"A 86 St" ,"A 81 St-Museum of Natural History" ,"A 72 St" ,"A 59 St-Columbus Circle" ,"A 50 St" ,"A 42 St-Port Authority Bus Terminal" ,"A 34 St-Penn Station" ,"A 23 St" ,"A 14 St" ,"A W 4 St-Wash Sq" ,"A Spring St" ,"A Canal St" ,"A Chambers St" ,"A Fulton St" ,"A High St" ,"A Jay St-MetroTech" ,"A Hoyt-Schermerhorn Sts" ,"A Lafayette Av" ,"A Clinton-Washington Avs" ,"A Franklin Av" ,"A Nostrand Av" ,"A Kingston-Throop Avs" ,"A Utica Av" ,"A Ralph Av" ,"A Rockaway Av" ,"A Broadway Junction" ,"A Liberty Av" ,"A Van Siclen Av" ,"A Shepherd Av" ,"A Euclid Av" ,"A Grant Av" ,"A 80 St" ,"A 88 St" ,"A Rockaway Blvd" ,"A 104 St" ,"A 111 St" ,"A Ozone Park-Lefferts Blvd" ,"B 21 St-Queensbridge" ,"B Roosevelt Island" ,"B Lexington Av/63 St" ,"B 57 St" ,"B 9 Av" ,"B Fort Hamilton Pkwy" ,"B 50 St" ,"B 55 St" ,"B 62 St" ,"B 71 St" ,"B 79 St" ,"B 18 Av" ,"B 20 Av" ,"B Bay Pkwy" ,"B 25 Av" ,"B Bay 50 St" ,"D Norwood-205 St" ,"D Bedford Park Blvd" ,"D Kingsbridge Rd" ,"D Fordham Rd" ,"D 182-183 Sts" ,"D Tremont Av" ,"D 174-175 Sts" ,"D 170 St" ,"D 167 St" ,"D 161 St-Yankee Stadium" ,"D 155 St" ,"D 145 St" ,"D 7 Av" ,"D 47-50 Sts-Rockefeller Ctr" ,"D 42 St-Bryant Pk" ,"D 34 St-Herald Sq" ,"D 23 St" ,"D 14 St" ,"D W 4 St-Wash Sq" ,"D Broadway-Lafayette St" ,"D Grand St" ,"D Atlantic Av-Barclays Ctr" ,"D Prospect Park" ,"D Parkside Av" ,"D Church Av" ,"D Beverley Rd" ,"D Cortelyou Rd" ,"D Newkirk Plaza" ,"D Avenue H" ,"D Avenue J" ,"D Avenue M" ,"D Kings Hwy" ,"D Avenue U" ,"D Neck Rd" ,"D Sheepshead Bay" ,"D Brighton Beach" ,"D Ocean Pkwy" ,"D W 8 St-NY Aquarium" ,"D Coney Island-Stillwell Av" ,"E World Trade Center" ,"F Jamaica-179 St" ,"F 169 St" ,"F Parsons Blvd" ,"F Sutphin Blvd" ,"F Briarwood" ,"F Kew Gardens-Union Tpke" ,"F 75 Av" ,"F Court Sq-23 St" ,"F Lexington Av/53 St" ,"F 5 Av/53 St" ,"F 2 Av" ,"F Delancey St-Essex St" ,"F East Broadway" ,"F York St" ,"F Bergen St" ,"F Carroll St" ,"F Smith-9 Sts" ,"F 4 Av-9 St" ,"F 7 Av" ,"F 15 St-Prospect Park" ,"F Fort Hamilton Pkwy" ,"F Church Av" ,"F Ditmas Av" ,"F 18 Av" ,"F Avenue I" ,"F Bay Pkwy" ,"F Avenue N" ,"F Avenue P" ,"F Kings Hwy" ,"F Avenue U" ,"F Avenue X" ,"F Neptune Av" ,"G Jamaica Center-Parsons/Archer" ,"G Sutphin Blvd-Archer Av-JFK Airport" ,"G Jamaica-Van Wyck" ,"G Forest Hills-71 Av" ,"G 67 Av" ,"G 63 Dr-Rego Park" ,"G Woodhaven Blvd" ,"G Grand Av-Newtown" ,"G Elmhurst Av" ,"G Jackson Hts-Roosevelt Av" ,"G 65 St" ,"G Northern Blvd" ,"G 46 St" ,"G Steinway St" ,"G 36 St" ,"G Queens Plaza" ,"G Court Sq" ,"G 21 St" ,"G Greenpoint Av" ,"G Nassau Av" ,"G Metropolitan Av" ,"G Broadway" ,"G Flushing Av" ,"G Myrtle-Willoughby Avs" ,"G Bedford-Nostrand Avs" ,"G Classon Av" ,"G Clinton-Washington Avs" ,"G Fulton St" ,"H Aqueduct Racetrack" ,"H Aqueduct-N Conduit Av" ,"H Howard Beach-JFK Airport" ,"H Broad Channel" ,"H Beach 67 St" ,"H Beach 60 St" ,"H Beach 44 St" ,"H Beach 36 St" ,"H Beach 25 St" ,"H Far Rockaway-Mott Av" ,"H Beach 90 St" ,"H Beach 98 St" ,"H Beach 105 St" ,"H Rockaway Park-Beach 116 St" ,"J 121 St" ,"J 111 St" ,"J 104 St" ,"J Woodhaven Blvd" ,"J 85 St-Forest Pkwy" ,"J 75 St-Elderts Ln" ,"J Cypress Hills" ,"J Crescent St" ,"J Norwood Av" ,"J Cleveland St" ,"J Van Siclen Av" ,"J Alabama Av" ,"J Broadway Junction" ,"J Chauncey St" ,"J Halsey St" ,"J Gates Av" ,"J Kosciuszko St" ,"L 8 Av" ,"L 6 Av" ,"L 14 St-Union Sq" ,"L 3 Av" ,"L 1 Av" ,"L Bedford Av" ,"L Lorimer St" ,"L Graham Av" ,"L Grand St" ,"L Montrose Av" ,"L Morgan Av" ,"L Jefferson St" ,"L DeKalb Av" ,"L Myrtle-Wyckoff Avs" ,"L Halsey St" ,"L Wilson Av" ,"L Bushwick Av-Aberdeen St" ,"L Broadway Junction" ,"L Atlantic Av" ,"L Sutter Av" ,"L Livonia Av" ,"L New Lots Av" ,"L East 105 St" ,"L Canarsie-Rockaway Pkwy" ,"M Middle Village-Metropolitan Av" ,"M Fresh Pond Rd" ,"M Forest Av" ,"M Seneca Av" ,"M Myrtle-Wyckoff Avs" ,"M Knickerbocker Av" ,"M Central Av" ,"M Myrtle Av" ,"M Flushing Av" ,"M Lorimer St" ,"M Hewes St" ,"M Marcy Av" ,"M Delancey St-Essex St" ,"M Bowery" ,"M Canal St" ,"M Chambers St" ,"M Fulton St" ,"M Broad St" ,"N 8 Av" ,"N Fort Hamilton Pkwy" ,"N New Utrecht Av" ,"N 18 Av" ,"N 20 Av" ,"N Bay Pkwy" ,"N Kings Hwy" ,"N Avenue U" ,"N 86 St" ,"N S.B. Coney Island" ,"Q Canal St" ,"Q 72 St" ,"Q 86 St" ,"Q 96 St" ,"R Astoria-Ditmars Blvd" ,"R Astoria Blvd" ,"R 30 Av" ,"R Broadway" ,"R 36 Av" ,"R 39 Av-Dutch Kills" ,"R Queensboro Plaza" ,"R Lexington Av/59 St" ,"R 5 Av/59 St" ,"R 57 St-7 Av" ,"R 49 St" ,"R Times Sq-42 St" ,"R 34 St-Herald Sq" ,"R 28 St" ,"R 23 St" ,"R 14 St-Union Sq" ,"R 8 St-NYU" ,"R Prince St" ,"R Canal St" ,"R City Hall" ,"R Cortlandt St" ,"R Rector St" ,"R Whitehall St-South Ferry" ,"R Court St" ,"R Jay St-MetroTech" ,"R DeKalb Av" ,"R Atlantic Av-Barclays Ctr" ,"R Union St" ,"R 4 Av-9 St" ,"R Prospect Av" ,"R 25 St" ,"R 36 St" ,"R 45 St" ,"R 53 St" ,"R 59 St" ,"R Bay Ridge Av" ,"R 77 St" ,"R 86 St" ,"R Bay Ridge-95 St" ,"S Franklin Av" ,"S Park Pl" ,"S Botanic Garden" ,"S Tottenville" ,"S Arthur Kill" ,"S Richmond Valley" ,"S Pleasant Plains" ,"S Prince's Bay" ,"S Huguenot" ,"S Annadale" ,"S Eltingville" ,"S Great Kills" ,"S Bay Terrace" ,"S Oakwood Heights" ,"S New Dorp" ,"S Grant City" ,"S Jefferson Av" ,"S Dongan Hills" ,"S Old Town" ,"S Grasmere" ,"S Clifton" ,"S Stapleton" ,"S Tompkinsville" ,"S St George"]
lines = ["1", "2", "3", "4", "5", "6", "7", "A", "C", "E", "B", "D", "F", "M", "N", "Q", "R", "W", "J", "Z", "L", "S"]
brokenstops = ["R70N", "R70S", "R60S", "R60N", "R65S", "R65N", "D23S", "D23N", "H17S", "H18S", "A29S"]
lines_array = []
stops_array = []
combined_array = []

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
    for i in range(len(lines_array)): 
        combined_array.append(str(lines_array[i] + " " + stops_array[i]))
    print(combined_array)
    #if string in combined array matches a possible stop, light the LED with the same index as the index in possible stops

else: 
    ()
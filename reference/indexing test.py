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

#MTA SETTINGS
#possible_stops = ["1 Van Cortlandt Park-242 St" ,"1 238 St" ,"1 231 St" ,"1 Marble Hill-225 St" ,"1 215 St" ,"1 207 St" ,"1 Dyckman St" ,"1 191 St" ,"1 181 St" ,"1 168 St-Washington Hts" ,"1 157 St" ,"1 145 St" ,"1 137 St-City College" ,"1 125 St" ,"1 116 St-Columbia University" ,"1 Cathedral Pkwy (110 St)" ,"1 103 St" ,"1 96 St" ,"1 86 St" ,"1 79 St" ,"1 72 St" ,"1 66 St-Lincoln Center" ,"1 59 St-Columbus Circle" ,"1 50 St" ,"1 Times Sq-42 St" ,"1 34 St-Penn Station" ,"1 28 St" ,"1 23 St" ,"1 18 St" ,"1 14 St" ,"1 Christopher St-Sheridan Sq" ,"1 Houston St" ,"1 Canal St" ,"1 Franklin St" ,"1 Chambers St" ,"1 WTC Cortlandt" ,"1 Rector St" ,"1 South Ferry Loop" ,"1 South Ferry" ,"2 Wakefield-241 St" ,"2 Nereid Av" ,"2 233 St" ,"2 225 St" ,"2 219 St" ,"2 Gun Hill Rd" ,"2 Burke Av" ,"2 Allerton Av" ,"2 Pelham Pkwy" ,"2 Bronx Park East" ,"2 E 180 St" ,"2 West Farms Sq-E Tremont Av" ,"2 174 St" ,"2 Freeman St" ,"2 Simpson St" ,"2 Intervale Av" ,"2 Prospect Av" ,"2 Jackson Av" ,"2 3 Av-149 St" ,"2 149 St-Grand Concourse" ,"2 135 St" ,"2 125 St" ,"2 116 St" ,"2 Central Park North (110 St)" ,"2 Park Place" ,"2 Fulton St" ,"2 Wall St" ,"2 Clark St" ,"2 Borough Hall" ,"2 Hoyt St" ,"2 Nevins St" ,"2 Atlantic Av-Barclays Ctr" ,"2 Bergen St" ,"2 Grand Army Plaza" ,"2 Eastern Pkwy-Brooklyn Museum" ,"2 Franklin Av-Medgar Evers College" ,"2 President St-Medgar Evers College" ,"2 Sterling St" ,"2 Winthrop St" ,"2 Church Av" ,"2 Beverly Rd" ,"2 Newkirk Av-Little Haiti" ,"2 Flatbush Av-Brooklyn College" ,"2 Nostrand Av" ,"2 Kingston Av" ,"2 Crown Hts-Utica Av" ,"2 Sutter Av-Rutland Rd" ,"2 Saratoga Av" ,"2 Rockaway Av" ,"2 Junius St" ,"2 Pennsylvania Av" ,"2 Van Siclen Av" ,"2 New Lots Av" ,"3 Harlem-148 St" ,"3 145 St" ,"4 Woodlawn" ,"4 Mosholu Pkwy" ,"4 Bedford Park Blvd-Lehman College" ,"4 Kingsbridge Rd" ,"4 Fordham Rd" ,"4 183 St" ,"4 Burnside Av" ,"4 176 St" ,"4 Mt Eden Av" ,"4 170 St" ,"4 167 St" ,"4 161 St-Yankee Stadium" ,"4 149 St-Grand Concourse" ,"4 138 St-Grand Concourse" ,"4 Fulton St" ,"4 Wall St" ,"4 Bowling Green" ,"4 Borough Hall" ,"5 Eastchester-Dyre Av" ,"5 Baychester Av" ,"5 Gun Hill Rd" ,"5 Pelham Pkwy" ,"5 Morris Park" ,"6 Pelham Bay Park" ,"6 Buhre Av" ,"6 Middletown Rd" ,"6 Westchester Sq-E Tremont Av" ,"6 Zerega Av" ,"6 Castle Hill Av" ,"6 Parkchester" ,"6 St Lawrence Av" ,"6 Morrison Av-Soundview" ,"6 Elder Av" ,"6 Whitlock Av" ,"6 Hunts Point Av" ,"6 Longwood Av" ,"6 E 149 St" ,"6 E 143 St-St Mary's St" ,"6 Cypress Av" ,"6 Brook Av" ,"6 3 Av-138 St" ,"6 125 St" ,"6 116 St" ,"6 110 St" ,"6 103 St" ,"6 96 St" ,"6 86 St" ,"6 77 St" ,"6 68 St-Hunter College" ,"6 59 St" ,"6 51 St" ,"6 Grand Central-42 St" ,"6 33 St" ,"6 28 St" ,"6 23 St" ,"6 14 St-Union Sq" ,"6 Astor Pl" ,"6 Bleecker St" ,"6 Spring St" ,"6 Canal St" ,"6 Brooklyn Bridge-City Hall" ,"7 Flushing-Main St" ,"7 Mets-Willets Point" ,"7 111 St" ,"7 103 St-Corona Plaza" ,"7 Junction Blvd" ,"7 90 St-Elmhurst Av" ,"7 82 St-Jackson Hts" ,"7 74 St-Broadway" ,"7 69 St" ,"7 61 St-Woodside" ,"7 52 St" ,"7 46 St-Bliss St" ,"7 40 St-Lowery St" ,"7 33 St-Rawson St" ,"7 Queensboro Plaza" ,"7 Court Sq" ,"7 Hunters Point Av" ,"7 Vernon Blvd-Jackson Av" ,"7 Grand Central-42 St" ,"7 5 Av" ,"7 Times Sq-42 St" ,"7 34 St-Hudson Yards" ,"S Grand Central-42 St" ,"S Times Sq-42 St" ,"A Inwood-207 St" ,"A Dyckman St" ,"A 190 St" ,"A 181 St" ,"A 175 St" ,"A 168 St" ,"A 163 St-Amsterdam Av" ,"A 155 St" ,"A 145 St" ,"A 135 St" ,"A 125 St" ,"A 116 St" ,"A Cathedral Pkwy (110 St)" ,"A 103 St" ,"A 96 St" ,"A 86 St" ,"A 81 St-Museum of Natural History" ,"A 72 St" ,"A 59 St-Columbus Circle" ,"A 50 St" ,"A 42 St-Port Authority Bus Terminal" ,"A 34 St-Penn Station" ,"A 23 St" ,"A 14 St" ,"A W 4 St-Wash Sq" ,"A Spring St" ,"A Canal St" ,"A Chambers St" ,"A Fulton St" ,"A High St" ,"A Jay St-MetroTech" ,"A Hoyt-Schermerhorn Sts" ,"A Lafayette Av" ,"A Clinton-Washington Avs" ,"A Franklin Av" ,"A Nostrand Av" ,"A Kingston-Throop Avs" ,"A Utica Av" ,"A Ralph Av" ,"A Rockaway Av" ,"A Broadway Junction" ,"A Liberty Av" ,"A Van Siclen Av" ,"A Shepherd Av" ,"A Euclid Av" ,"A Grant Av" ,"A 80 St" ,"A 88 St" ,"A Rockaway Blvd" ,"A 104 St" ,"A 111 St" ,"A Ozone Park-Lefferts Blvd" ,"B 21 St-Queensbridge" ,"B Roosevelt Island" ,"B Lexington Av/63 St" ,"B 57 St" ,"B 9 Av" ,"B Fort Hamilton Pkwy" ,"B 50 St" ,"B 55 St" ,"B 62 St" ,"B 71 St" ,"B 79 St" ,"B 18 Av" ,"B 20 Av" ,"B Bay Pkwy" ,"B 25 Av" ,"B Bay 50 St" ,"D Norwood-205 St" ,"D Bedford Park Blvd" ,"D Kingsbridge Rd" ,"D Fordham Rd" ,"D 182-183 Sts" ,"D Tremont Av" ,"D 174-175 Sts" ,"D 170 St" ,"D 167 St" ,"D 161 St-Yankee Stadium" ,"D 155 St" ,"D 145 St" ,"D 7 Av" ,"D 47-50 Sts-Rockefeller Ctr" ,"D 42 St-Bryant Pk" ,"D 34 St-Herald Sq" ,"D 23 St" ,"D 14 St" ,"D W 4 St-Wash Sq" ,"D Broadway-Lafayette St" ,"D Grand St" ,"D Atlantic Av-Barclays Ctr" ,"D Prospect Park" ,"D Parkside Av" ,"D Church Av" ,"D Beverley Rd" ,"D Cortelyou Rd" ,"D Newkirk Plaza" ,"D Avenue H" ,"D Avenue J" ,"D Avenue M" ,"D Kings Hwy" ,"D Avenue U" ,"D Neck Rd" ,"D Sheepshead Bay" ,"D Brighton Beach" ,"D Ocean Pkwy" ,"D W 8 St-NY Aquarium" ,"D Coney Island-Stillwell Av" ,"E World Trade Center" ,"F Jamaica-179 St" ,"F 169 St" ,"F Parsons Blvd" ,"F Sutphin Blvd" ,"F Briarwood" ,"F Kew Gardens-Union Tpke" ,"F 75 Av" ,"F Court Sq-23 St" ,"F Lexington Av/53 St" ,"F 5 Av/53 St" ,"F 2 Av" ,"F Delancey St-Essex St" ,"F East Broadway" ,"F York St" ,"F Bergen St" ,"F Carroll St" ,"F Smith-9 Sts" ,"F 4 Av-9 St" ,"F 7 Av" ,"F 15 St-Prospect Park" ,"F Fort Hamilton Pkwy" ,"F Church Av" ,"F Ditmas Av" ,"F 18 Av" ,"F Avenue I" ,"F Bay Pkwy" ,"F Avenue N" ,"F Avenue P" ,"F Kings Hwy" ,"F Avenue U" ,"F Avenue X" ,"F Neptune Av" ,"G Jamaica Center-Parsons/Archer" ,"G Sutphin Blvd-Archer Av-JFK Airport" ,"G Jamaica-Van Wyck" ,"G Forest Hills-71 Av" ,"G 67 Av" ,"G 63 Dr-Rego Park" ,"G Woodhaven Blvd" ,"G Grand Av-Newtown" ,"G Elmhurst Av" ,"G Jackson Hts-Roosevelt Av" ,"G 65 St" ,"G Northern Blvd" ,"G 46 St" ,"G Steinway St" ,"G 36 St" ,"G Queens Plaza" ,"G Court Sq" ,"G 21 St" ,"G Greenpoint Av" ,"G Nassau Av" ,"G Metropolitan Av" ,"G Broadway" ,"G Flushing Av" ,"G Myrtle-Willoughby Avs" ,"G Bedford-Nostrand Avs" ,"G Classon Av" ,"G Clinton-Washington Avs" ,"G Fulton St" ,"H Aqueduct Racetrack" ,"H Aqueduct-N Conduit Av" ,"H Howard Beach-JFK Airport" ,"H Broad Channel" ,"H Beach 67 St" ,"H Beach 60 St" ,"H Beach 44 St" ,"H Beach 36 St" ,"H Beach 25 St" ,"H Far Rockaway-Mott Av" ,"H Beach 90 St" ,"H Beach 98 St" ,"H Beach 105 St" ,"H Rockaway Park-Beach 116 St" ,"J 121 St" ,"J 111 St" ,"J 104 St" ,"J Woodhaven Blvd" ,"J 85 St-Forest Pkwy" ,"J 75 St-Elderts Ln" ,"J Cypress Hills" ,"J Crescent St" ,"J Norwood Av" ,"J Cleveland St" ,"J Van Siclen Av" ,"J Alabama Av" ,"J Broadway Junction" ,"J Chauncey St" ,"J Halsey St" ,"J Gates Av" ,"J Kosciuszko St" ,"L 8 Av" ,"L 6 Av" ,"L 14 St-Union Sq" ,"L 3 Av" ,"L 1 Av" ,"L Bedford Av" ,"L Lorimer St" ,"L Graham Av" ,"L Grand St" ,"L Montrose Av" ,"L Morgan Av" ,"L Jefferson St" ,"L DeKalb Av" ,"L Myrtle-Wyckoff Avs" ,"L Halsey St" ,"L Wilson Av" ,"L Bushwick Av-Aberdeen St" ,"L Broadway Junction" ,"L Atlantic Av" ,"L Sutter Av" ,"L Livonia Av" ,"L New Lots Av" ,"L East 105 St" ,"L Canarsie-Rockaway Pkwy" ,"M Middle Village-Metropolitan Av" ,"M Fresh Pond Rd" ,"M Forest Av" ,"M Seneca Av" ,"M Myrtle-Wyckoff Avs" ,"M Knickerbocker Av" ,"M Central Av" ,"M Myrtle Av" ,"M Flushing Av" ,"M Lorimer St" ,"M Hewes St" ,"M Marcy Av" ,"M Delancey St-Essex St" ,"M Bowery" ,"M Canal St" ,"M Chambers St" ,"M Fulton St" ,"M Broad St" ,"N 8 Av" ,"N Fort Hamilton Pkwy" ,"N New Utrecht Av" ,"N 18 Av" ,"N 20 Av" ,"N Bay Pkwy" ,"N Kings Hwy" ,"N Avenue U" ,"N 86 St" ,"N S.B. Coney Island" ,"Q Canal St" ,"Q 72 St" ,"Q 86 St" ,"Q 96 St" ,"R Astoria-Ditmars Blvd" ,"R Astoria Blvd" ,"R 30 Av" ,"R Broadway" ,"R 36 Av" ,"R 39 Av-Dutch Kills" ,"R Queensboro Plaza" ,"R Lexington Av/59 St" ,"R 5 Av/59 St" ,"R 57 St-7 Av" ,"R 49 St" ,"R Times Sq-42 St" ,"R 34 St-Herald Sq" ,"R 28 St" ,"R 23 St" ,"R 14 St-Union Sq" ,"R 8 St-NYU" ,"R Prince St" ,"R Canal St" ,"R City Hall" ,"R Cortlandt St" ,"R Rector St" ,"R Whitehall St-South Ferry" ,"R Court St" ,"R Jay St-MetroTech" ,"R DeKalb Av" ,"R Atlantic Av-Barclays Ctr" ,"R Union St" ,"R 4 Av-9 St" ,"R Prospect Av" ,"R 25 St" ,"R 36 St" ,"R 45 St" ,"R 53 St" ,"R 59 St" ,"R Bay Ridge Av" ,"R 77 St" ,"R 86 St" ,"R Bay Ridge-95 St" ,"S Franklin Av" ,"S Park Pl" ,"S Botanic Garden" ,"S Tottenville" ,"S Arthur Kill" ,"S Richmond Valley" ,"S Pleasant Plains" ,"S Prince's Bay" ,"S Huguenot" ,"S Annadale" ,"S Eltingville" ,"S Great Kills" ,"S Bay Terrace" ,"S Oakwood Heights" ,"S New Dorp" ,"S Grant City" ,"S Jefferson Av" ,"S Dongan Hills" ,"S Old Town" ,"S Grasmere" ,"S Clifton" ,"S Stapleton" ,"S Tompkinsville" ,"S St George"]
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
    #if string in combined array matches a possible stop, light up the LED for that location
    if "1 Van Cortlandt Park-242 St" in combined_array:
        pixels1[1]= line_123
    elif "1 238 St" in combined_array:
        pixels1[2]= line_123
    elif "1 231 St" in combined_array:
        pixels1[3]= line_123
    elif "1 Marble Hill-225 St" in combined_array:
        pixels1[4]= line_123
    elif "1 215 St" in combined_array:
        pixels1[5]= line_123
    elif "1 207 St" in combined_array:
        pixels1[6]= line_123
    elif "1 Dyckman St" in combined_array:
        pixels1[7]= line_123
    elif "1 191 St" in combined_array:
        pixels1[8]= line_123
    elif "1 181 St" in combined_array:
        pixels1[9]= line_123
    elif "1 168 St-Washington Hts" in combined_array:
        pixels1[10]= line_123
    elif "1 157 St" in combined_array:
        pixels1[11]= line_123
    elif "1 145 St" in combined_array:
        pixels1[12]= line_123
    elif "1 137 St-City College" in combined_array:
        pixels1[13]= line_123
    elif "1 125 St" in combined_array:
        pixels1[14]= line_123
    elif "1 116 St-Columbia University" in combined_array:
        pixels1[15]= line_123
    elif "1 Cathedral Pkwy (110 St)" in combined_array:
        pixels1[16]= line_123
    elif "1 103 St" in combined_array:
        pixels1[17]= line_123
    elif "1 96 St" in combined_array:
        pixels1[18]= line_123
    elif "1 86 St" in combined_array:
        pixels1[19]= line_123
    elif "1 79 St" in combined_array:
        pixels1[20]= line_123
    elif "1 72 St" in combined_array:
        pixels1[21]= line_123
    elif "1 66 St-Lincoln Center" in combined_array:
        pixels1[22]= line_123
    elif "1 59 St-Columbus Circle" in combined_array:
        pixels1[23]= line_123
    elif "1 50 St" in combined_array:
        pixels1[24]= line_123
    elif "1 Times Sq-42 St" in combined_array:
        pixels1[25]= line_123
    elif "1 34 St-Penn Station" in combined_array:
        pixels1[26]= line_123
    elif "1 28 St" in combined_array:
        pixels1[27]= line_123
    elif "1 23 St" in combined_array:
        pixels1[28]= line_123
    elif "1 18 St" in combined_array:
        pixels1[29]= line_123
    elif "1 14 St" in combined_array:
        pixels1[30]= line_123
    elif "1 Christopher St-Sheridan Sq" in combined_array:
        pixels1[31]= line_123
    elif "1 Houston St" in combined_array:
        pixels1[32]= line_123
    elif "1 Canal St" in combined_array:
        pixels1[33]= line_123
    elif "1 Franklin St" in combined_array:
        pixels1[34]= line_123
    elif "1 Chambers St" in combined_array:
        pixels1[35]= line_123
    elif "1 WTC Cortlandt" in combined_array:
        pixels1[36]= line_123
    elif "1 Rector St" in combined_array:
        pixels1[37]= line_123
    elif "1 South Ferry Loop" in combined_array:
        pixels1[38]= line_123
    elif "1 South Ferry" in combined_array:
        pixels1[39]= line_123
    elif "2 Wakefield-241 St" in combined_array:
        pixels1[40]= line_123
    elif "2 Nereid Av" in combined_array:
        pixels1[41]= line_123
    elif "2 233 St" in combined_array:
        pixels1[42]= line_123
    elif "2 225 St" in combined_array:
        pixels1[43]= line_123
    elif "2 219 St" in combined_array:
        pixels1[44]= line_123
    elif "2 Gun Hill Rd" in combined_array:
        pixels1[45]= line_123
    elif "2 Burke Av" in combined_array:
        pixels1[46]= line_123
    elif "2 Allerton Av" in combined_array:
        pixels1[47]= line_123
    elif "2 Pelham Pkwy" in combined_array:
        pixels1[48]= line_123
    elif "2 Bronx Park East" in combined_array:
        pixels1[49]= line_123
    elif "2 E 180 St" in combined_array:
        pixels1[50]= line_123
    elif "2 West Farms Sq-E Tremont Av" in combined_array:
        pixels1[51]= line_123
    elif "2 174 St" in combined_array:
        pixels1[52]= line_123
    elif "2 Freeman St" in combined_array:
        pixels1[53]= line_123
    elif "2 Simpson St" in combined_array:
        pixels1[54]= line_123
    elif "2 Intervale Av" in combined_array:
        pixels1[55]= line_123
    elif "2 Prospect Av" in combined_array:
        pixels1[56]= line_123
    elif "2 Jackson Av" in combined_array:
        pixels1[57]= line_123
    elif "2 3 Av-149 St" in combined_array:
        pixels1[58]= line_123
    elif "2 149 St-Grand Concourse" in combined_array:
        pixels1[59]= line_123
    elif "2 135 St" in combined_array:
        pixels1[60]= line_123
    elif "2 125 St" in combined_array:
        pixels1[61]= line_123
    elif "2 116 St" in combined_array:
        pixels1[62]= line_123
    elif "2 Central Park North (110 St)" in combined_array:
        pixels1[63]= line_123
    elif "2 Park Place" in combined_array:
        pixels1[64]= line_123
    elif "2 Fulton St" in combined_array:
        pixels1[65]= line_123
    elif "2 Wall St" in combined_array:
        pixels1[66]= line_123
    elif "2 Clark St" in combined_array:
        pixels1[67]= line_123
    elif "2 Borough Hall" in combined_array:
        pixels1[68]= line_123
    elif "2 Hoyt St" in combined_array:
        pixels1[69]= line_123
    elif "2 Nevins St" in combined_array:
        pixels1[70]= line_123
    elif "2 Atlantic Av-Barclays Ctr" in combined_array:
        pixels1[71]= line_123
    elif "2 Bergen St" in combined_array:
        pixels1[72]= line_123
    elif "2 Grand Army Plaza" in combined_array:
        pixels1[73]= line_123
    elif "2 Eastern Pkwy-Brooklyn Museum" in combined_array:
        pixels1[74]= line_123
    elif "2 Franklin Av-Medgar Evers College" in combined_array:
        pixels1[75]= line_123
    elif "2 President St-Medgar Evers College" in combined_array:
        pixels1[76]= line_123
    elif "2 Sterling St" in combined_array:
        pixels1[77]= line_123
    elif "2 Winthrop St" in combined_array:
        pixels1[78]= line_123
    elif "2 Church Av" in combined_array:
        pixels1[79]= line_123
    elif "2 Beverly Rd" in combined_array:
        pixels1[80]= line_123
    elif "2 Newkirk Av-Little Haiti" in combined_array:
        pixels1[81]= line_123
    elif "2 Flatbush Av-Brooklyn College" in combined_array:
        pixels1[82]= line_123
    elif "2 Nostrand Av" in combined_array:
        pixels1[83]= line_123
    elif "2 Kingston Av" in combined_array:
        pixels1[84]= line_123
    elif "2 Crown Hts-Utica Av" in combined_array:
        pixels1[85]= line_123
    elif "2 Sutter Av-Rutland Rd" in combined_array:
        pixels1[86]= line_123
    elif "2 Saratoga Av" in combined_array:
        pixels1[87]= line_123
    elif "2 Rockaway Av" in combined_array:
        pixels1[88]= line_123
    elif "2 Junius St" in combined_array:
        pixels1[89]= line_123
    elif "2 Pennsylvania Av" in combined_array:
        pixels1[90]= line_123
    elif "2 Van Siclen Av" in combined_array:
        pixels1[91]= line_123
    elif "2 New Lots Av" in combined_array:
        pixels1[92]= line_123
    elif "3 Harlem-148 St" in combined_array:
        pixels1[93]= line_123
    elif "3 145 St" in combined_array:
        pixels1[94]= line_123
    elif "4 Woodlawn" in combined_array:
        pixels1[95]= line_456
    elif "4 Mosholu Pkwy" in combined_array:
        pixels1[96]= line_456
    elif "4 Bedford Park Blvd-Lehman College" in combined_array:
        pixels1[97]= line_456
    elif "4 Kingsbridge Rd" in combined_array:
        pixels1[98]= line_456
    elif "4 Fordham Rd" in combined_array:
        pixels1[99]= line_456
    elif "4 183 St" in combined_array:
        pixels1[100]= line_456
    elif "4 Burnside Av" in combined_array:
        pixels1[101]= line_456
    elif "4 176 St" in combined_array:
        pixels1[102]= line_456
    elif "4 Mt Eden Av" in combined_array:
        pixels1[103]= line_456
    elif "4 170 St" in combined_array:
        pixels1[104]= line_456
    elif "4 167 St" in combined_array:
        pixels1[105]= line_456
    elif "4 161 St-Yankee Stadium" in combined_array:
        pixels1[106]= line_456
    elif "4 149 St-Grand Concourse" in combined_array:
        pixels1[107]= line_456
    elif "4 138 St-Grand Concourse" in combined_array:
        pixels1[108]= line_456
    elif "4 Fulton St" in combined_array:
        pixels1[109]= line_456
    elif "4 Wall St" in combined_array:
        pixels1[110]= line_456
    elif "4 Bowling Green" in combined_array:
        pixels1[111]= line_456
    elif "4 Borough Hall" in combined_array:
        pixels1[112]= line_456
    elif "5 Eastchester-Dyre Av" in combined_array:
        pixels1[113]= line_456
    elif "5 Baychester Av" in combined_array:
        pixels1[114]= line_456
    elif "5 Gun Hill Rd" in combined_array:
        pixels1[115]= line_456
    elif "5 Pelham Pkwy" in combined_array:
        pixels1[116]= line_456
    elif "5 Morris Park" in combined_array:
        pixels1[117]= line_456
    elif "6 Pelham Bay Park" in combined_array:
        pixels1[118]= line_456
    elif "6 Buhre Av" in combined_array:
        pixels1[119]= line_456
    elif "6 Middletown Rd" in combined_array:
        pixels1[120]= line_456
    elif "6 Westchester Sq-E Tremont Av" in combined_array:
        pixels1[121]= line_456
    elif "6 Zerega Av" in combined_array:
        pixels1[122]= line_456
    elif "6 Castle Hill Av" in combined_array:
        pixels1[123]= line_456
    elif "6 Parkchester" in combined_array:
        pixels1[124]= line_456
    elif "6 St Lawrence Av" in combined_array:
        pixels1[125]= line_456
    elif "6 Morrison Av-Soundview" in combined_array:
        pixels1[126]= line_456
    elif "6 Elder Av" in combined_array:
        pixels1[127]= line_456
    elif "6 Whitlock Av" in combined_array:
        pixels1[128]= line_456
    elif "6 Hunts Point Av" in combined_array:
        pixels1[129]= line_456
    elif "6 Longwood Av" in combined_array:
        pixels1[130]= line_456
    elif "6 E 149 St" in combined_array:
        pixels1[131]= line_456
    elif "6 E 143 St-St Mary's St" in combined_array:
        pixels1[132]= line_456
    elif "6 Cypress Av" in combined_array:
        pixels1[133]= line_456
    elif "6 Brook Av" in combined_array:
        pixels1[134]= line_456
    elif "6 3 Av-138 St" in combined_array:
        pixels1[135]= line_456
    elif "6 125 St" in combined_array:
        pixels1[136]= line_456
    elif "6 116 St" in combined_array:
        pixels1[137]= line_456
    elif "6 110 St" in combined_array:
        pixels1[138]= line_456
    elif "6 103 St" in combined_array:
        pixels1[139]= line_456
    elif "6 96 St" in combined_array:
        pixels1[140]= line_456
    elif "6 86 St" in combined_array:
        pixels1[141]= line_456
    elif "6 77 St" in combined_array:
        pixels1[142]= line_456
    elif "6 68 St-Hunter College" in combined_array:
        pixels1[143]= line_456
    elif "6 59 St" in combined_array:
        pixels1[144]= line_456
    elif "6 51 St" in combined_array:
        pixels1[145]= line_456
    elif "6 Grand Central-42 St" in combined_array:
        pixels1[146]= line_456
    elif "6 33 St" in combined_array:
        pixels1[147]= line_456
    elif "6 28 St" in combined_array:
        pixels1[148]= line_456
    elif "6 23 St" in combined_array:
        pixels1[149]= line_456
    elif "6 14 St-Union Sq" in combined_array:
        pixels1[150]= line_456
    elif "6 Astor Pl" in combined_array:
        pixels1[151]= line_456
    elif "6 Bleecker St" in combined_array:
        pixels1[152]= line_456
    elif "6 Spring St" in combined_array:
        pixels1[153]= line_456
    elif "6 Canal St" in combined_array:
        pixels1[154]= line_456
    elif "6 Brooklyn Bridge-City Hall" in combined_array:
        pixels1[155]= line_456
    elif "7 Flushing-Main St" in combined_array:
        pixels1[156]= line_7
    elif "7 Mets-Willets Point" in combined_array:
        pixels1[157]= line_7
    elif "7 111 St" in combined_array:
        pixels1[158]= line_7
    elif "7 103 St-Corona Plaza" in combined_array:
        pixels1[159]= line_7
    elif "7 Junction Blvd" in combined_array:
        pixels1[160]= line_7
    elif "7 90 St-Elmhurst Av" in combined_array:
        pixels1[161]= line_7
    elif "7 82 St-Jackson Hts" in combined_array:
        pixels1[162]= line_7
    elif "7 74 St-Broadway" in combined_array:
        pixels1[163]= line_7
    elif "7 69 St" in combined_array:
        pixels1[164]= line_7
    elif "7 61 St-Woodside" in combined_array:
        pixels1[165]= line_7
    elif "7 52 St" in combined_array:
        pixels1[166]= line_7
    elif "7 46 St-Bliss St" in combined_array:
        pixels1[167]= line_7
    elif "7 40 St-Lowery St" in combined_array:
        pixels1[168]= line_7
    elif "7 33 St-Rawson St" in combined_array:
        pixels1[169]= line_7
    elif "7 Queensboro Plaza" in combined_array:
        pixels1[170]= line_7
    elif "7 Court Sq" in combined_array:
        pixels1[171]= line_7
    elif "7 Hunters Point Av" in combined_array:
        pixels1[172]= line_7
    elif "7 Vernon Blvd-Jackson Av" in combined_array:
        pixels1[173]= line_7
    elif "7 Grand Central-42 St" in combined_array:
        pixels1[174]= line_7
    elif "7 5 Av" in combined_array:
        pixels1[175]= line_7
    elif "7 Times Sq-42 St" in combined_array:
        pixels1[176]= line_7
    elif "7 34 St-Hudson Yards" in combined_array:
        pixels1[177]= line_7
    elif "S Grand Central-42 St" in combined_array:
        pixels1[178]= line_ls
    elif "S Times Sq-42 St" in combined_array:
        pixels1[179]= line_ls
    elif "A Inwood-207 St" in combined_array:
        pixels1[180]= line_ace
    elif "A Dyckman St" in combined_array:
        pixels1[181]= line_ace
    elif "A 190 St" in combined_array:
        pixels1[182]= line_ace
    elif "A 181 St" in combined_array:
        pixels1[183]= line_ace
    elif "A 175 St" in combined_array:
        pixels1[184]= line_ace
    elif "A 168 St" in combined_array:
        pixels1[185]= line_ace
    elif "A 163 St-Amsterdam Av" in combined_array:
        pixels1[186]= line_ace
    elif "A 155 St" in combined_array:
        pixels1[187]= line_ace
    elif "A 145 St" in combined_array:
        pixels1[188]= line_ace
    elif "A 135 St" in combined_array:
        pixels1[189]= line_ace
    elif "A 125 St" in combined_array:
        pixels1[190]= line_ace
    elif "A 116 St" in combined_array:
        pixels1[191]= line_ace
    elif "A Cathedral Pkwy (110 St)" in combined_array:
        pixels1[192]= line_ace
    elif "A 103 St" in combined_array:
        pixels1[193]= line_ace
    elif "A 96 St" in combined_array:
        pixels1[194]= line_ace
    elif "A 86 St" in combined_array:
        pixels1[195]= line_ace
    elif "A 81 St-Museum of Natural History" in combined_array:
        pixels1[196]= line_ace
    elif "A 72 St" in combined_array:
        pixels1[197]= line_ace
    elif "A 59 St-Columbus Circle" in combined_array:
        pixels1[198]= line_ace
    elif "A 50 St" in combined_array:
        pixels1[199]= line_ace
    elif "A 42 St-Port Authority Bus Terminal" in combined_array:
        pixels1[200]= line_ace
    elif "A 34 St-Penn Station" in combined_array:
        pixels1[201]= line_ace
    elif "A 23 St" in combined_array:
        pixels1[202]= line_ace
    elif "A 14 St" in combined_array:
        pixels1[203]= line_ace
    elif "A W 4 St-Wash Sq" in combined_array:
        pixels1[204]= line_ace
    elif "A Spring St" in combined_array:
        pixels1[205]= line_ace
    elif "A Canal St" in combined_array:
        pixels1[206]= line_ace
    elif "A Chambers St" in combined_array:
        pixels1[207]= line_ace
    elif "A Fulton St" in combined_array:
        pixels1[208]= line_ace
    elif "A High St" in combined_array:
        pixels1[209]= line_ace
    elif "A Jay St-MetroTech" in combined_array:
        pixels1[210]= line_ace
    elif "A Hoyt-Schermerhorn Sts" in combined_array:
        pixels1[211]= line_ace
    elif "A Lafayette Av" in combined_array:
        pixels1[212]= line_ace
    elif "A Clinton-Washington Avs" in combined_array:
        pixels1[213]= line_ace
    elif "A Franklin Av" in combined_array:
        pixels1[214]= line_ace
    elif "A Nostrand Av" in combined_array:
        pixels1[215]= line_ace
    elif "A Kingston-Throop Avs" in combined_array:
        pixels1[216]= line_ace
    elif "A Utica Av" in combined_array:
        pixels1[217]= line_ace
    elif "A Ralph Av" in combined_array:
        pixels1[218]= line_ace
    elif "A Rockaway Av" in combined_array:
        pixels1[219]= line_ace
    elif "A Broadway Junction" in combined_array:
        pixels1[220]= line_ace
    elif "A Liberty Av" in combined_array:
        pixels1[221]= line_ace
    elif "A Van Siclen Av" in combined_array:
        pixels1[222]= line_ace
    elif "A Shepherd Av" in combined_array:
        pixels1[223]= line_ace
    elif "A Euclid Av" in combined_array:
        pixels1[224]= line_ace
    elif "A Grant Av" in combined_array:
        pixels1[225]= line_ace
    elif "A 80 St" in combined_array:
        pixels1[226]= line_ace
    elif "A 88 St" in combined_array:
        pixels1[227]= line_ace
    elif "A Rockaway Blvd" in combined_array:
        pixels1[228]= line_ace
    elif "A 104 St" in combined_array:
        pixels1[229]= line_ace
    elif "A 111 St" in combined_array:
        pixels1[230]= line_ace
    elif "A Ozone Park-Lefferts Blvd" in combined_array:
        pixels1[231]= line_ace
    elif "B 21 St-Queensbridge" in combined_array:
        pixels1[232]= line_bdfm
    elif "B Roosevelt Island" in combined_array:
        pixels1[233]= line_bdfm
    elif "B Lexington Av/63 St" in combined_array:
        pixels1[234]= line_bdfm
    elif "B 57 St" in combined_array:
        pixels1[235]= line_bdfm
    elif "B 9 Av" in combined_array:
        pixels1[236]= line_bdfm
    elif "B Fort Hamilton Pkwy" in combined_array:
        pixels1[237]= line_bdfm
    elif "B 50 St" in combined_array:
        pixels1[238]= line_bdfm
    elif "B 55 St" in combined_array:
        pixels1[239]= line_bdfm
    elif "B 62 St" in combined_array:
        pixels1[240]= line_bdfm
    elif "B 71 St" in combined_array:
        pixels1[241]= line_bdfm
    elif "B 79 St" in combined_array:
        pixels1[242]= line_bdfm
    elif "B 18 Av" in combined_array:
        pixels1[243]= line_bdfm
    elif "B 20 Av" in combined_array:
        pixels1[244]= line_bdfm
    elif "B Bay Pkwy" in combined_array:
        pixels1[245]= line_bdfm
    elif "B 25 Av" in combined_array:
        pixels1[246]= line_bdfm
    elif "B Bay 50 St" in combined_array:
        pixels1[247]= line_bdfm
    elif "D Norwood-205 St" in combined_array:
        pixels1[248]= line_bdfm
    elif "D Bedford Park Blvd" in combined_array:
        pixels1[249]= line_bdfm
    elif "D Kingsbridge Rd" in combined_array:
        pixels1[250]= line_bdfm
    elif "D Fordham Rd" in combined_array:
        pixels1[251]= line_bdfm
    elif "D 182-183 Sts" in combined_array:
        pixels1[252]= line_bdfm
    elif "D Tremont Av" in combined_array:
        pixels1[253]= line_bdfm
    elif "D 174-175 Sts" in combined_array:
        pixels1[254]= line_bdfm
    elif "D 170 St" in combined_array:
        pixels1[255]= line_bdfm
    elif "D 167 St" in combined_array:
        pixels1[256]= line_bdfm
    elif "D 161 St-Yankee Stadium" in combined_array:
        pixels1[257]= line_bdfm
    elif "D 155 St" in combined_array:
        pixels1[258]= line_bdfm
    elif "D 145 St" in combined_array:
        pixels1[259]= line_bdfm
    elif "D 7 Av" in combined_array:
        pixels1[260]= line_bdfm
    elif "D 47-50 Sts-Rockefeller Ctr" in combined_array:
        pixels1[261]= line_bdfm
    elif "D 42 St-Bryant Pk" in combined_array:
        pixels1[262]= line_bdfm
    elif "D 34 St-Herald Sq" in combined_array:
        pixels1[263]= line_bdfm
    elif "D 23 St" in combined_array:
        pixels1[264]= line_bdfm
    elif "D 14 St" in combined_array:
        pixels1[265]= line_bdfm
    elif "D W 4 St-Wash Sq" in combined_array:
        pixels1[266]= line_bdfm
    elif "D Broadway-Lafayette St" in combined_array:
        pixels1[267]= line_bdfm
    elif "D Grand St" in combined_array:
        pixels1[268]= line_bdfm
    elif "D Atlantic Av-Barclays Ctr" in combined_array:
        pixels1[269]= line_bdfm
    elif "D Prospect Park" in combined_array:
        pixels1[270]= line_bdfm
    elif "D Parkside Av" in combined_array:
        pixels1[271]= line_bdfm
    elif "D Church Av" in combined_array:
        pixels1[272]= line_bdfm
    elif "D Beverley Rd" in combined_array:
        pixels1[273]= line_bdfm
    elif "D Cortelyou Rd" in combined_array:
        pixels1[274]= line_bdfm
    elif "D Newkirk Plaza" in combined_array:
        pixels1[275]= line_bdfm
    elif "D Avenue H" in combined_array:
        pixels1[276]= line_bdfm
    elif "D Avenue J" in combined_array:
        pixels1[277]= line_bdfm
    elif "D Avenue M" in combined_array:
        pixels1[278]= line_bdfm
    elif "D Kings Hwy" in combined_array:
        pixels1[279]= line_bdfm
    elif "D Avenue U" in combined_array:
        pixels1[280]= line_bdfm
    elif "D Neck Rd" in combined_array:
        pixels1[281]= line_bdfm
    elif "D Sheepshead Bay" in combined_array:
        pixels1[282]= line_bdfm
    elif "D Brighton Beach" in combined_array:
        pixels1[283]= line_bdfm
    elif "D Ocean Pkwy" in combined_array:
        pixels1[284]= line_bdfm
    elif "D W 8 St-NY Aquarium" in combined_array:
        pixels1[285]= line_bdfm
    elif "D Coney Island-Stillwell Av" in combined_array:
        pixels1[286]= line_bdfm
    elif "E World Trade Center" in combined_array:
        pixels1[287]= line_ace
    elif "F Jamaica-179 St" in combined_array:
        pixels1[288]= line_bdfm
    elif "F 169 St" in combined_array:
        pixels1[289]= line_bdfm
    elif "F Parsons Blvd" in combined_array:
        pixels1[290]= line_bdfm
    elif "F Sutphin Blvd" in combined_array:
        pixels1[291]= line_bdfm
    elif "F Briarwood" in combined_array:
        pixels1[292]= line_bdfm
    elif "F Kew Gardens-Union Tpke" in combined_array:
        pixels1[293]= line_bdfm
    elif "F 75 Av" in combined_array:
        pixels1[294]= line_bdfm
    elif "F Court Sq-23 St" in combined_array:
        pixels1[295]= line_bdfm
    elif "F Lexington Av/53 St" in combined_array:
        pixels1[296]= line_bdfm
    elif "F 5 Av/53 St" in combined_array:
        pixels1[297]= line_bdfm
    elif "F 2 Av" in combined_array:
        pixels1[298]= line_bdfm
    elif "F Delancey St-Essex St" in combined_array:
        pixels1[299]= line_bdfm
    elif "F East Broadway" in combined_array:
        pixels1[300]= line_bdfm
    elif "F York St" in combined_array:
        pixels1[301]= line_bdfm
    elif "F Bergen St" in combined_array:
        pixels1[302]= line_bdfm
    elif "F Carroll St" in combined_array:
        pixels1[303]= line_bdfm
    elif "F Smith-9 Sts" in combined_array:
        pixels1[304]= line_bdfm
    elif "F 4 Av-9 St" in combined_array:
        pixels1[305]= line_bdfm
    elif "F 7 Av" in combined_array:
        pixels1[306]= line_bdfm
    elif "F 15 St-Prospect Park" in combined_array:
        pixels1[307]= line_bdfm
    elif "F Fort Hamilton Pkwy" in combined_array:
        pixels1[308]= line_bdfm
    elif "F Church Av" in combined_array:
        pixels1[309]= line_bdfm
    elif "F Ditmas Av" in combined_array:
        pixels1[310]= line_bdfm
    elif "F 18 Av" in combined_array:
        pixels1[311]= line_bdfm
    elif "F Avenue I" in combined_array:
        pixels1[312]= line_bdfm
    elif "F Bay Pkwy" in combined_array:
        pixels1[313]= line_bdfm
    elif "F Avenue N" in combined_array:
        pixels1[314]= line_bdfm
    elif "F Avenue P" in combined_array:
        pixels1[315]= line_bdfm
    elif "F Kings Hwy" in combined_array:
        pixels1[316]= line_bdfm
    elif "F Avenue U" in combined_array:
        pixels1[317]= line_bdfm
    elif "F Avenue X" in combined_array:
        pixels1[318]= line_bdfm
    elif "F Neptune Av" in combined_array:
        pixels1[319]= line_bdfm
    elif "G Jamaica Center-Parsons/Archer" in combined_array:
        pixels1[320]= line_g
    elif "G Sutphin Blvd-Archer Av-JFK Airport" in combined_array:
        pixels1[321]= line_g
    elif "G Jamaica-Van Wyck" in combined_array:
        pixels1[322]= line_g
    elif "G Forest Hills-71 Av" in combined_array:
        pixels1[323]= line_g
    elif "G 67 Av" in combined_array:
        pixels1[324]= line_g
    elif "G 63 Dr-Rego Park" in combined_array:
        pixels1[325]= line_g
    elif "G Woodhaven Blvd" in combined_array:
        pixels1[326]= line_g
    elif "G Grand Av-Newtown" in combined_array:
        pixels1[327]= line_g
    elif "G Elmhurst Av" in combined_array:
        pixels1[328]= line_g
    elif "G Jackson Hts-Roosevelt Av" in combined_array:
        pixels1[329]= line_g
    elif "G 65 St" in combined_array:
        pixels1[330]= line_g
    elif "G Northern Blvd" in combined_array:
        pixels1[331]= line_g
    elif "G 46 St" in combined_array:
        pixels1[332]= line_g
    elif "G Steinway St" in combined_array:
        pixels1[333]= line_g
    elif "G 36 St" in combined_array:
        pixels1[334]= line_g
    elif "G Queens Plaza" in combined_array:
        pixels1[335]= line_g
    elif "G Court Sq" in combined_array:
        pixels1[336]= line_g
    elif "G 21 St" in combined_array:
        pixels1[337]= line_g
    elif "G Greenpoint Av" in combined_array:
        pixels1[338]= line_g
    elif "G Nassau Av" in combined_array:
        pixels1[339]= line_g
    elif "G Metropolitan Av" in combined_array:
        pixels1[340]= line_g
    elif "G Broadway" in combined_array:
        pixels1[341]= line_g
    elif "G Flushing Av" in combined_array:
        pixels1[342]= line_g
    elif "G Myrtle-Willoughby Avs" in combined_array:
        pixels1[343]= line_g
    elif "G Bedford-Nostrand Avs" in combined_array:
        pixels1[344]= line_g
    elif "G Classon Av" in combined_array:
        pixels1[345]= line_g
    elif "G Clinton-Washington Avs" in combined_array:
        pixels1[346]= line_g
    elif "G Fulton St" in combined_array:
        pixels1[347]= line_g
    elif "H Aqueduct Racetrack" in combined_array:
        pixels1[348]= line_h
    elif "H Aqueduct-N Conduit Av" in combined_array:
        pixels1[349]= line_h
    elif "H Howard Beach-JFK Airport" in combined_array:
        pixels1[350]= line_h
    elif "H Broad Channel" in combined_array:
        pixels1[351]= line_h
    elif "H Beach 67 St" in combined_array:
        pixels1[352]= line_h
    elif "H Beach 60 St" in combined_array:
        pixels1[353]= line_h
    elif "H Beach 44 St" in combined_array:
        pixels1[354]= line_h
    elif "H Beach 36 St" in combined_array:
        pixels1[355]= line_h
    elif "H Beach 25 St" in combined_array:
        pixels1[356]= line_h
    elif "H Far Rockaway-Mott Av" in combined_array:
        pixels1[357]= line_h
    elif "H Beach 90 St" in combined_array:
        pixels1[358]= line_h
    elif "H Beach 98 St" in combined_array:
        pixels1[359]= line_h
    elif "H Beach 105 St" in combined_array:
        pixels1[360]= line_h
    elif "H Rockaway Park-Beach 116 St" in combined_array:
        pixels1[361]= line_h
    elif "J 121 St" in combined_array:
        pixels1[362]= line_jz
    elif "J 111 St" in combined_array:
        pixels1[363]= line_jz
    elif "J 104 St" in combined_array:
        pixels1[364]= line_jz
    elif "J Woodhaven Blvd" in combined_array:
        pixels1[365]= line_jz
    elif "J 85 St-Forest Pkwy" in combined_array:
        pixels1[366]= line_jz
    elif "J 75 St-Elderts Ln" in combined_array:
        pixels1[367]= line_jz
    elif "J Cypress Hills" in combined_array:
        pixels1[368]= line_jz
    elif "J Crescent St" in combined_array:
        pixels1[369]= line_jz
    elif "J Norwood Av" in combined_array:
        pixels1[370]= line_jz
    elif "J Cleveland St" in combined_array:
        pixels1[371]= line_jz
    elif "J Van Siclen Av" in combined_array:
        pixels1[372]= line_jz
    elif "J Alabama Av" in combined_array:
        pixels1[373]= line_jz
    elif "J Broadway Junction" in combined_array:
        pixels1[374]= line_jz
    elif "J Chauncey St" in combined_array:
        pixels1[375]= line_jz
    elif "J Halsey St" in combined_array:
        pixels1[376]= line_jz
    elif "J Gates Av" in combined_array:
        pixels1[377]= line_jz
    elif "J Kosciuszko St" in combined_array:
        pixels1[378]= line_jz
    elif "L 8 Av" in combined_array:
        pixels1[379]= line_ls
    elif "L 6 Av" in combined_array:
        pixels1[380]= line_ls
    elif "L 14 St-Union Sq" in combined_array:
        pixels1[381]= line_ls
    elif "L 3 Av" in combined_array:
        pixels1[382]= line_ls
    elif "L 1 Av" in combined_array:
        pixels1[383]= line_ls
    elif "L Bedford Av" in combined_array:
        pixels1[384]= line_ls
    elif "L Lorimer St" in combined_array:
        pixels1[385]= line_ls
    elif "L Graham Av" in combined_array:
        pixels1[386]= line_ls
    elif "L Grand St" in combined_array:
        pixels1[387]= line_ls
    elif "L Montrose Av" in combined_array:
        pixels1[388]= line_ls
    elif "L Morgan Av" in combined_array:
        pixels1[389]= line_ls
    elif "L Jefferson St" in combined_array:
        pixels1[390]= line_ls
    elif "L DeKalb Av" in combined_array:
        pixels1[391]= line_ls
    elif "L Myrtle-Wyckoff Avs" in combined_array:
        pixels1[392]= line_ls
    elif "L Halsey St" in combined_array:
        pixels1[393]= line_ls
    elif "L Wilson Av" in combined_array:
        pixels1[394]= line_ls
    elif "L Bushwick Av-Aberdeen St" in combined_array:
        pixels1[395]= line_ls
    elif "L Broadway Junction" in combined_array:
        pixels1[396]= line_ls
    elif "L Atlantic Av" in combined_array:
        pixels1[397]= line_ls
    elif "L Sutter Av" in combined_array:
        pixels1[398]= line_ls
    elif "L Livonia Av" in combined_array:
        pixels1[399]= line_ls
    elif "L New Lots Av" in combined_array:
        pixels1[400]= line_ls
    elif "L East 105 St" in combined_array:
        pixels1[401]= line_ls
    elif "L Canarsie-Rockaway Pkwy" in combined_array:
        pixels1[402]= line_ls
    elif "M Middle Village-Metropolitan Av" in combined_array:
        pixels1[403]= line_bdfm
    elif "M Fresh Pond Rd" in combined_array:
        pixels1[404]= line_bdfm
    elif "M Forest Av" in combined_array:
        pixels1[405]= line_bdfm
    elif "M Seneca Av" in combined_array:
        pixels1[406]= line_bdfm
    elif "M Myrtle-Wyckoff Avs" in combined_array:
        pixels1[407]= line_bdfm
    elif "M Knickerbocker Av" in combined_array:
        pixels1[408]= line_bdfm
    elif "M Central Av" in combined_array:
        pixels1[409]= line_bdfm
    elif "M Myrtle Av" in combined_array:
        pixels1[410]= line_bdfm
    elif "M Flushing Av" in combined_array:
        pixels1[411]= line_bdfm
    elif "M Lorimer St" in combined_array:
        pixels1[412]= line_bdfm
    elif "M Hewes St" in combined_array:
        pixels1[413]= line_bdfm
    elif "M Marcy Av" in combined_array:
        pixels1[414]= line_bdfm
    elif "M Delancey St-Essex St" in combined_array:
        pixels1[415]= line_bdfm
    elif "M Bowery" in combined_array:
        pixels1[416]= line_bdfm
    elif "M Canal St" in combined_array:
        pixels1[417]= line_bdfm
    elif "M Chambers St" in combined_array:
        pixels1[418]= line_bdfm
    elif "M Fulton St" in combined_array:
        pixels1[419]= line_bdfm
    elif "M Broad St" in combined_array:
        pixels1[420]= line_bdfm
    elif "N 8 Av" in combined_array:
        pixels1[421]= line_nqrw
    elif "N Fort Hamilton Pkwy" in combined_array:
        pixels1[422]= line_nqrw
    elif "N New Utrecht Av" in combined_array:
        pixels1[423]= line_nqrw
    elif "N 18 Av" in combined_array:
        pixels1[424]= line_nqrw
    elif "N 20 Av" in combined_array:
        pixels1[425]= line_nqrw
    elif "N Bay Pkwy" in combined_array:
        pixels1[426]= line_nqrw
    elif "N Kings Hwy" in combined_array:
        pixels1[427]= line_nqrw
    elif "N Avenue U" in combined_array:
        pixels1[428]= line_nqrw
    elif "N 86 St" in combined_array:
        pixels1[429]= line_nqrw
    elif "N S.B. Coney Island" in combined_array:
        pixels1[430]= line_nqrw
    elif "Q Canal St" in combined_array:
        pixels1[431]= line_nqrw
    elif "Q 72 St" in combined_array:
        pixels1[432]= line_nqrw
    elif "Q 86 St" in combined_array:
        pixels1[433]= line_nqrw
    elif "Q 96 St" in combined_array:
        pixels1[434]= line_nqrw
    elif "R Astoria-Ditmars Blvd" in combined_array:
        pixels1[435]= line_nqrw
    elif "R Astoria Blvd" in combined_array:
        pixels1[436]= line_nqrw
    elif "R 30 Av" in combined_array:
        pixels1[437]= line_nqrw
    elif "R Broadway" in combined_array:
        pixels1[438]= line_nqrw
    elif "R 36 Av" in combined_array:
        pixels1[439]= line_nqrw
    elif "R 39 Av-Dutch Kills" in combined_array:
        pixels1[440]= line_nqrw
    elif "R Queensboro Plaza" in combined_array:
        pixels1[441]= line_nqrw
    elif "R Lexington Av/59 St" in combined_array:
        pixels1[442]= line_nqrw
    elif "R 5 Av/59 St" in combined_array:
        pixels1[443]= line_nqrw
    elif "R 57 St-7 Av" in combined_array:
        pixels1[444]= line_nqrw
    elif "R 49 St" in combined_array:
        pixels1[445]= line_nqrw
    elif "R Times Sq-42 St" in combined_array:
        pixels1[446]= line_nqrw
    elif "R 34 St-Herald Sq" in combined_array:
        pixels1[447]= line_nqrw
    elif "R 28 St" in combined_array:
        pixels1[448]= line_nqrw
    elif "R 23 St" in combined_array:
        pixels1[449]= line_nqrw
    elif "R 14 St-Union Sq" in combined_array:
        pixels1[450]= line_nqrw
    elif "R 8 St-NYU" in combined_array:
        pixels1[451]= line_nqrw
    elif "R Prince St" in combined_array:
        pixels1[452]= line_nqrw
    elif "R Canal St" in combined_array:
        pixels1[453]= line_nqrw
    elif "R City Hall" in combined_array:
        pixels1[454]= line_nqrw
    elif "R Cortlandt St" in combined_array:
        pixels1[455]= line_nqrw
    elif "R Rector St" in combined_array:
        pixels1[456]= line_nqrw
    elif "R Whitehall St-South Ferry" in combined_array:
        pixels1[457]= line_nqrw
    elif "R Court St" in combined_array:
        pixels1[458]= line_nqrw
    elif "R Jay St-MetroTech" in combined_array:
        pixels1[459]= line_nqrw
    elif "R DeKalb Av" in combined_array:
        pixels1[460]= line_nqrw
    elif "R Atlantic Av-Barclays Ctr" in combined_array:
        pixels1[461]= line_nqrw
    elif "R Union St" in combined_array:
        pixels1[462]= line_nqrw
    elif "R 4 Av-9 St" in combined_array:
        pixels1[463]= line_nqrw
    elif "R Prospect Av" in combined_array:
        pixels1[464]= line_nqrw
    elif "R 25 St" in combined_array:
        pixels1[465]= line_nqrw
    elif "R 36 St" in combined_array:
        pixels1[466]= line_nqrw
    elif "R 45 St" in combined_array:
        pixels1[467]= line_nqrw
    elif "R 53 St" in combined_array:
        pixels1[468]= line_nqrw
    elif "R 59 St" in combined_array:
        pixels1[469]= line_nqrw
    elif "R Bay Ridge Av" in combined_array:
        pixels1[470]= line_nqrw
    elif "R 77 St" in combined_array:
        pixels1[471]= line_nqrw
    elif "R 86 St" in combined_array:
        pixels1[472]= line_nqrw
    elif "R Bay Ridge-95 St" in combined_array:
        pixels1[473]= line_nqrw
    elif "S Franklin Av" in combined_array:
        pixels1[474]= line_ls
    elif "S Park Pl" in combined_array:
        pixels1[475]= line_ls
    elif "S Botanic Garden" in combined_array:
        pixels1[476]= line_ls
    elif "S Tottenville" in combined_array:
        pixels1[477]= line_ls
    elif "S Arthur Kill" in combined_array:
        pixels1[478]= line_ls
    elif "S Richmond Valley" in combined_array:
        pixels1[479]= line_ls
    elif "S Pleasant Plains" in combined_array:
        pixels1[480]= line_ls
    elif "S Prince's Bay" in combined_array:
        pixels1[481]= line_ls
    elif "S Huguenot" in combined_array:
        pixels1[482]= line_ls
    elif "S Annadale" in combined_array:
        pixels1[483]= line_ls
    elif "S Eltingville" in combined_array:
        pixels1[484]= line_ls
    elif "S Great Kills" in combined_array:
        pixels1[485]= line_ls
    elif "S Bay Terrace" in combined_array:
        pixels1[486]= line_ls
    elif "S Oakwood Heights" in combined_array:
        pixels1[487]= line_ls
    elif "S New Dorp" in combined_array:
        pixels1[488]= line_ls
    elif "S Grant City" in combined_array:
        pixels1[489]= line_ls
    elif "S Jefferson Av" in combined_array:
        pixels1[490]= line_ls
    elif "S Dongan Hills" in combined_array:
        pixels1[491]= line_ls
    elif "S Old Town" in combined_array:
        pixels1[492]= line_ls
    elif "S Grasmere" in combined_array:
        pixels1[493]= line_ls
    elif "S Clifton" in combined_array:
        pixels1[494]= line_ls
    elif "S Stapleton" in combined_array:
        pixels1[495]= line_ls
    elif "S Tompkinsville" in combined_array:
        pixels1[496]= line_ls
    elif "S St George" in combined_array:
        pixels1[497]= line_ls
    else:
        ()
    
    # temp while testing to not use extra power
    time.sleep(10)
    pixels1.fill((0, 0, 0))
    

else: 
    ()
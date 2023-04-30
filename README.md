# MTA-LED-Map-Raspi
(Eventually...) A single python file that will pull NYC-MTA GTFS data and assign it to individually addressable LEDs. May also include NJ PATH data...


Steps: 

Install python3. This was tested on windows 10 22H2 with Python 3.10 and on a raspberry Pi Zero with Python 3.9.2 

Install the following dependancies: 

pip install time
pip install datetime
pip install nyct_gtfs
pip install python-dotenv

You can ignore warnings about any scripts not being in PATH. 
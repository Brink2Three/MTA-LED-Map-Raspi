# MTA-LED-Map-Raspi
(Eventually...) A single python file that will pull NYC-MTA GTFS data and assign it to individually addressable LEDs. May also include NJ PATH data...


Steps: 

Install python3. This was tested on windows 10 22H2 with Python 3.10 and on a raspberry Pi Zero with Python 3.9.2. 
Only the requests testing will work on windows, as the LED code will attempt to connect to non-existent GPIO pins. 


Install the following dependancies: 

pip install time
pip install datetime
pip install nyct_gtfs
pip install python-dotenv

You can ignore warnings about any scripts not being in PATH. 


Create a file in the root directory called ".env" and add the following to it: api_key = "YOUR API KEY HERE"
Replace "YOUR API KEY HERE" with your actual MTA API key. 







LED size used: .2" x .2", inner circle is .15" in diameter. 
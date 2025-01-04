# MTA-LED-Map-Raspi

## IN PROGRESS

A single python file that will pull NYC-MTA GTFS data and assign it to individually addressable LEDs. May also include NJ PATH data if I ever figure out how to parse their API.

## To make this yourself

### Parts

- Raspberry Pi (I have tested with a Zero1 W and a Zero 2 W)
- a 5V 8A Power supply (Enough to power the entire board you connect)
- Dupont connectors (for connecting power supply to board/Raspi for now)
- A board, ordered from JCLPCB, PCBway or any PCB order vendor. (see Maps/PCB Gerber Files)

### Software Steps

Install python3. This was tested on windows 10 22H2 with Python 3.10 and on a raspberry Pi Zero2 with Python 3.9.2.
Only the requests testing will work on windows, as the LED code will attempt to connect to non-existent GPIO pins.
//TODO Make "test display" via console to display labeled stops with LED colors.

Install the following dependancies as root. As far as I know, you cannot install them in a virtual environment. They need root access to use the GPIO pins.

```bash
sudo pip install rpi_ws281x
sudo pip install adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
sudo pip install time
sudo pip install datetime
sudo pip install nyct_gtfs
```

(python-dotenv used to be required, but nyct_gtfs no longer requires API keys!)

You can ignore warnings about any scripts not being in PATH.

Clone this repo to the raspberry pi, running raspbian (raspberry piOS) lite or ubuntu server.

Depending on what boards you have connected, run the related "displaymode.py" script.
*THIS WILL TAKE A MINUTE TO UPDATE.*
The raspberry pi Zero 1 is SLOW to read the SD card, and takes about 45-75 seconds per cycle.
The Pi Zero 2 is faster, averaging about 15-18 seconds per cycle for the bothalf-displaymode file.

If you get lights, you did it! You can now add the script to crontab to have it run on an interval. I suggest once every 2 minutes, as slow internet or SD cards can cause the runtime to go over 1 minute.

## EXPIERMENTAL

In the setup folder, there is a script that moves the nyct-gtfs folder to a ramdisk (from the default sudo install location). This is meant to decrease the wear and load time of the package, since it polls files in this directory 44 times per run for just the bothalf displaymode script. The plan is eventually to have all of this run persistently, but for now I just run it on startup and put the bothalf displaymode script in root's crontab to run it once every 2 minutes.

If you do not clear this before rebooting the pi, it *will* break. If it does, run `sudo pip install nyct_gtfs --force-reinstall`.
Example of error message:
```bash
Traceback (most recent call last):
  File "/home/brink/MTA-LED-Map-Raspi/mtaled-bothalf-displaymode.py", line 9, in <module>
    from nyct_gtfs import NYCTFeed
ImportError: cannot import name 'NYCTFeed' from 'nyct_gtfs' (unknown location)
```

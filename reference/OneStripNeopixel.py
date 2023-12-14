
import time
import board
import neopixel

pixels1 = neopixel.NeoPixel(board.D18, 87, brightness=.15)

x=0


pixels1.fill((15, 15, 15))

time.sleep(3)

while x<159:
    
    pixels1[x] = (0, 0, 255)
    pixels1[x-1] = (15, 15, 15)
    x=x+1
    time.sleep(0.1)

while x>-1:
    pixels1[x] = (255, 0, 0)
    pixels1[x+1] = (15, 15, 15)
    x=x-1
    time.sleep(0.1)
   
while x<159:
    
    pixels1[x] = (255, 0, 255)
    pixels1[x-1] = (15, 15, 15)
    x=x+1
    time.sleep(0.1)

while x>-1:
    pixels1[x] = (255, 255, 0)
    pixels1[x+1] = (15, 15, 15)
    x=x-1
    time.sleep(0.1)

time.sleep(5)

pixels1.fill((0, 0, 0))



import time
import board
import neopixel

pixels1 = neopixel.NeoPixel(board.D18, 180, brightness=.15)

x=0

# Line colors so I don't have to type the codes out
line_123 = (238, 53, 46) # Too pink
line_456 = (0, 147, 60)
line_ace = (0, 57, 166)
line_7 = (185, 51, 173)
line_bdfm = (255, 99, 25)
line_jz = (153, 102, 51)
line_nqrw = (252, 204, 10)
line_ls = (128, 129, 131)
bg = (15, 15, 15)

pixels1.fill((15, 15, 15))

time.sleep(3)

while x<159:
    
    pixels1[x] = line_123
    pixels1[x-1] = bg
    x=x+1
    time.sleep(0.1)

while x>-1:
    pixels1[x] = line_456
    pixels1[x+1] = bg
    x=x-1
    time.sleep(0.1)
   
while x<159:
    
    pixels1[x] = line_ace
    pixels1[x-1] = bg
    x=x+1
    time.sleep(0.1)

while x>-1:
    pixels1[x] = line_7
    pixels1[x+1] = bg
    x=x-1
    time.sleep(0.1)

while x<159:
    
    pixels1[x] = line_bdfm
    pixels1[x-1] = bg
    x=x+1
    time.sleep(0.1)

while x>-1:
    pixels1[x] = line_jz
    pixels1[x+1] = bg
    x=x-1
    time.sleep(0.1)

while x<159:
    
    pixels1[x] = line_nqrw
    pixels1[x-1] = bg
    x=x+1
    time.sleep(0.1)

while x>-1:
    pixels1[x] = line_ls
    pixels1[x+1] = bg
    x=x-1
    time.sleep(0.1)    

time.sleep(5)

pixels1.fill((0, 0, 0))


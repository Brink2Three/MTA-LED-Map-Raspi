
import time
import board
import neopixel

pixels1 = neopixel.NeoPixel(board.D18, 180, brightness=.15)

x=0

# Line colors so I don't have to type the codes out
line_123 = (127, 0, 0)
line_456 = (0, 127, 7)
line_ace = (6, 20, 127)
line_7 = (100, 0, 100)
line_bdfm = (127, 50, 14)
line_jz = (153, 102, 51)
line_nqrw = (252, 204, 10)
line_ls = (128, 129, 131)
bg = (15, 15, 15)

pixels1.fill((15, 15, 15))

time.sleep(3)

print( "123 is currently shown")
while x<20:
    pixels1[x] = line_123
    pixels1[x-3] = bg
    x=x+1
    time.sleep(0.5)

print( "456 is currently shown")
while x>-1:
    pixels1[x] = line_456
    pixels1[x+3] = bg
    x=x-1
    time.sleep(0.5)

print( "ACE is currently shown")   
while x<20:
    pixels1[x] = line_ace
    pixels1[x-3] = bg
    x=x+1
    time.sleep(0.5)

print( "7 is currently shown")
while x>-1:
    pixels1[x] = line_7
    pixels1[x+3] = bg
    x=x-1
    time.sleep(0.5)

print( "BDFM is currently shown")
while x<20:
    pixels1[x] = line_bdfm
    pixels1[x-3] = bg
    x=x+1
    time.sleep(0.5)

print( "JZ is currently shown")
while x>-1:
    pixels1[x] = line_jz
    pixels1[x+3] = bg
    x=x-1
    time.sleep(0.5)

print( "NQRW is currently shown")
while x<20:
    pixels1[x] = line_nqrw
    pixels1[x-3] = bg
    x=x+1
    time.sleep(0.5)

print( "LS is currently shown")
while x>-1:
    pixels1[x] = line_ls
    pixels1[x+3] = bg
    x=x-1
    time.sleep(0.5)    

time.sleep(5)

pixels1.fill((0, 0, 0))

time.sleep(0.25)

pixels1[1] = line_123
pixels1[2] = line_456
pixels1[3] = line_ace
pixels1[4] = line_7
pixels1[5] = line_bdfm
pixels1[6] = line_jz
pixels1[7] = line_nqrw
pixels1[8] = line_ls

time.sleep(5)

pixels1.fill((0, 0, 0))


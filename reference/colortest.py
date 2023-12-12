
import time
import board
import neopixel

pixels1 = neopixel.NeoPixel(board.D18, 85, brightness=.20)

x=0

# Line colors so I don't have to type the codes out
line_123 = (127, 0, 0)
line_456 = (0, 127, 7)
line_ace = (6, 20, 127)
line_7 = (100, 0, 100)
line_bdfm = (255, 107, 0)
line_jz = (190, 50, 14)
line_nqrw = (252, 204, 10)
line_ls = (128, 129, 131)
bg = (25, 25, 25)

pixels1.fill((25, 25, 25))

time.sleep(3)

print( "123 is currently shown")
while x<85:
    pixels1[x] = line_123
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)

print( "456 is currently shown")
while x<85:
    pixels1[x] = line_456
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)
    x=0

print( "ACE is currently shown")   
while x<85:
    pixels1[x] = line_ace
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)
    x=0

print( "7 is currently shown")
while x<85:
    pixels1[x] = line_7
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)
    x=0

print( "BDFM is currently shown")
while x<85:
    pixels1[x] = line_bdfm
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)
    x=0

print( "JZ is currently shown")
while x<85:
    pixels1[x] = line_jz
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)
    x=0

print( "NQRW is currently shown")
while x<85:
    pixels1[x] = line_nqrw
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)
    x=0

print( "LS is currently shown")
while x<85:
    pixels1[x] = line_ls
    pixels1[x-5] = bg
    x=x+1
    time.sleep(0.5)
    x=0    

time.sleep(5)

pixels1.fill((0, 0, 0))

time.sleep(0.25)

pixels1[1,5,18,20,21,33,39,47,49,51,57,60,66,69,81,83] = line_123
pixels1[3,6] = line_456
pixels1[82,68,67,59,50,48,38,32,22,19,13] = line_ace
pixels1[58,] = line_7
pixels1[5] = line_bdfm
pixels1[6] = line_jz
pixels1[7] = line_nqrw
pixels1[8] = line_ls

time.sleep(10)

pixels1.fill((0, 0, 0))



import time
import board
import neopixel

pixels1 = neopixel.NeoPixel(board.D18, 87, brightness=.20)

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

pixels1[0] = line_123
pixels1[1] = line_123 # Missing LED #1
pixels1[2] = line_123 # Missing LED #2
pixels1[17] = line_123
pixels1[19] = line_123
pixels1[20] = line_123
pixels1[32] = line_123
pixels1[38] = line_123
pixels1[46] = line_123
pixels1[48] = line_123
pixels1[50] = line_123
pixels1[56] = line_123
pixels1[59] = line_123
pixels1[65] = line_123
pixels1[68] = line_123
pixels1[80] = line_123
pixels1[82] = line_123

pixels1[2] = line_456
pixels1[5] = line_456
pixels1[12] = line_ace
pixels1[18] = line_ace
pixels1[21] = line_ace
pixels1[31] = line_ace
pixels1[37] = line_ace
pixels1[47] = line_ace
pixels1[49] = line_ace
pixels1[58] = line_ace
pixels1[66] = line_ace
pixels1[67] = line_ace
pixels1[81] = line_ace

pixels1[57] = line_7
pixels1[11] = line_bdfm
pixels1[12] = line_jz
pixels1[4] = line_nqrw
pixels1[7] = line_nqrw
pixels1[13] = line_nqrw

pixels1[14] = line_ls

time.sleep(10)

pixels1.fill((0, 0, 0))


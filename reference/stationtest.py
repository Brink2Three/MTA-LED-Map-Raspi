
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
pixels1[19] = line_123
pixels1[21] = line_123
pixels1[22] = line_123
pixels1[34] = line_123
pixels1[40] = line_123
pixels1[48] = line_123
pixels1[50] = line_123
pixels1[52] = line_123
pixels1[58] = line_123
pixels1[61] = line_123
pixels1[67] = line_123
pixels1[70] = line_123
pixels1[82] = line_123
pixels1[84] = line_123

pixels1[4] = line_456
pixels1[7] = line_456
pixels1[14] = line_ace
pixels1[20] = line_ace
pixels1[23] = line_ace
pixels1[33] = line_ace
pixels1[39] = line_ace
pixels1[49] = line_ace
pixels1[51] = line_ace
pixels1[60] = line_ace
pixels1[68] = line_ace
pixels1[69] = line_ace
pixels1[83] = line_ace

pixels1[59] = line_7
pixels1[13] = line_bdfm
pixels1[14] = line_jz
pixels1[5] = line_nqrw
pixels1[9] = line_nqrw
pixels1[15] = line_nqrw

pixels1[16] = line_ls

time.sleep(10)

pixels1.fill((0, 0, 0))


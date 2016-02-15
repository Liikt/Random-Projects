import sys
import math

width = int(input())
height = int(input())

x = -1
y = -1
line = []

def findShit(x,y):
    xr = -1
    yr = -1
    xu = -1
    yu = -1
    for i in range(x+1,width):
        if line[y][i] == '0':
            xr = i
            yr = y
            break
    for i in range(y+1,height):
        if line[i][x] == '0':
            yu = i
            xu = x
            break
    print('%d %d %d %d %d %d' % (x, y, xr, yr, xu, yu))

for i in range(height):
    line.append(input())

ity = 0
for y in line:
    itx = 0
    for x in y:
        if x == '0':
            findShit(itx, ity)
        itx += 1
    ity += 1

import sys
import math
import threading

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
indiemap=[]
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # each line represents a line in the grid and contains W integers T. The absolute value of T specifies the type of the room. If T is negative, the room cannot be rotated.
    indiemap.append([int(x) for x in line.split()])
    #print(indiemap[i],file=sys.stderr)
ex = int(input())  # the coordinate along the X axis of the exit.

#types -> [y->coordinate,x->coordinate)
types=[]
types.append({'TOP':[0,0],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[1,0],'LEFT':[1,0],'RIGHT':[1,0]})
types.append({'TOP':[0,0],'LEFT':[0,1],'RIGHT':[0,-1]})
types.append({'TOP':[1,0],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[0,-1],'LEFT':[0,0],'RIGHT':[1,0]})
types.append({'TOP':[0,1],'LEFT':[1,0],'RIGHT':[0,0]})
types.append({'TOP':[0,0],'LEFT':[0,1],'RIGHT':[0,-1]})
types.append({'TOP':[1,0],'LEFT':[0,0],'RIGHT':[1,0]})
types.append({'TOP':[0,0],'LEFT':[1,0],'RIGHT':[1,0]})
types.append({'TOP':[1,0],'LEFT':[1,0],'RIGHT':[0,0]})
types.append({'TOP':[0,-1],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[0,1],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[0,0],'LEFT':[0,0],'RIGHT':[1,0]})
types.append({'TOP':[0,0],'LEFT':[1,0],'RIGHT':[0,0]})

# game loop
while True:
    xi, yi, posi = input().split()
    xi = int(xi)
    yi = int(yi)
    r = int(input())  # the number of rocks currently in the grid.
    for i in range(r):
        xr, yr, posr = input().split()
        xr = int(xr)
        yr = int(yr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # One line containing on of three commands: 'X Y LEFT', 'X Y RIGHT' or 'WAIT'
    print("2 1 LEFT")

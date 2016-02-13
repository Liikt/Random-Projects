import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
jump = False
while True:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    if jump == False:
        if coord_x == road-1:
            jump = True
            print("JUMP")   
        elif coord_x < road-1:
            if speed < gap+1:
                print("SPEED")
            elif speed > gap+1:
                print("SLOW")
            else:
                print("WAIT")
        
    else:
        print("SLOW")
    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.


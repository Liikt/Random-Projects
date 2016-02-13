import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    x = initial_tx - light_x
    y = initial_ty - light_y
    
    if x < 0 and y < 0:
        initial_tx+=1
        initial_ty+=1
        print("SE")
    elif x < 0 and y > 0:
        initial_tx+=1
        initial_ty-=1
        print("NE")
    elif x > 0 and y < 0:
        initial_tx-=1
        initial_ty+=1
        print("SW")
    elif x > 0 and y > 0:
        initial_tx-=1
        initial_ty-=1
        print("SE")
    elif x == 0 or y == 0:
        if abs(y) in range(1,18):
            if y > 0:
                initial_ty-=1
                print("N")
            else:
                initial_ty+=1
                print("S")
        if abs(x) in range(1,40):
            if x > 0:
                initial_tx-=1
                print("W")
            else:
                initial_tx+=1
                print("E")
            
    # A single line providing the move to be made: N NE E SE S SW W or NW

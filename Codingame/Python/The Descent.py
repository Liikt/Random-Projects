# import sys
# import math

# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.

# sent = False
# # game loop
# while True:
#     space_x, space_y = [int(i) for i in input().split()]
#     maxn = 0
#     maxh = 0
#     for i in range(8):
#         x = int(input())
#         print(str(maxh),file=sys.stderr)
#         if x > maxh:
#             maxh = x
#             maxn = i
#         mountain_h = x  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
    
#     # Write an action using print
#     # To debug: print("Debug messages...", file=sys.stderr)
    
#     if space_x != maxn:
#         print("HOLD")
#     else:
#         print("FIRE")
    
#     # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).

###########################
## This task got changed ##
###########################

## This is now the newer solution
while True:
    mnt = []
    for i in range(8):
        mnt.append(int(input()))
    print(mnt.index(max(mnt)))

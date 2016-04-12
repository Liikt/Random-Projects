import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

res = 10000000
rest = 0
inp = temps.split()
sent = False
for i in inp:
    if abs(int(i)) < res:
        res = abs(int(i))
        rest = int(i)
        if rest < 0:
            sent = False
        else:
            sent = True
    elif abs(int(i)) == res and sent == False:
        rest = int(i)
    elif abs(int(i)) == res and sent == True:
        rest = abs(int(i))

print(str(rest))
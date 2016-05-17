import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def rec(x, y):
    if x < 0 or y < 0:
        return
    global mem
    try:
        if str(x)+' '+str(y) in mem or lmap[y][x] == '#':
            return
        else:
            mem.append(str(x)+' '+str(y))
            rec(x+1,y)
            rec(x-1,y)
            rec(x,y+1)
            rec(x,y-1)
    except:
        return

    


def first(x, y):
    global mem
    try:
        if lmap[y][x] == '#':
            return
        else:
            rec(x, y)
    except:
        return

l = int(input())
h = int(input())
lmap=[]
mem=[]
count=0
for i in range(h):
    line=input()
    if '#' in line:
        count += line.count('#')
    lmap.append(line)
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if count > 3:
        first(x,y)
        print(len(mem))
        mem=[]
    else:
        print(h*l-count)


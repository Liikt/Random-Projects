import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

zw=[]

def foo(a,b):
    return min(abs(a[b]-a[b-1]),abs(a[b]-a[b+1]))

def bar(a,b):
    return abs(a[b]-a[b-1])

mini = 1000000

for i in range(n):
    pi = int(input())
    zw.append(pi)
        
zw.sort()

if len(zw)%2==0:
    for i in range(1,len(zw)-1,2):
        #print('1: ' + str(i) + ' len: '+ str(len(zw)),file=sys.stderr)
        test = foo(zw,i)
        if test < mini:
            mini = test
    test = bar(zw,len(zw)-1)
    if test < mini:
        mini = test
else:
    for i in range(1,len(zw)-1,2):
        #print('2: ' + str(i) + ' len: '+ str(len(zw)),file=sys.stderr)
        test = foo(zw,i)
        if test < mini:
            mini = test

print(zw,file=sys.stderr)
            
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(mini)

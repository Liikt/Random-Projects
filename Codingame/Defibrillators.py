from __future__ import division
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(',','.'))
lat = float(input().replace(',','.'))
n = int(input())
mini = 10000000000.0

def lang(a):
    return a[len(a)-2].replace(',','.')
    
def lati(a):
    return a[len(a)-1].replace(',','.')
    
def strip(a):
    for i in a:
        if len(i) == 0:
            a.remove('')

zw = []

for i in range(n):
    defib = input()
    defib = defib[2:]
    defib = defib.split(';')
    strip(defib)
    zw.append(defib)
    
it = 0
erg = 0

for i in zw:
    x = (lon - float(lang(i)))*math.cos((lat+float(lati(i)))/2)
    y = lat-float(lati(i))
    d = math.sqrt((x*x)+(y*y))*6371
    print(d,file=sys.stderr)
    print(i,file=sys.stderr)
    print('-------------------------',file=sys.stderr)
    if d < mini:
        mini = d
        erg = it
    it += 1
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


try:
    h = int(zw[erg][0])
    print(zw[erg][1])
except:
    print(zw[erg][0])

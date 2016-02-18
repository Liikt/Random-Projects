dist = 0

n = int(input())
houses = []
for i in range(n):
    houses.append([int(j) for j in input().split()])

def calcFitness(j):
    above = 0
    under = 0
    on = 0
    for h in houses:
        if h[1] > y:
            above+=1
        elif h[1] < y:
            under+= 1
        else:
            on+=1
    if above - under > on:
        return j
    elif under - above > on:
        return -j
    else:
        return 0

minx = min(houses)[0]
maxx = max(houses)[0]

dist+=(maxx-minx)

maxi = 0
mini = 0

if n > 0:
    mini = houses[0][1]
    maxi = houses[0][1]
    
    for h in houses:
        if h[1] < mini:
            mini = h[1]
        if h[1] > maxi:
            maxi = h[1]

y = int((maxi+mini)/2)

j = 1
zwz = 0
while j != 0:
    zw = calcFitness(j)
    if zwz == zw and zwz != 0:                       #sprung in gleiche richtung
        j+=1
    elif zw == -zwz and zwz != 0:                    #sprung in andere richtung
        j-=1
    elif zw == 0:
        j -= 1
    y += zw
    zwz = zw

for h in houses:
    dist+=abs(y-h[1])
    
if n == 1:
    print(0)
else:
    print(dist)
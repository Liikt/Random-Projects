import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def loop(r):
    global rides
    global money
    money *= math.floor()

groupsception=[]
places, rides, nG = [int(i) for i in input().split()]
groups=[]       #ppl waiting to ride
left=-1
for i in range(nG):
    groups.append(int(input()))
groupsception.append(str(groups))
#print("Places per ride:",places,"\nRides:",rides,"\nGroups:",nG, groups, file=sys.stderr)

money=0
for r in range(rides):
    onride=[]   #ppl on this particular ride
    ppl=0
    while len(groups)>0 and ppl+groups[0]<=places:
        g=groups.pop(0)
        ppl+=g
        onride.append(g)
        money+=g
    groups+=onride
    print('Groups: ', groups, 'Groupsception: ', groupsception, 'Bool: ', groups in groupsception, file=sys.stderr)
    if str(groups) in groupsception:
        #left=r+1
        loop(r)
        break
    else:
        groupsception.append(str(groups))

    
# if left == -1:
#     left = rides

# money *= math.floor(rides/left)
# for x in range(rides%left):
#     onride=[]   #ppl on this particular ride
#     ppl=0
#     while len(groups)>0 and ppl+groups[0]<=places:
#         g=groups.pop(0)
#         ppl+=g
#         onride.append(g)
#         money+=g
#     groups+=onride

print(money)

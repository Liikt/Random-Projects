import sys
import math
 
loop = False
path = []
town = []   #will be an 2d char array, BUT CHARACTERS HERE ARE town[y][x] not x,y!!
teleport = []               #form=[[tp1x,tp1y],[tp2x,tp2y]]
bender = [[], 'SOUTH', 0]   #form= [[x,y], direction, berserkmode(toggle)]
history =[]         #history of the moves for loop detection (will contain bender+townhash)
priority = ['SOUTH', 'EAST', 'NORTH', 'WEST']
pr_short = ['S', 'E', 'N', 'W']
groundmod=['T','I','B','S', 'E', 'N', 'W']
wallmod = ['X','#']
direc_to_move = {'SOUTH':[0, 1], 'EAST':[1, 0], 'NORTH':[0, -1], 'WEST':[-1, 0]}
c_to_direc = {'S':'SOUTH', 'E':'EAST', 'N':'NORTH', 'W':'WEST'}
 
def townhash(l,c):
    #global town
    townval=0
    for i in range(l):
        for j in range(c):
            townval+=ord(town[i][j])
    return(townval)
 
   
def warp():
    #global bender
    #global teleport
    if bender[0]==teleport[0]:
        bender[0]=teleport[1]
    else:
        bender[0]=teleport[0]
 
def prio_reverse():
    #global priority
    priority.reverse()
   
def beertoggle():
    #global bender
    bender[2]=(bender[2]+1)%2
   
grounddic={'T':warp, 'I':prio_reverse, 'B':beertoggle}
       
def newpos():   #returns new bender[0], doesnt overwrite
    #global bender
    move=[0,0]
    move[0]+=direc_to_move[bender[1]][0]
    move[1]+=direc_to_move[bender[1]][1]
    move[0]+=bender[0][0]
    move[1]+=bender[0][1]
    return move
 
def print_town(l,c):
    #global town
    for i in range(l):
        line=''
        for j in range(c):
            line+=town[i][j]
        print(line, file=sys.stderr)
   
   
l, c = [int(i) for i in input().split()]   
   
for i in range(l):
    row = input()
    town.append([])
    for j in range(c):
        town[i].append(row[j])
        if row[j]=='@':
            bender[0].append(j)     #x=j
            bender[0].append(i)     #y=i
        if row[j]=='T':
            teleport.append([])
            teleport[len(teleport)-1].append(j)
            teleport[len(teleport)-1].append(i)
 
 
print_town(l,c)
 
ground=town[bender[0][1]][bender[0][0]]
while ground!='$' and loop!=True:
    #first check the ground, then the walls, then move
    print('ground: g '+str(ground)+' g', file=sys.stderr)
    if ground in groundmod:
        if ground in pr_short:
            bender[1]=c_to_direc[ground]
        else:
            grounddic[ground]()
    frontpos=newpos()           #from: [x,y]
    front=town[frontpos[1]][frontpos[0]]
    direc=0     #index for priority list
    print('front: f '+str(front)+' f', file=sys.stderr)
    while front in wallmod:
        print('WALL', file=sys.stderr)
        if front=='X' and bender[2]==1:
            town[frontpos[1]][frontpos[0]]=' '
            break
        bender[1]=priority[direc]
        direc+=1
        frontpos=newpos()
        front=town[frontpos[1]][frontpos[0]]
 
    bender[0]=newpos()
    ground=town[bender[0][1]][bender[0][0]]
    path.append(bender[1])
   
    #loop detection:
    historyentry=[]
    historyentry.append([])
    historyentry[0].append(bender[0][0])
    historyentry[0].append(bender[0][1])
    historyentry.append(bender[1])
    historyentry.append(bender[2])
    historyentry.append(townhash(l,c))
    if historyentry not in history:
        history.append(historyentry)
    else:
        loop=True
    print(history, file=sys.stderr)
   
if loop == True:
    print('LOOP')
else:
    for x in path: print(x)
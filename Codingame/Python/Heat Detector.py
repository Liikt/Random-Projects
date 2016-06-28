import sys
import math

def checkRims(x, y):
    ret=[x,y]
    global w,h
    if x<0:
        ret[0]=0
    if y<0:
        ret[1]=0
    if x>=w:
        ret[0]=w-1
    if y>=h:
        ret[1]=h-1
    return ret

#    U (Up)
#    UR (Up-Right)
#    R (Right)
#    DR (Down-Right)
#    D (Down)
#    DL (Down-Left)
#    L (Left)
#    UL (Up-Left)

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

#Auslagerung der ersten Runde
bomb_dir=input()
xy=[0,0]        #Weite des Sprunges
for c in bomb_dir:
    if c=='D':
        xy[1]=h-y0
    elif c=='U':
        xy[1]=-(y0+1)
    elif c=='R':
        xy[0]=w-x0
    elif c=='L':
        xy[0]=-(x0+1)
print(xy, file=sys.stderr)
for i in range(2):
    if xy[i]>=0:
        xy[i]=math.ceil(xy[i]/2)
    else:
        xy[i]=math.floor(xy[i]/2)
print(xy, file=sys.stderr)
if True:
    x0+=xy[0]
    y0+=xy[1]
    x0,y0=checkRims(x0,y0)
    print(str(x0)+' '+str(y0))


# game loop
while True:
    for i in range(2):
        if xy[i]>=0:
            xy[i]=math.ceil(xy[i]/2)
        else:
            xy[i]=math.floor(xy[i]/2)
    bomb_dir_old=bomb_dir
    bomb_dir=input()
    if len(bomb_dir)==1:
        if bomb_dir[0] in ['L','R']:
            xy[1]=0
        else:
            xy[0]=0
    for c in bomb_dir:
        if c not in bomb_dir_old:
            if c in ['L','R']:
                xy[0]= -(xy[0])
            else:
                xy[1]= -(xy[1])
    x0+=xy[0]
    y0+=xy[1]
    x0,y0=checkRims(x0,y0)
    print(xy, file=sys.stderr)
    print(str(x0)+' '+str(y0))
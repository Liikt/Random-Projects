import sys
import math

w, h = [int(i) for i in input().split()]
array = []
for i in range(h):
    array.append([int(i) for i in input().split()]) 
ex = int(input())


#types -> [y->coordinate,x->coordinate)
types=[]
types.append({'TOP':[0,0],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[1,0],'LEFT':[1,0],'RIGHT':[1,0]})
types.append({'TOP':[0,0],'LEFT':[0,1],'RIGHT':[0,-1]})
types.append({'TOP':[1,0],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[0,-1],'LEFT':[0,0],'RIGHT':[1,0]})
types.append({'TOP':[0,1],'LEFT':[1,0],'RIGHT':[0,0]})
types.append({'TOP':[0,0],'LEFT':[0,1],'RIGHT':[0,-1]})
types.append({'TOP':[1,0],'LEFT':[0,0],'RIGHT':[1,0]})
types.append({'TOP':[0,0],'LEFT':[1,0],'RIGHT':[1,0]})
types.append({'TOP':[1,0],'LEFT':[1,0],'RIGHT':[0,0]})
types.append({'TOP':[0,-1],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[0,1],'LEFT':[0,0],'RIGHT':[0,0]})
types.append({'TOP':[0,0],'LEFT':[0,0],'RIGHT':[1,0]})
types.append({'TOP':[0,0],'LEFT':[1,0],'RIGHT':[0,0]})

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    move=types[array[yi][xi]][pos]

    xi+=move[1]
    yi+=move[0]

    print(str(xi) + ' ' + str(yi))

import sys
import math

n = int(input())
i = input().split()

for it in range(len(i)):
    i[it] = int(i[it])
    
maxi = 0
loss = 0

for x in i:
    print(str(x) + ' ' + str(maxi) + ' ' + str(loss),file=sys.stderr)
    if x > maxi:
        maxi = x
    else:
        if (x - maxi) < loss:
            loss = (x - maxi)
    
print(loss)
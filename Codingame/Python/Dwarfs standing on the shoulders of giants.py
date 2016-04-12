import sys
import math

n = int(input())
main = []
left = []
for i in range(n):
    l = []
    x, y = [int(j) for j in input().split()]
    l.append(x)
    l.append(y)

    left.append(x)
    main.append(l)

def comp(l):
    if len(l) == 1:
        return []
    erg = []
    zwischen = []
    for kante in l:
        for i in range(len(left)):
            if left[i] == kante[1]:
                zwischen.append(kante[0])
                zwischen.append(main[i][1])
                erg.append(zwischen)
                zwischen = []
    return erg
    
lis = main
it = 1

while lis != []:
    lis = comp(lis)
    it += 1
    
print(it)
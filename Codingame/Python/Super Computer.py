import sys
import math

n = int(input())

array = []

for i in range(n):
    j, d = [int(j) for j in input().split()]
    z = []
    z.append(j+d-1)
    z.append(j)
    array.append(z)
    
count = 0

print(array,file=sys.stderr)
array.sort()

def delete(zahl):
    while len(array) > 0 and array[0][1] <= zahl:
        array.pop(0)

while len(array) > 0:
    job = array[0]
    print('Job: '+str(job),file=sys.stderr)
    delete(job[0])
    count += 1
    print('---------------',file=sys.stderr)
    
print(count)
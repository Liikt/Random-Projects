import sys

r = input()
l = int(input())

s=r

def seq(s):
    nextlvl=''
    arr=s.split()
    count=0
    zw=[]
    sent=arr[0]
    for x in arr:
        if x != sent:
            zw.append(str(count))
            zw.append(sent)
            sent = x
            count = 1
        else:
            count+=1
    zw.append(str(count))
    zw.append(sent)

    for x in range(0,len(zw)):
        nextlvl+=zw[x] + ' '
    return nextlvl[:len(nextlvl)-1]

for i in range(l-1):
    s=seq(s)
print(s)
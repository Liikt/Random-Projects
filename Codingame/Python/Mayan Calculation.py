import sys
import math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
numerals=[]     #form: one numeral is numeral[i][0 -> h-1] i=number of the numeral 0-19
rows=[]
output=[]
num=[[],[]]     #SHIT IS GETTING REAL!
 
def checknumber(nn,i):
    for j in range(20):
        if num[nn][i]==numerals[j]:
            return j
            break
 
           
l, h = [int(i) for i in input().split()]
for i in range(h):
    rows.append(input())
    #output.append('')
   
for i in range(20):
    numerals.append([])
    for j in range(h):
        nmline = rows[j][i*l:][:l]
        numerals[i].append(nmline)
numcount=[]
for k in range(2):
    numcount.append(int(int(input())/h))
    for i in range(numcount[k]):
        num[k].append([])
        for j in range(h):
            num[k][i].append(input())
operation=input()
n=[0,0]
for k in range(2):
    for i in range(numcount[k]):
        x=checknumber(k,i)
        x=x*(20**(numcount[k]-i-1))
        print(x, file=sys.stderr)
        n[k]+=x
erg= -1
if operation=='+':
    erg=n[0]+n[1]
elif operation=='-':
    erg=n[0]-n[1]
elif operation=='*':
    erg=n[0]*n[1]
else:
    erg=int(n[0]/n[1])
print(erg, file=sys.stderr)
ergarray=[]
if erg!=0:
    while erg!=0:
        ergarray.append(erg%20)
        erg=int(erg/20)
else:
    ergarray.append(0)
ergarray.reverse()
print(ergarray, file=sys.stderr)
 
for i in range(len(ergarray)):
    for j in range(h):
        print(numerals[ergarray[i]][j])
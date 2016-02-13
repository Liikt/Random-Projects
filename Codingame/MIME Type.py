import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
dic = {} 
ex = []
ty = []
dev = '---------------------------------'

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ex.append(ext.upper())
    ty.append(mt)

zw = zip(ex,ty)
dic = dict(zw)
reg = re.compile('\w{0,256}\.*\.\w{0,10}')
ex = []


for i in range(q):
    fname = input()  # One file name per line.
    print(fname,file=sys.stderr)

    if re.match(reg,fname):
        test = re.findall(reg,fname)
        ex.append(test[len(test)-1].split('.')[len(test[0].split('.'))-1].upper())
    elif re.match(reg,fname):
        ex.append('noooooooooooooope')
    else:
        ex.append('noooooooooooooope')
        
print(dev,file=sys.stderr)
print(dic,file=sys.stderr)
print(ex,file=sys.stderr)
print(dev,file=sys.stderr)

for i in ex:
    if i in dic:
        print(dic[i])
    else:
        print("UNKNOWN")


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.


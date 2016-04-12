import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

row = ''
ans = ''
for i in range(h):
    row += input()
    row += 'ö'
    
rows = row.split('ö')
print(rows,file=sys.stderr)
test = []
for row in rows:
    sent = 0
    char = 1
    for x in row:
        if sent == l-1:
            row = row[:char] + 'ä' + row[char:]
            sent = 0
            char += 2
        else:
            sent += 1
            char += 1
    
    test.append(row.split('ä'))

    
for i in range(h):
    for buchstabe in t:
        if ord(buchstabe) in range(65,91):
            ans += test[i][(ord(buchstabe)-65)]
        elif ord(buchstabe) in range(97,123):
            ans += test[i][(ord(buchstabe)-97)]
        elif sent < 4:
            ans += test[i][26]
        elif sent == 4:
            ans += ' '
    ans += '\n'
    
print(ans)#,file=sys.stderr)

#ASCII offset A-Z -> 64 (+1 aber ich will mit 1 anfangen)
#ASCII offset a-z -> 96 (+1 aber ich will mit 1 anfangen)
#row = 108 charslang

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
print(message,file=sys.stderr)
ans = ''
padd = '00 '

def block1(a):
    if a == '1':
        return '0 '
    else:
        return '00 '

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
message = ''.join(format(ord(x), 'b') for x in message)

it = 0
ite = 0
zw = []

zw = message

l = len(message)

for x in range(l):
    if it == 7:
        it = -1
        zw = zw[:ite] + '#' + zw[ite:]
    it += 1
    ite += 1
    
#print(zw,file=sys.stderr)
zw = zw.split('#')
message = ''

for x in zw:
    while len(x) % 7 != 0:
        x = '0' + x
    message = message + x
print(message,file=sys.stderr)


# for x in arr:
#   zahl = x[0]
#   ans += block1(zahl)
#   for i in range(8):
#       if zahl == i:
#           ans += '0'
#       elif zahl != i:
#           zahl = i
#           ans += ' '
#           ans += block1(zahl)
#           ans += '0'
#   zw.append(ans)

# for x in zw:
#   ans += x
#   ans += ' '


zahl = message[0]

it = 1

ans += block1(zahl)
for i in message:
    if zahl == i:
        ans += '0'
    elif zahl != i:
        zahl = i
        ans += ' '
        ans += block1(zahl)
        ans += '0'

    
print(ans)
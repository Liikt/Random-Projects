import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement

loop = False
path = []
town = []
stack = []
stackT = []
teleport = [[-1, -1],[-1, -1]]
bender = [[], 'SOUTH', 0]
priority = ['SOUTH', 'EAST', 'NORTH', 'WEST']
extra = ['T', 'B', 'X', '#', 'I', 'S', 'E', 'N', 'W']
t = 0
modifier = False
dic1 = {'SOUTH':[0, 1], 'EAST':[1, 0], 'NORTH':[0, -1], 'WEST':[-1, 0]}
dic2 = {'S':'SOUTH', 'E':'EAST', 'N':'NORTH', 'W':'WEST'}
kill = []

l, c = [int(i) for i in input().split()]

def appendBender(bender):
    stack.append([])
    stack[len(stack)-1].append([])
    stack[len(stack)-1][0].append(bender[0][0])
    stack[len(stack)-1][0].append(bender[0][1])
    stack[len(stack)-1].append(bender[1])
    stack[len(stack)-1].append(bender[2])
    
def appendTown(town):
    stackT.append([])
    for i in town:
        stackT[len(stackT)-1].append(i)

for i in range(l):
    row = input()
    town.append(row)
    print(row, file=sys.stderr)
    
    if '@' in row:
        bender[0].append(row.find('@'))        # -> X Position
        bender[0].append(i)                    # -> Y Position
        
    if t == 0 and 'T' in row:
        teleport[0][0] = row.find('T')
        teleport[0][1] = i
        t = 1
        
    if '$' in row:
        kill.append(row.find('$'))
        kill.append(i) 
        
    if t == 1 and 'T' in row[row.find('T') + 1:]:
        teleport[1][0] = row.find('T',teleport[0][0]+1)
        teleport[1][1] = i
    elif t == 1 and 'T' in row and i != teleport[0][1]:
        teleport[1][0] = row.find('T')
        teleport[1][1] = i


while bender[0] != kill:
    #print('kill: ' + str(kill),file=sys.stderr)
    #print('bender[0]: ' + str(bender[0]),file=sys.stderr)
    #print('modifier: ' + str(modifier),file=sys.stderr)
    #print(stack, file=sys.stderr)
    #print(bender, file=sys.stderr)
    #print(stack, file=sys.stderr)
    #print(stackT, file=sys.stderr)
    
    if town[bender[0][1]][bender[0][0]] not in extra or modifier == True:
        
        #print('Lauf/Break/Drehen', file=sys.stderr)
        direc = dic1[bender[1]]
        if town[bender[0][1] + direc[1]][bender[0][0] + direc[0]] == 'X' and bender[2] == 1:
            appendBender(bender)
            appendTown(town)
            for x in [0, 1]: bender[0][x] += direc[x]
            #print('Break', file=sys.stderr)
            path.append(bender[1])
            
            town[bender[0][1]] = town[bender[0][1]][:bender[0][0]] + ' ' + town[bender[0][1]][bender[0][0]+1:]
            
            if bender in stack and stack.count(bender) > 2 and stackT[stack.index(bender)] == town:
                print(bender, file=sys.stderr)
                print(stack[stack.index(bender)+1], file=sys.stderr)
                print(stack[stack.index(bender)+2], file=sys.stderr)
                print(stack[stack.index(bender)+3], file=sys.stderr)
                print(stack[stack.index(bender)+4], file=sys.stderr)
                print('teleport: ' + str(teleport), file=sys.stderr)
                stackT.pop(stack.index(bender))
                stack.remove(bender)
                if bender in stack and stackT[stack.index(bender)] == town:
                    loop = True
                    break
            
            #print(town[bender[0][1]],file=sys.stderr)
        elif town[bender[0][1] + direc[1]][bender[0][0] + direc[0]] not in ['#', 'X']:
            appendBender(bender)
            appendTown(town)
            for x in [0, 1]: bender[0][x] += direc[x]
            modifier = False
            #print('Lauf ' + bender[1], file=sys.stderr)
            path.append(bender[1])
            
            if bender in stack and stack.count(bender) > 2 and stackT[stack.index(bender)] == town:
                print(bender, file=sys.stderr)
                print(stack[stack.index(bender)+1], file=sys.stderr)
                print(stack[stack.index(bender)+2], file=sys.stderr)
                print(stack[stack.index(bender)+3], file=sys.stderr)
                print(stack[stack.index(bender)+4], file=sys.stderr)
                print('teleport: ' + str(teleport), file=sys.stderr)
                stackT.pop(stack.index(bender))
                stack.remove(bender)
                if bender in stack and stackT[stack.index(bender)] == town:
                    loop = True
                    break
        else:
            bender[1] = priority[0]
            direc = dic1[bender[1]]
            #print('Dreh', file=sys.stderr)
            while town[bender[0][1] + direc[1]][bender[0][0] + direc[0]] in ['#', 'X']:
                bender[1] = priority[(priority.index(bender[1]) + 1) % 4]
                direc = dic1[bender[1]]
                #print(5, file=sys.stderr)
        
    elif town[bender[0][1]][bender[0][0]] in ['N', 'S', 'W', 'E'] and modifier == False:
        bender[1] = dic2[town[bender[0][1]][bender[0][0]]]
        modifier = True
        #print('Richtung ' + bender[1], file=sys.stderr)
    elif town[bender[0][1]][bender[0][0]] == 'B' and modifier == False:
        bender[2] = (bender[2]+1)%2
        modifier = True
        #print('Beer', file=sys.stderr)
    elif town[bender[0][1]][bender[0][0]] == 'I' and modifier == False:
        priority.reverse()
        modifier = True
        #print('Invertieren', file=sys.stderr)
    elif town[bender[0][1]][bender[0][0]] == 'T' and modifier == False:
        #print(9, file=sys.stderr)
        if bender[0] == teleport[0]:
            bender[0] = teleport[1]
            #print('Teleport 1 -> 2', file=sys.stderr)
        elif bender[0] == teleport[1]:
            bender[0] = teleport[0]
            #print('Teleport 2 -> 1', file=sys.stderr)
        modifier = True
    
    
    #print('---------------------',file=sys.stderr)
    #print('#' + town[bender[0][1]][bender[0][0]] + '#', file=sys.stderr)
    
if loop == True:
    print('LOOP')
else:
    for x in path: print(x)
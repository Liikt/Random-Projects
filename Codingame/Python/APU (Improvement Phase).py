import sys
import math
import copy
 
# The machines are gaining ground. Time to show them what we're really made of...
# nodes = [hash, right, left, lower, upper, #neighbors, [#linksPerNeighbor]]
changeSides={1:2,2:1,3:4,4:3}
nodes=[]
nodesonly=[]
links = []
valid = []
conflicts=[[link, conflict-hash1,...]]


#hash = xyc (x = x coordinate, y = y coordinate, c = count)
def hashCoord(x, y, c):
    return str(chr(x+48)+chr(y+48)+str(c))
 
def retrieve(h):
    return [ord(h[0])-48,ord(h[1])-48,int(h[2])]
 
def set_MLinks(j,m):
    n=[[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    n[0][0], n[1][0], useless = retrieve(nodes[j][0])
    for i in range(1,5):
        if nodes[j][i]!=-1:
            print(str(nodes[j][i])+' '+str(j),file=sys.stderr)
            n[0][i], n[1][i], useless = retrieve(nodes[nodes[j][i]][0])
            otherNode=nodes[j][i]
            link = str(n[0][0])+' '+str(n[1][0])+' '+str(n[0][i])+' '+str(n[1][i])+' 1'
            linkBack = str(n[0][i])+' '+str(n[1][i])+' '+str(n[0][0])+' '+str(n[1][0])+' 1'
            linkcount=links.count(link)+links.count(linkBack)
            if nodes[nodes[j][i]][0][2] == '1':
                linkcount+=1
            for k in range(m-linkcount):
                links.append(link)
                nodes[j][6][i-1]+=1
                nodes[otherNode][6][changeSides[i]-1]+=1    
            if sum(nodes[j][6]) == int(nodes[j][0][2]) and j not in valid:
                valid.append(j)
            if sum(nodes[otherNode][6]) == int(nodes[otherNode][0][2]) and otherNode not in valid:
                valid.append(otherNode)
 
def preProcess():
    for j in range(len(nodes)):
        if nodes[j][5]*2 == int(nodes[j][0][2]):
            set_MLinks(j,2)
        elif nodes[j][5]*2-1== int(nodes[j][0][2]):
            set_MLinks(j,1)

def newIndices():
    print(nodesonly,file=sys.stderr)
    for node in nodes:
        for i in range(1,5):
            if node[i] != -1:
                node[i]=nodesonly.index(backup[node[i]][0])

def pruning():
    for v in valid:
        temp = nodes[v]
        for n in range(1,5):
            if temp[n] > 0:
                zw = temp[n]
                if temp[n] not in valid:
                    number = int(nodes[zw][0][2]) - int(temp[6][n-1])
                    nodes[zw][0] = nodes[zw][0][:2] + str(number)
                nodes[zw][6][changeSides[n]-1] = 0.0
                if temp[0][2]=='1':
                    nodes[zw][5]-=0.5
                else:
                    nodes[zw][5]-=1
                #print(temp[0] + ' ' + nodes[zw][0] + ' ' + str(nodes[zw][5]),file=sys.stderr)
        #for x in range(4):
            if len(str(temp[6][n-1]))<2:
                derp = temp[n]
                nodes[derp][changeSides[n]] = -1

    valid.sort(reverse=True)
    for v in valid:
        nodes.pop(v)
        nodesonly.pop(v)
    valid.clear()
    newIndices()

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
line = []
for i in range(height):
    line.append(input())  # width characters, each either a number or a '.'
 
zw=-1
# Two coordinates and one integer: a node, one of its neighbors, the number of links connecting them.
for i in range(height):
    x=len(nodes)-1
    for j in range(width):
        if line[i][j]!='.':
            node=hashCoord(j,i,int(line[i][j]))
            nodesonly.append(node)
            nodes.append([node, -1, -1, -1, -1, 0, [0.0,0.0,0.0,0.0]])            
            if zw != x:
                nodes[zw+1][5]=1
                nodes[zw+1][2]=zw                               #set left neighbor
                nodes[zw][1]=zw+1                               #set right neighbor
                nodes[zw][6][0]=0
                nodes[zw+1][6][1]=0
                nodes[zw][5]+=1
                if node[2] == '1':
                    nodes[zw][5] -= 0.5
                if nodes[zw][0][2]=='1':
                    nodes[zw+1][5]-=0.5
            zw +=1
 
for j in range(width):
    indexOld=-1
    for i in range(height):
        if line[i][j]!='.':
            index = nodesonly.index(hashCoord(j,i,int(line[i][j])))
            if indexOld>-1:            
                nodes[index][4]=indexOld
                nodes[index][6][3] = 0
                nodes[index][5]+=1
                if nodes[indexOld][0][2]=='1':
                    nodes[index][5]-=0.5
                nodes[indexOld][3]=index
                nodes[indexOld][6][2] = 0
                nodes[indexOld][5]+=1
                if nodes[index][0][2]=='1':
                    nodes[indexOld][5]-=0.5
            indexOld=index

backup = copy.deepcopy(nodes)

while len(nodes) > 0:
    preProcess()
    pruning()

for link in links:
    print(link)
 

import sys
import math
 
links=[]
nodes=[]        #nodes=[node1,node2...] # node = [hash, right, left, lower, upper, isolationstatus]
nodesonly=[]    #only hashes to find the index when given the coordinates
links = []      #links=[link1,link2,..] # link = [node1index,node2index,linknumber,list of crossing links]
linksonly=[]
 
def hashCoord(x, y, c):
    return str(chr(x+48)+chr(y+48)+str(c))
 
def retrieve(h):
    return [ord(h[0])-48,ord(h[1])-48,int(h[2])]
 
def setLink(a,b,numLinks,prinnt):
    global horizontalLinks
    if b<a:
        a,b = b,a
 
    ax, ay, useless = retrieve(nodes[a])
    bx, by, useless = retrieve(nodes[b])
    link = ' '.join([str(ax), str(ay), str(bx), str(by), str(numLinks)])
    nodes[a][0][2]-=1
    nodes[b][0][2]-=1
    linkIndex=linksonly.index(str(a)+str(b))
    horizontal=1     #FÜR CROSSING LINKS
    if linkIndex<=horizontalLinks:
        horizontal=0
    if not links[linkIndex][2]:         #(==0)
        for crossing in links[linkIndex][3]:
            nodes[links[crossing][0]][2*horizontal+1] = -1
            nodes[links[crossing][1]][2*horizontal+2] = -1
    links[linkIndex][2]+=numLinks
    #isolation
    if nodes[a][5]:
        if nodes[a][0][2]!=0:
            

    if prinnt:
        print(link)
    return link

 
def setOL(index):       #set obvious links
    neival=0            #neighbor value
    are1=[0,0,0,0]
    for i in range(1,5):
        nei=nodes[index][i]     #neighbor (INDEX!!)
        if nei != -1:
            if nodes[nei][0][2] == 1:
                neival+=0.5
                are1[i-1]=1
            else:
                neival+=1
    numLinks=0
    if neival*2==nodes[index][0][2]:
        numLinks=2
    elif (neival*2)-1==nodes[index][0][2]:
        numLinks=1
    if numLinks>0:
        for i in range(1,5):
            nei=nodes[index][i]
            if are1[i-1]==0:
                setLink(index,nei,numLinks,1)
 
def setIL(index):       #set isolation links
    pass
 
def processNode(index):
    lset=setOL(index)
    lset= lset or setIL(index)
    return lset
  
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
            nodes.append([node, -1, -1, -1, -1, True])            
            if zw != x:
                nodes[zw+1][2]=zw                               #set left neighbor
                nodes[zw][1]=zw+1                             #set right neighbor
                links.append([zw,zw+1,0,[]])
                linksonly.append(str(zw)+str(zw+1))
            zw +=1
 
horizontalLinks=len(links)
 
for j in range(width):
    indexOld=-1
    for i in range(height):
        if line[i][j]!='.':
            index = nodesonly.index(hashCoord(j,i,int(line[i][j])))
            if indexOld>-1:            
                nodes[index][4]=indexOld
                nodes[indexOld][3]=index
                links.append([indexOld,index,0,[]])
                linksonly.append(str(indexOld)+str(index))
                lastl=len(links)
                for i in range(0,horizontalLinks):
                    l1x1, l1y1, useless = retrieve(nodes[links[i][0]][0])
                    l1x2, l1y2, useless = retrieve(nodes[links[i][1]][0])
                    l2x1, l2y1, useless = retrieve(nodes[links[lastl][0]][0])
                    l2x2, l2y2, useless = retrieve(nodes[links[lastl][1]][0])
                    if l1x1<l2x1<l1x2 and l2y1<l1y1<l2y2:
                        links[i][3].append(lastl)
                        links[lastl][3].append(i)
            indexOld=index
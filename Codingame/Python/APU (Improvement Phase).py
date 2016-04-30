import sys
import math
 
 
linksonly=[]
nodes=[]        #nodes=[node1,node2...] # node = [hash, right, left, lower, upper, isolationstatus]
nodesonly=[]    #only hashes to find the index when given the coordinates
links = []      #links=[link1,link2,..] # link = [node1index,node2index,linknumber,list of crossing links]
 
def hashCoord(x, y, c):
    return str(chr(x+48)+chr(y+48)+str(c))
 
def retrieve(h):
    return [ord(h[0])-48,ord(h[1])-48,int(h[2])]
 
def setLink(a,b,numLinks,prinnt):
    if numLinks==0:
        return 0
    global horizontalLinks
    if b<a:
        a,b = b,a
    ax, ay, useless = retrieve(nodes[a][0])
    bx, by, useless = retrieve(nodes[b][0])
    link = ' '.join([str(ax), str(ay), str(bx), str(by), str(numLinks)])
    nodes[a][0]=nodes[a][0][:2]+str(int(nodes[a][0][2])-numLinks)
    nodes[b][0]=nodes[b][0][:2]+str(int(nodes[b][0][2])-numLinks)
    linkIndex=linksonly.index(str(a)+str(b))
    vertical=0     #FÜR CROSSING LINKS
    if linkIndex<horizontalLinks:
        vertical=1
    if not links[linkIndex][2]:         #(==0)
        for crossing in links[linkIndex][3]:
            nodes[links[crossing][0]][2*vertical+1] = -1
            nodes[links[crossing][1]][2*vertical+2] = -1
    links[linkIndex][2]+=numLinks
    #isolation
    #if nodes[a][5]:
    #    if nodes[a][0][2]!=0:
           
    for i in a,b:
        if not int(nodes[i][0][2]):
            #print("delete",i,nodes[i][0], file=sys.stderr)
            for j in range(1,5):
                if nodes[i][j]!=-1:
                    nodes[nodes[i][j]][nodes[nodes[i][j]][1:5].index(i)+1] = -1
                    nodes[i][j]=-1
 
    if prinnt:
        print(link)
        #print(link, file=sys.stderr)
    return link
 
 
def setOL(index):       #set obvious links
    neival=0            #neighbor value
    are1=[0,0,0,0]
    for i in range(1,5):
        nei=nodes[index][i]     #neighbor (INDEX!!)
        if nei!= -1:
            if int(nodes[nei][0][2])==1 and nodes[nei][5]==1:
                neival+=0.5
                are1[i-1]=1
            else:
                neival+=1
    numLinks=0
    if neival*2 == int(nodes[index][0][2]):
        numLinks=2
    elif (neival*2)-1 == int(nodes[index][0][2]):
        numLinks=1
    #print("index:",index, "numLinks:",numLinks, "are1:", are1, file=sys.stderr)
    if numLinks>0:
        for i in range(1,5):
            nei=nodes[index][i]
            if nei!=-1:
                if are1[i-1]==1:
                    setLink(index,nei,numLinks-1,1)
                else:
                    setLink(index,nei,numLinks,1)
        return True
    return False
 
 
 
 
 
def setIL(index):       #set isolation links
    pass
 
 
def processNode(index):
    lset=False
    if int(nodes[index][0][2]):
        lset=setOL(index)
        #lset= lset or setIL(index)
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
                for i in range(0,horizontalLinks):
                    l1x1, l1y1, useless = retrieve(nodes[links[i][0]][0])
                    l1x2, l1y2, useless = retrieve(nodes[links[i][1]][0])
                    l2x1, l2y1, useless = retrieve(nodes[links[-1][0]][0])
                    l2x2, l2y2, useless = retrieve(nodes[links[-1][1]][0])
                    if l1x1<l2x1<l1x2 and l2y1<l1y1<l2y2:
                        links[i][3].append(len(links)-1)
                        links[-1][3].append(i)
            indexOld=index
 
print("nodes initialized:",str(nodes), file=sys.stderr)
print("links:",links,file=sys.stderr)
 
action=True
while action:
    acts=0
    for i in range(len(nodes)):
        act_now=processNode(i)
        if act_now:
            pass    #FOR DEBUG!
            #print(" nodes",str(nodes), file=sys.stderr)
            #print("links:",links,file=sys.stderr)
        acts+=int(act_now)
    print("actions:",acts, file=sys.stderr)
    action=bool(acts)
    print("-----------------------------------------------", file=sys.stderr)
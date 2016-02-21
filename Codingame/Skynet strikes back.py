# DISCLAIMER:
# The Testcase Complex Mesh only works ine the Submit NOT in the actual test
# It probably has to do with inconsistencies between the test and submit cases 
# The thing causing the discrapencies is probably in line 95 the '<'
# If you want to solve all testcases use '<='. If you want to submit use '<' 

adj = []
gateways = []
erg = []
critical = []

def testGateways(node):
    gates = 0
    for gate in gateways:
        if gate in adj[node]:
            gates += 1
    return gates
      

def delCrit(index):
    if index in critical:
        critical.remove(index)
 
def delZelda(n1, n2):  
    adj[n1].remove(n2)
    adj[n2].remove(n1)
 
def addAdj(n1, n2):
    adj[n1].append(n2)
    adj[n2].append(n1)
 
def calcAbstand(start):
    abstand = 1
 
    visited.append(start)
    temp = start
    erg[start] = 0
 
    for node in visited:
        foundGateway=False
        for x in adj[node]:
            if x not in visited:
                visited.append(x)
                erg[x] = abstand
                if testGateways(x)>0:
                    foundGateway=True
 
        if node == temp:
            if foundGateway==True:
                for i in range(len(visited)-1,visited.index(temp),-1):
                    if testGateways(visited[i])==0:
                        visited.pop(i)

            abstand += 1
            temp = visited[len(visited)-1]
 
n, l, e = [int(i) for i in input().split()]
 
for x in range(n):
    adj.append([])
 
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    addAdj(n1, n2)
 
for i in range(e):
    gateways.append(int(input()))  # the index of a gateways node
 
# find all nodes with more than 1 adjacent gateways
for i in range(len(adj)):
    gates=testGateways(i)
    if gates > 1:
        critical.append(i) 

# game loop
while True:
    visited = []
    for x in range(n):
        erg.append(n+1)
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    a=testGateways(si)
    if a>0:
        for gate in gateways:
            if gate in adj[si]:
                print(str(gate)+' '+str(si))
                delZelda(gate,si)
                break
    elif len(critical) > 0:
        calcAbstand(si)
        mini=n+2
        critest = -1
        for crit in critical:
            if erg[crit]<mini:
                mini=erg[crit]
                critest=crit

        for x in adj[critest]:
            if x in gateways:
                print(str(x)+' '+str(critest))
                delZelda(x,critest)
                delCrit(critest)
                break
    else:
        for g in gateways:
            if len(adj[g]) > 0:
                print(str(g)+' '+str(adj[g][len(adj[g])-1]))
                delZelda(g,adj[g][len(adj[g])-1])
                break


    erg.clear()

# Testcase X
# LOCKED
# 20
# 100 300
# 200 280
# 300 260
# 400 240
# 500 220
# 700 160
# 700 250
# 200 400
# 300 400
# 400 400
# 500 400
# 100 500
# 200 500
# 300 500
# 400 500
# 500 500
# 300 550
# 600 500
# 700 450
# 700 550
# 24
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 4 6
# 0 7
# 7 8
# 8 9
# 9 10
# 7 11
# 11 12
# 12 13
# 13 14
# 14 15
# 15 16
# 15 17
# 17 18
# 17 19
# 11 16
# 12 16
# 13 16
# 14 16
# 15 16
# 0
# 7
# 5
# 6
# 8
# 10
# 16
# 18
# 19
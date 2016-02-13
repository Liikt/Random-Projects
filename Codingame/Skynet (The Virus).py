import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
visited = []
erg = []
abstand = 1
adj = []
gateways = []

def delZelda(n1, n2):  
    adj[n1].remove(n2)
    adj[n2].remove(n1)

def addAdj(n1, n2):
    adj[n1].append(n2)
    adj[n2].append(n1)

def calcAbstand(start):
    global abstand

    visited.append(start)
    temp = start
    erg[start] = 0

    for node in visited:
        for x in adj[node]:
            if x not in visited:
                visited.append(x)
                erg[x] = abstand

        if node == temp:
            abstand += 1
            temp = visited[len(visited)-1]

def calcAction():
    global n
    mini = n + 1
    g = -1
    current = -1

    for gateway in gateways:
        for node in adj[gateway]:
            if erg[node] < mini:
                mini = erg[node]
                g = gateway
                current = node

    delZelda(g, current)
    print(str(g) + ' ' + str(current))

n, l, e = [int(i) for i in input().split()]

for x in range(n):
    erg.append(-1)
    adj.append([])

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    addAdj(n1, n2)

for i in range(e):
    gateways.append(int(input()))  # the index of a gateways node

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    calcAbstand(si)
    calcAction()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
#   print("0 1")

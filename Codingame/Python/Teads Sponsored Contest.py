import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

nodes = []
exist = []

def printNodes():
    for n in nodes:
        print('Number: ' + str(n.getNumber()) + ' Links to: [' + n.printDebug() + ']',file=sys.stderr)
    print('-------------------',file=sys.stderr)

class node(object):
    def __init__(self, number):
        self.number = number
        self.links = []

    def getNumber(self):
        return self.number

    def getLinks(self):
        return self.links

    def printDebug(self):
        r = ''
        for x in self.links:
            r += str(x.getNumber()) + ', '
        return r[:len(r)-2]

    def addLink(self, node):
        self.links.append(node)
        

n = int(input())  # the number of adjacency relations
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    x = node(xi)
    y = node(yi)

    # if xi not in exist:
    #     nodes.append(x)
    #     exist.append(xi)
    # else:
    #     x = nodes[exist.index(xi)]

    # if yi not in exist:
    #     nodes.append(y)
    #     exist.append(yi)
    # else:
    #     y = nodes[exist.index(yi)]

    # x.addLink(y)
    # y.addLink(x)
    

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# The minimal amount of steps required to completely propagate the advertisement
#printNodes()

class Node(object):
    def __init__(self, number='-1'):
        self.number = number
        self.children = []

    def getNumber(self):
        return self.number

    def getChildren(self):
        return self.children 

    def insertChildren(self,node):
        self.children.append(node)


class tree(object):
    def __init__(self, root=[], count=0):
        self.root = Node()
        self.count = count

    def getCount(self):
        return self.count

    def insert_node(self, number):
        number = str(number)
        temp = self.root
        numChildren = []     
        for x in self.root.getChildren():
            numChildren.append(x.getNumber())

        if number[0] not in numChildren:
            newEl = Node(number[0])
            self.root.insertChildren(newEl)
            self.count+=1
            temp = newEl
            number=number[1:]
            
        for zif in number:
            numChildren = []     
            for x in temp.getChildren():
                numChildren.append(x.getNumber())
            if zif in numChildren:
                temp=temp.getChildren()[numChildren.index(zif)]
            else: 
                temp.insertChildren(Node(zif))
                self.count+=1
                temp = temp.getChildren()[len(temp.getChildren())-1]

n = int(input())
baum = tree()
for i in range(n):
    baum.insert_node(input())

print(baum.getCount())

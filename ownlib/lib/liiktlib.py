import os

def filemerge(file1, file2, file3):
    if not os.path.isfile(file1) or not os.path.isfile(file2) or not os.path.isfile(file3):
        print("[Error] One of these files doesn't exist!")
        return

    with open(file1) as f:
        list1 = f.read().split("\n")

    with open(file2) as f:
        list2 = f.read().split("\n")
    
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x]+':'+list2[x])

    f = open(file3,"w")
    for x in list3:
        f.write(x+"\n")
    f.close()
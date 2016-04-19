import random
import Utils


def RandomSort(arr, s):
    instructions = 0
    while True:
        instructions += 1
        rand = random.randint(0,1)
        instructions += 1
        if rand == 1:
            instructions += 1
            check, instructions = Utils.checkIfSorted(arr, s, instructions)
            if check == True:
                instructions += 1
                return arr, instructions
        instructions += 1
        rand = random.randint(0,1)
        instructions += 1
        if rand == 1:
            instructions += 1
            rand2 = random.randint(0,(len(arr)-1))
            instructions += 1
            rand3 = random.randint(0,(len(arr)-1))
            instructions += 1
            arr, instructions = Utils.swap(arr, rand2, rand3, instructions)

def Bubble(arr, s):
    instructions = 0

    instructions += 1
    for x in range(0,len(arr)-1):
        instructions += 1
        for i in range(0,len(arr)-2):
            instructions += 1
            if s == 0:
                instructions += 1
                if arr[i] > arr[i+1]:
                    instructions += 1
                    arr, instructions = Utils.swap(arr, i, i+1, instructions)
            else:
                instructions += 1
                if arr[i] < arr[i+1]:
                    instructions += 1
                    arr, instructions = Utils.swap(arr, i, i+1, instructions)
        instructions += 1
    instructions += 1
    return arr, instructions

if __name__ == '__main__':
    pass
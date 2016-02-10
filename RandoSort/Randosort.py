import time
import random
import os
import platform
import re

def compare(arr):
    global instructions

    bub = arr
    ran = arr

    instructions = 0
    Bubble(bub)
    print('For a list with ' + str(len(arr)) + ' entries, Bubblesort takes ' + str(instructions) + ' instructions.')
    temp = instructions
    instructions = 0
    RandomSort(ran)
    print('For a list with ' + str(len(arr)) + ' entries, Randomsort takes ' + str(instructions) + ' instructions.')
    temp = input('Press return to continue')
    clear()


def printList(arr):
    temp = ''

    for x in arr:
        temp += str(x) + ', '

    temp = temp[:len(temp)-2]

    print('\nYour current List = ' + temp)
    temp = input('Press return to continue')
    clear()

def shuffleList(arr):
    if len(arr) != 0:
        while True:
            print('\nPlease enter how often you want to shuffle or \'B\' to get back!')
            inp = input('-> ')
            try:
                inp = int(inp)
                break
            except:
                if inp.lower() == 'b':
                    break
                print('That wasn\'t a number!') 
                temp = input('Press return to continue')
        for x in range(inp):        
            random.shuffle(arr)
        clear()
    else:
        print('List is empty.')
        temp = input('Press return to continue')
        clear()

def fillRandom(arr):
    sent = 0

    while True:
        print('\nPlease enter how many numbers or \'B\' to get back!')
        many = input('-> ')
        print('\nPlease enter the lower boundary of the range or \'B\' to get back!')
        low = input('-> ')
        print('\nPlease enter the upper boundary of the range or \'B\' to get back!')
        high = input('-> ')

        try:
            many = int(many)
            sent += 1
        except:
            if many.lower() == 'b':
                arr = []
                return
            print('That wasn\'t a number!')
            temp = input('Press return to continue')
        try:
            low = int(low)
            sent += 1
        except:
            if low.lower() == 'b':
                arr = []
                return
            print('That wasn\'t a number!')
            temp = input('Press return to continue')
        try:
            high = int(high)
            sent += 1
        except:
            if high.lower() == 'b':
                arr = []
                return
            print('That wasn\'t a number!')
            temp = input('Press return to continue')

        if sent == 3:
            break

    for x in range(many):        
        arr.append(random.randint(low, high))

    clear()
    return arr

def handleInput(inp, arr):

    clear()
    if inp.lower() == 'q':
        return 1
    elif inp.lower() == 's':
        shuffleList(arr)
        return 0
    elif inp.lower() == 'a':
        arr = RandomSort(arr)
        return 0
    elif inp.lower() == 'p':
        printList(arr)
        return 0
    elif inp.lower() == 'f':
        arr = fillRandom(arr)
        return 0 
    elif inp.lower() == 'c':
        compare(arr)

def clear():
    pl = platform.system()
    if pl == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def swap(arr, a, b):
    global instructions

    instructions += 1
    temp = arr[a]
    instructions += 1
    arr[a] = arr[b]
    instructions += 1
    arr[b] = temp

def checkIfSorted(arr):
    global instructions

    instructions += 1
    temp = arr
    instructions += 1
    for i in range(0,len(arr)-1):
        instructions += 1
        if arr[i] > arr[i+1]:
            instructions += 1
            return False
    return True

def RandomSort(arr):
    global instructions

    while True:
        instructions += 1
        rand = random.randint(0,1)
        instructions += 1
        if rand == 1:
            instructions += 1
            if checkIfSorted(arr) == True:
                instructions += 1
                return arr
        instructions += 1
        rand = random.randint(0,1)
        instructions += 1
        if rand == 1:
            instructions += 1
            rand2 = random.randint(0,(len(arr)-1))
            instructions += 1
            rand3 = random.randint(0,(len(arr)-1))
            instructions += 1
            swap(arr, rand2, rand3)
    clear()

def Bubble(arr):
    global instructions

    instructions += 1
    for x in range(0,len(arr)-1):
        instructions += 1
        for i in range(0,len(arr)-2):
            instructions += 1
            if arr[i] > arr[i+1]:
                instructions += 1
                swap(arr, i, i+1)
        instructions += 1
    instructions += 1
    clear()
        
def main():
    clear()
    array= []
    print('\n***********************************************************')
    print('*            Welcome to the Randomsort machine            *')
    print('***********************************************************')
    
    while True:
        print('**************************************************')
        print('*                A: Sort the List                *')
        print('*        C: Compare Bubble and Randomsort        *')
        print('*                F: Fill randomly                *')
        print('*          S: Shuffle the current list           *')
        print('*           P: Print the current list            *')
        print('*               D: Delete a Number               *')
        print('*               R: Remove the list               *')
        print('*     Any Number: Add the number to the list     *')
        print('*                    Q: Quit                     *')
        print('**************************************************')
        print('\nPlease enter your input!')
        inp = input('-> ')
        if handleInput(inp, array) == 1:
            break

if __name__ == '__main__':
    instructions = 0
    main()


#Funktionen 1. Array random füllen, 2. Array selbst füllen, 3. shuffle, 4. ausgabe
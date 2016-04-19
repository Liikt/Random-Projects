import time
import random
import platform
import os
import Sorts

sent = 0

def clear():
    pl = platform.system()
    if pl == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def swap(arr, a, b, instructions):
    instructions += 1
    temp = arr[a]
    instructions += 1
    arr[a] = arr[b]
    instructions += 1
    arr[b] = temp
    return arr, instructions

def checkIfSorted(arr, s, instructions):
    instructions += 1
    temp = arr
    instructions += 1
    for i in range(0,len(arr)-1):
        instructions += 1
        if s == 0:
            instructions += 1
            if arr[i] > arr[i+1]:
                instructions += 1
                return False, instructions
        else:
            instructions += 1
            if arr[i] < arr[i+1]:
                instructions += 1
                return False, instructions
    return True, instructions

def fillRandom(arr):
    sent = 0

    while True:
        print('\n Please enter how many numbers or \'B\' to get back!')
        many = input('-> ')
        if many.lower() == 'b':
                arr = []
                clear()
                return arr
        print('\n Please enter the lower boundary of the range or \'B\' to get back!')
        low = input('-> ')
        if low.lower() == 'b':
                arr = []
                clear()
                return arr
        print('\n Please enter the upper boundary of the range or \'B\' to get back!')
        high = input('-> ')
        if high.lower() == 'b':
                arr = []
                clear()
                return arr
      
        try:
            many = int(many)
            if many < 0:
                print('\n The amount has to be greater than 0!')
                temp = input(' Press return to continue')
                clear()
            else:
                sent += 1
        except:
            print('\n The amount wasn\'t a number!')
            temp = input(' Press return to continue')
            clear()

        try:
            low = int(low)
            sent += 1
        except:
            print('\n The lower boundary wasn\'t a number!')
            temp = input(' Press return to continue')
            clear()

        try:
            high = int(high)
            sent += 1
        except:
            print('\n The upper boundary wasn\'t a number!')
            temp = input(' Press return to continue')
            clear()

        if low > high:
            print('\n The lower boundary can\'t be a greater number than the upper boundary!')
            temp = input(' Press return to continue')
            clear()
        elif sent == 3:
            break

    for x in range(many):
        arr.append(random.randint(low, high))

    clear()
    return arr

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
                    clear()
                    break
                print(' That wasn\'t a number!') 
                temp = input(' Press return to continue')
        for x in range(inp):        
            random.shuffle(arr)
        clear()
        return arr
    else:
        print(' List is empty.')
        temp = input(' Press return to continue')
        clear()
        return arr


def printList(arr):
    temp = ''

    for x in arr:
        temp += str(x) + ', '

    temp = temp[:len(temp)-2]

    print('\n Your current List = ' + temp)
    temp = input(' Press return to continue')
    clear()

def compare(arr, s):
    instructions = 0
    bub = arr
    ran = arr

    instructions = Sorts.Bubble(bub, s)
    print('\n For a list with ' + str(len(arr)) + ' entries, Bubblesort takes ' + str(instructions) + ' instructions.')
    temp = instructions
    instructions = Sorts.RandomSort(ran, s)
    print(' For a list with ' + str(len(arr)) + ' entries, Randomsort takes ' + str(instructions) + ' instructions.')
    temp = input(' Press return to continue')
    clear()

def delete(arr):
    if len(arr) != 0:
        while True:
            print('\n Please enter what number you want to delete or \'B\' to get back!')
            inp = input(' -> ')
            try:
                inp = int(inp)
                break
            except:
                if inp.lower() == 'b':
                    clear()
                    break
                print(' That wasn\'t a number!') 
        if arr.count(inp) != 0:
            print('\n An instances of ' + str(inp) + ' got deleted!')
            temp = input(' Press return to continue')
            clear()
            arr.remove(inp)
            return arr
        else:
            print('\n The list doesn\'t contain ' + str(inp) + '!')
            temp = input(' Press return to continue')
            clear()
            return arr
    else:
        print(' List is empty.')
        temp = input(' Press return to continue')
        clear()

def rem(arr):
    return []

def shutdown():
    p = 'Shutting Down '
    for x in range(4):
        clear()
        print(p)
        p+='.'
        time.sleep(0.5)

def toggle(sent):
    sent = abs(sent - 1)
    return sent

def printCurrAscent(sent):

    if sent == 0:
        return '<'
    elif sent == 1:
        return '>'
    else:
        return 'Error ' + str(sent)

if __name__ == '__main__':
    pass
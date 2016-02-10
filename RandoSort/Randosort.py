import time
import random
import os
import platform

def toggle():
    global sent

    sent = abs(sent - 1)

def printCurrAscent():
    global sent

    if sent == 0:
        return '<'
    elif sent == 1:
        return '>'
    else:
        return 'Error ' + str(sent)

def rem(arr):
    while len(arr) != 0:
        for x in arr:
            arr.remove(x)
    return arr

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
            return arr.remove(inp)
        else:
            print('\n The list doesn\'t contain ' + str(inp) + '!')
            temp = input(' Press return to continue')
            clear()
            return arr
    else:
        print(' List is empty.')
        temp = input(' Press return to continue')
        clear()

def compare(arr, s):
    global instructions

    bub = arr
    ran = arr

    instructions = 0
    Bubble(bub, s)
    print('\n For a list with ' + str(len(arr)) + ' entries, Bubblesort takes ' + str(instructions) + ' instructions.')
    temp = instructions
    instructions = 0
    RandomSort(ran, s)
    print(' For a list with ' + str(len(arr)) + ' entries, Randomsort takes ' + str(instructions) + ' instructions.')
    temp = input(' Press return to continue')
    clear()


def printList(arr):
    temp = ''

    for x in arr:
        temp += str(x) + ', '

    temp = temp[:len(temp)-2]

    print('\n Your current List = ' + temp)
    temp = input(' Press return to continue')
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
                    clear()
                    break
                print(' That wasn\'t a number!') 
                temp = input(' Press return to continue')
        for x in range(inp):        
            random.shuffle(arr)
        clear()
    else:
        print(' List is empty.')
        temp = input(' Press return to continue')
        clear()

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

def handleInput(inp, arr, s):

    clear()
    if inp.lower() == 'q':
        return 1
    elif inp.lower() == 's':
        shuffleList(arr)
        return 0
    elif inp.lower() == 'a':
        arr = RandomSort(arr, s)
        return 0
    elif inp.lower() == 'p':
        printList(arr)
        return 0
    elif inp.lower() == 'f':
        arr = rem(arr)
        arr = fillRandom(arr)
        return 0 
    elif inp.lower() == 'c':
        compare(arr, s)
        return 0
    elif inp.lower() == 'd':
        arr = delete(arr)
        return 0
    elif inp.lower() == 'r':
        arr = rem(arr)
        return 0
    elif inp.lower() == 't':
        toggle()
        return 0
    else:
        try:
            inp = int(inp)
            arr.append(inp)
        except:
            print('\n That was a wrong input!') 
            temp = input(' Press return to continue')
            clear()

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

def checkIfSorted(arr, s):
    global instructions

    instructions += 1
    temp = arr
    instructions += 1
    for i in range(0,len(arr)-1):
        instructions += 1
        if s == 0:
            instructions += 1
            if arr[i] > arr[i+1]:
                instructions += 1
                return False
        else:
            instructions += 1
            if arr[i] < arr[i+1]:
                instructions += 1
                return False
    return True

def RandomSort(arr, s):
    global instructions

    while True:
        instructions += 1
        rand = random.randint(0,1)
        instructions += 1
        if rand == 1:
            instructions += 1
            if checkIfSorted(arr, s) == True:
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

def Bubble(arr, s):
    global instructions

    instructions += 1
    for x in range(0,len(arr)-1):
        instructions += 1
        for i in range(0,len(arr)-2):
            instructions += 1
            if s == 0:
                instructions += 1
                if arr[i] > arr[i+1]:
                    instructions += 1
                    swap(arr, i, i+1)
            else:
                instructions += 1
                if arr[i] < arr[i+1]:
                    instructions += 1
                    swap(arr, i, i+1)
        instructions += 1
    instructions += 1
    clear()
        
def main():
    global sent
    clear()
    array = []
    print('\n ***********************************************************')
    print(' *            Welcome to the Randomsort machine            *')
    print(' ***********************************************************')
    
    while True:
        print('\n **************************************************')
        print(' *                A: Sort the List                *')
        print(' *        C: Compare Bubble and Randomsort        *')
        print(' *                F: Fill randomly                *')
        print(' *          S: Shuffle the current list           *')
        print(' *           P: Print the current list            *')
        print(' *    T: Toggle the way of sorting (current: ' + printCurrAscent() + ')   *')
        print(' *               D: Delete a Number               *')
        print(' *               R: Remove the list               *')
        print(' *     Any Number: Add the number to the list     *')
        print(' *                    Q: Quit                     *')
        print(' **************************************************')
        print('\n Please enter your input!')
        inp = input(' -> ') 
        if handleInput(inp, array, sent) == 1:
            break

    print('Shutting Down ......................')
    time.sleep(2)

if __name__ == '__main__':
    instructions = 0
    sent = 0
    main()
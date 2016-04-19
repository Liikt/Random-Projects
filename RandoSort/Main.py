import time
import random
import os
import platform
import Sorts
import Utils

def handleInput(inp, arr, s):
    Utils.clear()
    if inp.lower() == 'q':
        return 1, arr, s
    elif inp.lower() == 's':
        arr = Utils.shuffleList(arr)
        return 0, arr, s
    elif inp.lower() == 'a':
        arr, ins = Sorts.RandomSort(arr, s)
        return 0, arr, s
    elif inp.lower() == 'p':
        Utils.printList(arr)
        return 0, arr, s
    elif inp.lower() == 'f':
        arr = Utils.rem(arr)
        arr = Utils.fillRandom(arr)
        return 0, arr, s
    elif inp.lower() == 'c':
        Utils.compare(arr, s)
        return 0, arr, s
    elif inp.lower() == 'd':
        arr = Utils.delete(arr)
        return 0, arr, s
    elif inp.lower() == 'r':
        arr = Utils.rem(arr)
        return 0, arr, s
    elif inp.lower() == 't':
        s = Utils.toggle(s)
        return 0, arr, s
    else:
        try:
            inp = int(inp)
            arr.append(inp)
            return 0, arr, s
        except:
            print('\n That was a wrong input!') 
            temp = input(' Press return to continue')
            Utils.clear()
            return 0, arr, s
        
def main():
    sent = 0
    Utils.clear()
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
        print(' *    T: Toggle the way of sorting (current: ' + Utils.printCurrAscent(sent) + ')   *')
        print(' *               D: Delete a Number               *')
        print(' *               R: Remove the list               *')
        print(' *     Any Number: Add the number to the list     *')
        print(' *                    Q: Quit                     *')
        print(' **************************************************')
        print('\n Please enter your input!')
        inp = input(' -> ')
        print(inp)
        inpu, array, sent = handleInput(inp, array, sent)
        if inpu == 1:
            break

    Utils.shutdown()

if __name__ == '__main__':
    main()
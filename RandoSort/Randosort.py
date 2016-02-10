import time
import random

test = [1, 5, 3, 2, 5, 3, 9]
tester = [1, 5, 3, 2, 5, 3, 9]
befehle = 0

def swap(arr, a, b):
	global befehle
	befehle += 1
	temp = arr[a]
	befehle += 1
	arr[a] = arr[b]
	befehle += 1
	arr[b] = temp

def checkIfSorted(arr):
	global befehle
	befehle += 1
	temp = arr
	befehle += 1
	for i in range(0,len(arr)-2):
		befehle += 1
		if arr[i] > arr[i+1]:
			befehle += 1
			return False
	return True

def RandomSort(arr):
	global befehle
	while True:
		befehle += 1
		rand = random.randint(0,1)
		befehle += 1
		if rand == 1:
			befehle += 1
			if checkIfSorted(arr) == True:
				befehle += 1
				return arr
		befehle += 1
		rand = random.randint(0,1)
		befehle += 1
		if rand == 1:
			befehle += 1
			rand2 = random.randint(0,(len(arr)-1))
			befehle += 1
			rand3 = random.randint(0,(len(arr)-1))
			befehle += 1
			swap(arr, rand2, rand3)

def Bubble(arr):
	global befehle
	befehle += 1
	for x in range(0,len(arr)-1):
		befehle += 1
		for i in range(0,len(arr)-2):
			befehle += 1
			if arr[i] > arr[i+1]:
				befehle += 1
				swap(arr, i, i+1)
		befehle += 1
	befehle += 1
		



RandomSort(test)
print('RandomSort: ' + str(befehle))
befehle = 0
Bubble(test)
print('BubbleSort: ' + str(befehle))
import sys
import time
#           1st pass                        2nd pass                               3rd pass
# ( 4 1 | 6 0 == 1 4 | 6 0 ) -> ( 1 4 6 | 0 == 1 4 6 | 0 ) -> ( 1 4 6 0 | == 1 4 0 6 | == 1 0 4 6 | == 0 1 4 6 )
# Not fast because it uses nested loops O(n^2) time, O(1) memory
# Time: O(n^2) - loops through array twice
# Space: O(1) - in place swaps / merge (hole overrwrites)

# Logical Steps:
# 1.) Selected First Unordered Element
# 2.) Swap other elements to the right to create correct position & shift unsorted element
# 3.) Advance the marker to the right one element

# Increasing (start: 1)         Decreasing (start: len(arr)-2)
# [10,4,0,2,11,20,3]            [10,4,0,2,11,20,3]
#                               [10,4,0,2,11,3,20]
# [10,4,0,2,11,20,3]            
# [4,10,0,2,11,20,3]            [10,4,0,2,3,11,20]

# [4,0,10,2,11,20,3]            [10,4,0,2,3,11,20]
# [0,4,10,2,11,20,3]            
#                               [10,4,0,2,3,11,20]
# [0,4,2,10,11,20,3]            
# [0,2,4,10,11,20,3]            [10,0,4,2,3,11,20]
#                               [10,0,2,4,3,11,20]
# [0,2,4,10,11,20,3]            [10,0,2,3,4,11,20]
#                       
# [0,2,4,10,11,20,3]            [0,10,2,3,4,11,20]
#                               [0,2,10,3,4,11,20]
# [0,2,4,10,11,3,20]            [0,2,3,10,4,11,20]
# [0,2,4,10,3,11,20]            [0,2,3,4,10,11,20]
# [0,2,4,3,10,11,20]
# [0,2,3,4,10,11,20]

#def insertionsort(arr,direction):
        #for start in range(1,len(arr)):
                #if direction == "increasing":
                        #currNum = arr[start]
                        #hole = start
                #else:
                        #currNum = arr[len(arr)-start-1]
                        #hole = len(arr)-start-1

                #print("Current Num: {}".format(currNum))
                #print("Start: {}".format(arr))
                #if direction == "increasing":
                        #while hole > 0 and currNum < arr[hole-1]:
                                #time.sleep(1)
                                #arr[hole], arr[hole-1] = arr[hole-1], arr[hole]
                                #print("Swap: {}".format(arr))
                                #hole = hole-1
                #else:
                        #while hole < len(arr)-1 and currNum > arr[hole+1]:
                                #time.sleep(1)
                                #arr[hole], arr[hole+1] = arr[hole+1], arr[hole]
                                #print("Swap: {}".format(arr))
                                #hole = hole+1
                        
                #print("End: {}".format(arr))
                #print()
        
        #return arr

def insertion_sort_swap(arr, direction):
	for initial_pass in range(1,len(arr)):
		for inverse_relation in range(initial_pass-1,-1,-1):
			print(initial_pass,inverse_relation)
			if arr[inverse_relation] > arr[inverse_relation+1]:
				if direction == "increasing":
					print("Current arr: {}".format(arr))
					print("Swapping: {} and {}".format(arr[inverse_relation], arr[inverse_relation+1]))
					arr[inverse_relation], arr[inverse_relation+1] = arr[inverse_relation+1], arr[inverse_relation]
					print("Swapped arr: {}".format(arr))
					print()
					time.sleep(1)
				else:
					break
			else:
				if direction == "increasing":
					break
				else:
					print("Current arr: {}".format(arr))
					print("Swapping: {} and {}".format(arr[inverse_relation], arr[inverse_relation+1]))
					arr[inverse_relation], arr[inverse_relation+1] = arr[inverse_relation+1], arr[inverse_relation]
					print("Swapped arr: {}".format(arr))
					print()
					time.sleep(1)
	
	return arr

def insertion_sort_shift(arr, direction):
	for initial_pass in range(1,len(arr)):
		currNum = arr[initial_pass]
		hole = initial_pass
		print("Current Num: {}, Index: {}".format(currNum, initial_pass))
		print("Start: {}".format(arr))
		if direction == 'increasing':
			while hole > 0 and arr[hole-1] > currNum:
				arr[hole] = arr[hole-1]
				time.sleep(1)
				print("Shift: {}".format(arr))
				hole = hole - 1
		else:
			while hole > 0 and arr[hole-1] < currNum:
				arr[hole] = arr[hole-1]
				time.sleep(1)
				print("Shift: {}".format(arr))
				hole = hole - 1
		arr[hole] = currNum
		print("End: {}".format(arr))
		time.sleep(1)
		print()

	return arr

def error():
        print("Invalid Entry.. Try again")
        print("Ex: 7,5,1,10,3,1,2")
        print("To exit enter 'q'")
        print()

while 1:
	data = input("Enter list of numbers to sort: ")

	if data == 'q':
		break

	method = input("Enter Insertion Sort Method: (1) Swap OR (2) Shift: ")
	direction = input("Enter Direction: (1) Decreasing (2) Increasing: ")
	data = data.split(',')

	try:
			data = [int(ele) for ele in data]
			method = int(method)
			direction = int(direction)
			direction = "decreasing" if direction == 1 else "increasing"
	except:
			error()
			continue

	if method == 1:
		print("Answer: {}".format(insertion_sort_swap(data,direction)))
	else:
		print("Answer: {}".format(insertion_sort_shift(data, direction)))
	print()

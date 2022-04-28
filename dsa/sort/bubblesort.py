import sys
import time

# Worst sorting algorithm, in terms of time. Space is good.
# Time - O(N^2)
# Space - O(1)

def bubblesort(arr,direction):
	for ele in range(len(arr)):
		currNum = arr[0]
		print("Iteration {}".format(ele))
		print("Start: {}".format(arr))
		for eleCompare in range(1,len(arr)-ele):
			time.sleep(1)
			if currNum < arr[eleCompare]:
				if direction == "increasing":
					print("Switch OG Largest {} with New Largest {}".format(currNum, arr[eleCompare]))
					time.sleep(1)
					tmp = currNum
					arr[eleCompare-1] = tmp
					currNum = arr[eleCompare]
				else:
					arr[eleCompare-1] = arr[eleCompare]
					
			else:
				if direction == "increasing":
					arr[eleCompare-1] = arr[eleCompare]
				else:
					print("Switch OG Smallest {} with New Smallest {}".format(currNum, arr[eleCompare]))
					time.sleep(1)
					tmp = currNum
					arr[eleCompare-1] = tmp
					currNum = arr[eleCompare]
				
			print("Arr: {}, Compared: {}\t{}".format(arr,currNum,arr[eleCompare]))

		arr[len(arr)-1-ele] = currNum 
		time.sleep(1)
		print("End: {}".format(arr))
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

	direction = input("Enter Direction: (1) Decreasing (2) Increasing: ")
	data = data.split(',')
	print()

	try:
		data = [int(ele) for ele in data]
		direction = int(direction)
		direction = "decreasing" if direction == 1 else "increasing"
	except:
		error()
		continue

	print("Answer: {}".format(bubblesort(data,direction)))
	print()


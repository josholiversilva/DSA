import sys
import time
# Time: O(nlogn)
# Space: O(n) - Auxilliary space to create temporary subarrays

# Merge sort uses a "divide-and-conquer" paradigm
# 1. Divide - Num of subproblems that are smaller instances of same problem
# 2. Conquer - Solve each subproblem recursively
# 3. Combine - All solutions to the subproblems into solution of original

# Merge sort application
# 1. Divide - n-element sequence to be sorted into 2 subsequences of n/2 elements each
# 2. Conquer - Sort Two subsequences recursively using merge sort
# 3. Combine - Merge 2 sorted subsequences to produce sorted answer

# base case - sequence to be sorted as length 1
# Dividing & Conquering = O(logn)
def mergesort(input):
	high = len(input)
	low = 0
	mid = high//2
	if high == 1:
		return [input[mid]]

	print("(Look Left) Divided {} into {}".format(input, input[low:mid]))
	print()
	time.sleep(1)
	left = mergesort(input[low:mid]) # 5
	
	time.sleep(1)
	print("(Look Right) Divided {} into {}".format(input, input[mid:high]))
	print()
	right = mergesort(input[mid:high]) # 2

	return merge(left,right,left+right)
	
# Loop through whole array's subproblems & sort along the way = O(N)
def merge(left, right, arrayToMerge):
	leftPtr, rightPtr, atmPtr = 0,0,0
	while leftPtr<len(left) and rightPtr<len(right):
		if left[leftPtr] <= right[rightPtr]:
			arrayToMerge[atmPtr] = left[leftPtr]
			leftPtr += 1
		else:
			arrayToMerge[atmPtr] = right[rightPtr]
			rightPtr += 1

		atmPtr += 1

	while leftPtr < len(left):
		arrayToMerge[atmPtr] = left[leftPtr]
		atmPtr += 1
		leftPtr += 1

	while rightPtr < len(right):
		arrayToMerge[atmPtr] = right[rightPtr]
		atmPtr += 1
		rightPtr += 1

	time.sleep(1)
	print("Merged Array: {} using L: {} & R: {}".format(arrayToMerge,left,right))
	print()
	return arrayToMerge

def error():
	print("Invalid Entry.. Try again")
	print("Ex: 7,5,1,10,3,1,2")
	print("To exit enter 'q'")
	print()
	
while 1:
	data = input("Enter list of numbers to sort: ")
	data = data.split(',')

	try:
		data = [int(ele) for ele in data]
	except:
		error()
		continue

	if data == 'q':
		break	
	
	print("Answer: {}".format(mergesort(data)))
	print()
	

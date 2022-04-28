import sys
import time

# Recursive partition with a pivot
# itemFromLeft = 1st Largest from left compared to pivot
# itemFromRight = 1st Smallest from right compared to pivot
# stop when itemFromLeft > itemFromRight 
# swap itemFromLeft with pivot

# Q: How to choose pivot?
# A: median-of-three -> 1st, middle, & last elements

# Time: Worst O(N^2), Best O(NLogN), Avg O(NlogN)
# Space: O(Logn) -> bc partitioning left/right of pivot every recursive call

def quicksort(arr):
	# base case (recursion)
	if len(arr) <= 1:
		return arr

	# Setting pivots
	pivot = len(arr)//2
	pivotVal = arr[len(arr)//2]

	# Swap pivot with last element & update pivot index
	print("Pivot Value: {}".format(pivotVal))
	print("Start: {}".format(arr))
	time.sleep(1)
	arr[pivot],arr[len(arr)-1] = arr[len(arr)-1],arr[pivot]
	pivot = len(arr)-1
	print("Swap Pivot with Last Ele: {}".format(arr)) 


	# Swap values until all left side < pivot and all right side >= pivot
	while True:
		leftLargest = 0
		rightSmallest = len(arr)-1

		while leftLargest < len(arr)-1 and arr[leftLargest] <= pivotVal:
			leftLargest += 1
		while rightSmallest > 0 and arr[rightSmallest] >= pivotVal:
			rightSmallest -= 1
		if leftLargest >= rightSmallest:
			break
		
		time.sleep(1)
		print("Swap: {} LL - {} RS - {}".format(arr,arr[leftLargest],arr[rightSmallest]))
		arr[leftLargest], arr[rightSmallest] = arr[rightSmallest], arr[leftLargest]
		print("After Swap: {}".format(arr))

	
	# Swap pivot into correct spot and update pivot value
	arr[leftLargest], arr[pivot] = arr[pivot], arr[leftLargest]
	pivot = leftLargest
	print("End: {}".format(arr))
	print("Left Partition: {}, Right Partition: {}".format(arr[:pivot], arr[pivot+1:]))
	print()
	
	# recurse the partition until len(arr) == 1
	arr[:pivot] = quicksort(arr[:pivot]) 			# left partition
	arr[pivot+1:] =	quicksort(arr[pivot+1:])		# right partition

	return arr

def quicksort_2(nums):
	if (len(nums) == 1):
		return nums
	if (len(nums) == 2):
		if nums[0] > nums[1]:
			nums[0], nums[1] = nums[1], nums[0]
		return nums

	pivot, left_ptr, right_ptr = len(nums)//2, 0, len(nums)-2

	nums[pivot], nums[len(nums)-1] = nums[len(nums)-1], nums[pivot]
	pivot = len(nums)-1
	while left_ptr < right_ptr:
		while nums[left_ptr] < nums[pivot] and left_ptr < len(nums)-2:
			left_ptr += 1
		while nums[right_ptr] > nums[pivot] and right_ptr > 0:
			right_ptr -= 1

		if left_ptr < right_ptr:
			nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]

	nums[left_ptr], nums[pivot] = nums[pivot], nums[left_ptr]
	pivot = left_ptr

	nums[:pivot] = quicksort_2(nums[:pivot])
	nums[pivot+1:] = quicksort_2(nums[pivot+1:])

	return nums

def error():
    print("Invalid Entry.. Try again")
    print("Ex: 7,5,1,10,3,1,2")
    print("To exit enter 'q'")
    print()

while 1:
	data = input("Enter list of numbers to sort: ")

	if data == 'q':
		break	

	data = data.split(',')
	
	try:
		data = [int(ele) for ele in data]
	except:
		error()
		continue

	print(data)

	print("Answer: {}".format(quicksort_2(data)))
	print()

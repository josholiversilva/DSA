
''' 1.) Maximum Subarray - Return sum of contiguous subarray (Easy) '''
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output = 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class SolutionMaxSub:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax, globalMax = -1, 0
        for num in nums:
            globalMax = max(globalMax, localMax+num)
            localMax = max(0, localMax+num)
        return globalMax
# O(n) time & O(n) space.
# Uses local maximum & global maximum to determine the largest sum
# 1.) Always determine whether local max > 0. If it ever goes below 0, we know that
# the addition of 2 numbers result in a lower value than previous. If it's > 0, we can safely assume
# that the current sum is greater than previous. 
# 2.) Determine if current local max is greater than global max. If it is, than that
# sum is the largest, so we store/replace that sum value.
# 3.) Loop through whole array & return largest sum

''' 2.) Valid Paranthesis - Easy '''

# Input - [ ({[]}) ]
# Output - True
# Explanation - Open brackets must be closed by the same type of brackets.
#               Open brackets must be closed in the correct order.

# Hashmap & stack
class SolutionValidParanthesis:
    def isValid(self, s: str) -> bool:
        hashmap = {'[' : ']', '(' : ')', '{' : '}'}
        stack = []
        for element in s:
            if element in hashmap.keys():
                stack.append(element)
            else:
                if not stack:
                    return False
                currStackElem = stack.pop()
                if hashmap[currStackElem] != element:
                    return False
            
        return stack == []

# One-way pass is the fastest way O(n) with O(n) space
# Hashmap is a perfect case for this since we know the keys and values
# Loop through and append to stack if the values are '(', '[', or '{'
# otherwise, pop the current element which would be the values of the keys then after popping,
# we can check if the element in the stack has the corresponding value in the hashmap

''' 3.) K largest values in array - Easy '''
# Given an array, return the top k largest values in the array
arr = [2,8,5,3,15]
k = 3
# output = [8,5,15]

from heapq import heappush, heappop
class Solution:
    def kLargest(self, arr, k):
        res = []
        heap = []
        for ele in arr:
            heappush(heap,-ele)
        for _ in range(k):
            res.append(-heappop(heap))

        return res

''' 4.) 215. Kth Largest Element in an Array - Medium '''
# Working with heaps
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return min(heapq.nlargest(k,nums)) # k=num largest eles, nums=iterable, return min (kth largest) of k size array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kq=[]
        # Initialize array of k size of first k elements i.e. k=2
        for i in range(k):
            heapq.heappush(kq,nums[i]) # creates min heap - (heap,item)
        
        # Compare k size array to the rest of num array after initialize point
        for k in nums[k:]:
            heapq.heappush(kq,max(k,heapq.heappop(kq))) # pops first index - smallest ele
            
        # Return smallest of k size array [2,3] <- 2 (kth largest)
        return heapq.heappop(kq) # heap

''' 5.) 347. Top K Frequent Elements - Medium  '''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Non-Optimized Brute Force [1032ms 5% faster]
        # Create Counter: O(n)
        # Loop through k largest indices O(k)
        # Every index, compare counter values & keep largest Value O(v)
        # Delete largestValue key in frequency & repeat with new frequency list
        # Time = O(n) + O(k)*O(v) = O(n)+O(k*v) = O(n+n^2) = O(n^2)
        # Space = O(f+h+r) = O(3n) = O(n)
            
        frequency = {}
        largestValue = {}
        res = []
        
        frequency = collections.Counter(nums)
        for count in range(k):
            largestValue[count] = 0
            largestKey = 0
            for key,val in frequency.items():
                largestValue[count] = max(largestValue[count],val)
                if val == largestValue[count]:
                    largestKey = key
            res.append(largestKey)
            del frequency[largestKey]
                
        return res

        # Optimized Heap+Counter [100ms 74.28% faster]
        # counter - {num:frequency} # O(n)
        # heap - k largest of (frequency,num) tuple #O(logn)
        # append k largest nums to result list & return
        # Time: O(n) + O(n*logn) + O(k) = O(2nlogn+k) = O(nlogn)
        # Space: O(r) + O(t) + O(f) = O(3n) = O(n)
        res = []
        tupleLargest = []
        frequency = collections.Counter(nums)
        for key,value in frequency.items():
            heapq.heappush(tupleLargest,(-value,key)) # push the count as negative, for max heap. python is minheap default
            
        for count in range(k):
            res.append(heapq.heappop(tupleLargest)[1])
            
        return res

        # My first one-liner for the style *sunglass_emoji*
        return [heapq.nlargest(k, ((value,key) for key,value in collections.Counter(nums).items()))[tupleIndex][1] for tupleIndex in range(k)]


''' 5.) First and Last Position of X in Sorted Array - Medium '''

''' 6.) 48. Rotate Image - Medium '''
# O(n^2) - Time, O(1) - Space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixSize = len(matrix)

        # First Move Diagonals
        #
        # [                             [
        #   [ 1 , 2,  3 ],                 [ 1, 4, 7 ],
        #   [ 4,  5,  6 ],      --->       [ 2, 5, 8 ],
        #   [ 7,  8,  9 ]                  [ 3, 6, 9 ]
        # ]                             ]
        for row in range(0,matrixSize):
            for column in range(0,row):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

        # Then Move Every Vertical Horizontally
        #
        # [                             [
        #   [ 1 , 4,  7 ],                 [ 7, 4, 1 ],
        #   [ 2,  5,  8 ],      --->       [ 8, 5, 2 ],
        #   [ 3,  6,  9 ]                  [ 9, 6, 3 ]
        # ]                             ]   
        for row in range(0,matrixSize):
            for column in range(0,matrixSize//2):
                matrix[row][column], matrix[row][matrixSize-1-column] = matrix[row][matrixSize-1-column], matrix[row][column]

''' 7.) 238. Product of Array Except Self - Medium '''
# Using tilde (inverted binary): 01 -> 10 so 2 becomes 4, 00->11 so 1 becomes 5
# In python array, reverses the elements similar to binary [1,2,3,4] first<->last, 2nd<->last-1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums) # [1,1,1,1]
        # Multiply all elements except nums[i]
        # Could be negative & length of nums >= 2
        # naive O(N^2)
        #for currNumIndex,currNumMultiply in enumerate(nums):
        #    currMultiple = 1
        #    for numToMultiplyIndex,numtoMultiply in enumerate(nums):
        #        if numToMultiplyIndex == currNumIndex:
        #            continue
        #        currMultiple *= numtoMultiply
        #    answer.append(currMultiple)
            
        # O(N) solution
        # nums = [1,2,3,4]
        # reaching numIndex, we should have all left products
        # reaching tilde (opposite) of numIndex, we should multiple by right prod before multiplying the current numIndex to right prod
        leftProduct = 1
        rightProduct = 1
        for numIndex in range(len(nums)):
            answer[numIndex] *= leftProduct # multiply all left side prods so that next num can inherit all left-side products
            leftProduct *= nums[numIndex] # keep getting left side prod so that next num indices get those products before multiplying by right product
            answer[~numIndex] *= rightProduct # multiply opposite index before, multiply that to rightProduct (now has leftProd*rightProd excluding self)
            rightProduct *= nums[~numIndex]# multiply tilde to right product for later left-side tildes
            
        return answer

''' 8.) 121. Best Time to Buy Stock Price - Easy '''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # naive - O(N^2), for every n choose smallest n' & take difference (n-n')
        # Total: O(N^2)
        # TLE
        globalProfit = 0
        #for buyIndex in range(len(prices)):
        #    if buyIndex == len(prices)-1:
        #        continue
        #    for sell in prices[buyIndex+1:]:
        #        currProfit = sell-prices[buyIndex]
        #        globalProfit = max(currProfit, globalProfit)
        #        
        #return globalProfit
        
        # Using a heap for comparisons
        # O(N) -> Traverse the list in backwards order
        #   O(logn) -> Push each node to the heap
        # O(1) -> Peek the largest value in heap (then heapVal-currVal for profit)
        # Total: O(N*logn+1) -> O(Nlogn)
        #heap = []
        #for buyIndex in range(len(prices)-1,-1,-1):
        #    if not heap:
        #        heapq.heappush(heap,-prices[buyIndex]) #maxheap
        #        continue
        #        
        #    currProfit = -heap[0] - prices[buyIndex]
        #    globalProfit = max(currProfit, globalProfit)
        #    heapq.heappush(heap,-prices[buyIndex])
        #return globalProfit
            
        # Using Greedy Method
        # O(N) -> Traverse through list (always buy @ smaller value) & sell @ current price
        # O(1) -> Compare using max() of always 2 updated numbers
        # Total: O(N)
        buy = float(math.inf)
        for price in prices:
            buy,globalProfit = min(price,buy), max(price-buy,globalProfit)
        
        return globalProfit

''' 9.) 134. Gas Station - Medium '''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute
        # 1. loop through n == len(gas) & len(cost)
        # 2. compare curr+gas-cost >= 0 if true startIndex=nIndex, else continue
        # 3. loop again len(n)
        # O(N^2)
        n = len(gas)
        for startIndex in range(n):
            curr = 0
            roundTrip = 0
            start = startIndex
            if curr+gas[startIndex]-cost[startIndex] < 0:
                continue
                
            while roundTrip != n:
                curr += gas[start]-cost[start]
                if curr < 0:
                    break
                start += 1 
                if start > n-1:
                    start = 0
                roundTrip += 1
            
            if curr >= 0:
                return startIndex
        
        return -1

        # O(N)
        # [-2,-2,-2,3,3] -> valid bc sum >= 0
        #                -> start @ index 3 bc currTotal >= 0
        diff = [gas[i]-cost[i] for i in range(len(gas))]
        total = sum(diff)

        if total < 0:
            return -1
        
        currTotal, start = 0, 0
        for index in range(len(gas)):
            currTotal += gas[index] - cost[index]
            if currTotal < 0:
                start = index+1
                currTotal = 0
                
        return start


''' 10.) 665. Non-decreasing Array - Medium '''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # modified = False
        # prev = -10**5-1
        # 1. Loop through each element starting at index 1
        # 2. nums[i] <= nums[i+1]? continue
        # 3. modified=True? return False
        # 4. try modify nums[i] w/ prev, if it works modified=True
        # 5. otherwise modify nums[i+1] -> nums[i]+1
        # 6. end of loop return True
        modified = False
        prev = -10**5-1
        for numIndex in range(len(nums)-1):
            if nums[numIndex] <= nums[numIndex+1]:
                prev = nums[numIndex]
                continue
                
            if modified:
                return False
            
            if prev <= nums[numIndex+1]:
                nums[numIndex] = prev
            else:
                nums[numIndex+1] = nums[numIndex]+1 
                
            modified = True
            prev = nums[numIndex]
            
        return True

''' 11.) 560. Subarray Sum Equals K - Medium '''
# Use hashmaps when trying to have sum/product to equal a target
# hashmap to lookup if we've seen the "target" before
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # magical O(N) solution using defaultdict
        ans = 0
        S = 0
        d = collections.defaultdict(int)
        d[S] = 1
        for num in nums:
            S += num
            ans += d[S-k]
            d[S] += 1
        
        return ans

''' 12.) 152. Maximum Product Subarray - Medium '''
# Use min, max when trying to find the largest of some sub
# take note of local min,max & global min,max
# while traversing in a linear fashion
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp
        # max, min
        # O(N)
        maximum, minimum, globalMax = nums[0], nums[0], nums[0]
        if len(nums) == 1:
            return nums[0]
        
        for x in range(1,len(nums)):
            maximum, minimum = max(maximum*nums[x], minimum*nums[x], nums[x]), min(maximum*nums[x], minimum*nums[x], nums[x])
            globalMax = max(maximum, globalMax)
            
        return globalMax

''' 13.) 442. Find All Duplicates in An Array - Medium '''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # nums = all integers in range [1,n]
        # loop through array [3,3,1]
        # possible to do below bc integer values appear once or twice
        # value of current element (3) , is the index-1 (2)
        # go to that index and make it negative (-1)
        # if the value of that index we went to (2)
        # is negative then we seen this number before
        ans = set()
        for numIndex in range(len(nums)):
            index = abs(nums[numIndex]) - 1
            if nums[index] < 0:
                ans.add(index+1)
            nums[index] *= -1
            
        return ans
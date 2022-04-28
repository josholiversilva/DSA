# 2 parameters
# 1 - String (sentence) - paranthesis/other chars
# 2 - Integer - index of one of opening paranthesis in sentence
# 
# return index of corresponding closing paranthesis
#

# input: 
# string "01(3(5()8))" -> a,A,0
# int: 2
# int: 4
#
# output: 10
# output2: 9
# 219(843)
def findClosingParan(sentence, openingParan):
    openParanCount = 0
    for charIndex in range(openingParan, len(sentence)):
        if sentence[charIndex] == '(':
            openParanCount += 1
        elif sentence[charIndex] == ')':
            openParanCount -= 1
            if openParanCount == 0:
                return charIndex

    return None

print(findClosingParan("01(3(5()8))", 4))












# function - Input/Output = List of intervals 
# Interval = start & end (tuple) start always < end
# merge intervals that overlap into single interval
# return list of merged intervals

# input: [(1,3), (4,5), (2,4), (-1,0)]
# output: [(1,5), (-1,0)]
#

# overlap = (1,4) (2,5)
# overlap2 = (1,5), (-1,0)
def intervals(times):
    for firstTime in range(len(times)):
        for secondTime in range(firstTime, len(times)):
            if isOverlap(firstTime, secondTime):
                continue

def isOverlap(firstTime0, firstTime1, secondTime0, secondTime1):
    if firstTime1 >= secondTime0:
        
        return True



def reverseArrRecurse(arr):
    def helper(arr, start=0, end=len(arr)//2):
        if start == end:
            return arr

        arr[start], arr[~start] = arr[~start], arr[start]
        helper(arr, start+1, end)

        return arr
    return helper(arr)

print(reverseArrRecurse([1,2,3,4,5,6]))





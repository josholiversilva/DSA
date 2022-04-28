# Python String Concatenation is weird.
# Time: O(N+M) where N is the concatentation string & M is the string to concatenate main string to
# Function below - (0+1)+(1+1)+(2+1)...+n = n(n+1)/2 = O(N^2)
# NOTE: Divide by 2 because we're adding 2 characters
def reverseString(inputString):
    outputString = ''
    for char in inputString:
        outputString = char + outputString

    return outputString

inputString = "hello world"
print(reverseString(inputString))


''' 1.) FizzBuzz - Easy'''
def fizzBuzz(self, n: int) -> List[str]:
        # %3 == "Fizz"
        # %5 == "Buzz"
        # %3 and %5 == "FizzBuzz"
        ans = []
        
        # naive
        for num in range(1,n+1):
            stringval = ""
            if num % 3 == 0:
                stringval += "Fizz"
            if num % 5 == 0:
                stringval += "Buzz"
            if stringval == "":
                stringval += str(num)
            
            ans.append(stringval)
        
        return ans  


''' 2.) Palindromic Substrings - Medium'''

''' 3.) Longest Substring with At Least K Repeating Characters - Medium '''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        staticLen = len(s)
        #base case 1 -> k is equal to always length of a char
        if k <= 1:
            return staticLen
        #base case 2 -> invalid entries
        if staticLen == 0 or staticLen < k:
            return 0
        
        # Divide Conquer
        substringCounts = Counter(s)
        pointer = 0

        ##################
        # left-substring #
        ##################

        # stop if invalid (left-substring)
        while pointer < staticLen and substringCounts[s[pointer]] >= k:
            pointer += 1
            
        # base case 3 (all valid then substring is the whole string)
        if pointer >= staticLen-1:
            return pointer

        leftSub = self.longestSubstring(s[0:pointer], k)

        ###################
        # right-substring #
        ###################

        # stop if valid
        while pointer < staticLen and substringCounts[s[pointer]] < k:
            pointer += 1
        rightSub = self.longestSubstring(s[pointer:], k) if pointer < staticLen else 0

        # return value of leftSub from 3 base cases
        return max(leftSub, rightSub)

''' 4.) 394. Decode String - Medium '''
class Solution:
    def decodeString(self, s: str) -> str:
        # brute force
        # assume k before [
        # try converting to int & printing char in []
        # if try works, 
        # except means we have [,],char
        # when we hit ], we do k*chars between [ & ]
        # output = 3*("a"+2*("c"))
        output = ""
        multStack = []
        multiplyChar = 0
        intChar = False
        for char in s:
            try:
                multiplyChar = int(char) + 10 * multiplyChar 
                intChar = True
            except:
                if intChar:
                    multStack.append(multiplyChar)
                    multiplyChar = 0
                    intChar = False
                    
                if char == "[":
                    multStack.append(char)
                elif char == "]":
                    expression = []
                    while True:
                        popMult = multStack.pop()
                        if popMult == '[':
                            multiply = multStack.pop()
                            if multStack:
                                multStack.append(multiply*''.join(expression))
                            else:
                                output += multiply*''.join(expression)
                            break
                        expression.insert(0,popMult)
                elif multStack:
                    multStack.append(char)
                else:
                    output += char

        return output
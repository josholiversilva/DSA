# sorting in place O(N)
def duplicatesInString():
    foo = "mppmt"
    return ''.join(sorted(set(foo),key=foo.index))

#print(duplicatesInString())

# Time: O(N)
# Space: O(1) - in place
s = "you got beautiful eyes"
import collections
def removeAlternateDuplicate(s):
    f = collections.defaultdict(int)
    ans = []
    for char in s:
        f[char] += 1
        if f.get(char,1) % 2 != 0:
            ans.append(char)
        
    return ''.join(ans)

#print(removeAlternateDuplicate(s))
nums = [100,180,260,310,40,535,692]
def stock(nums):
    buy = 999999999
    sell = 0
    profit = 0
    for num in nums:
        buy = min(buy,num)
        sell = max(num,sell)
        profit = max(sell-buy,profit)

    return profit

#print(stock(nums))

# You are given a string of 0’s and 1’s you have to find the number of 
# substrings in the string which starts and end with a 1.
def startEndOne(s):
    # dynamic sliding window that decreases size when amount of 1s > 2
    # ans when behind == ahead & different indices
    # temporarily decrease window until tmpBehind == ahead
    # add to ans when decreasing window and tmpBehind == ahead
    # go until end of string & return ans
    ans = 0
    try:
        behind, ahead = s.index('1'), s.index('1')
        numOnes = 1
    except:
        return ans

    while ahead != len(s):
        if ahead != behind and s[ahead] == '1' and s[behind] == '1':
            ans += 1
            numOnes += 1

        tmpBehind = behind
        tmpNumOnes = 0
        while tmpBehind != ahead and numOnes-tmpNumOnes > 2:
            tmpBehind += 1
            if ahead != tmpBehind and s[tmpBehind] == '1' and s[ahead] == '1':
                ans += 1
                tmpNumOnes += 1

        ahead += 1

    return ans


print(startEndOne("10101"))

# Given a string, find the longest substring which is palindrome
def longestPalindromicSubstring():
    # dynamic programming solution
    # O(N^2) Time & Space
    # dynamic programming

    # doesn't work atm
    if len(s) == 1:
        return s
    
    def dp(s):
        if len(s) <= 2:
            if s[0] == s[len(s)-1]:
                return s
            return ""
        
        left = dp(s[:len(s)-1])
        right = dp(s[1:])
        
        print(s, left, right)
        
        if s[0] == s[len(s)-1]: 
            if left==right:
                return s
        
        return left if len(left) >= len(right) else right
    
    return dp(s) if dp(s) != "" else s[0]

    # this works
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming
        if len(s) < 2:
            return s
        
        memo = {}
        start,end = 0,1
        for x in range(len(s)):
            for row in range(len(s)-x):
                col = row+x
                if row == col:
                    break
                 
                if col-row<3:
                    if s[row] == s[col]:
                        memo[(row,col)] = 1
                        start = row
                        end = col+1
                        continue
                else:
                    if s[row] == s[col] and memo[(row+1,col-1)] == 1:
                        memo[(row,col)] = 1
                        start = row
                        end = col+1
                        continue
                
                memo[(row,col)] = 0

        return s[start:end]

    # Start from the Middle
    # O(N^2) Time, O(1) Space


# Given a list of strings (boxList), sort each element with the following procedures
# 1.) alpha > numeric
# 2.) int(alph) > int(alph2) c > b
# 3.) if same, greater identifier should be used

# Given the following:
# Integer maxDistance
# List[List]<Integers> forwardTravel
# List[List]<Integers> returnTravel
# Return the most optimal forwardTravel,returnTravel keys such that
# the sum of both distances are no greater than maxDistance
# 
# maxDistance = 10000
# forwardTravel = [ [1,3000], [2,5000], [3,7000], [4,10000]]
# returnTravel = [ [1,2000], [2,3000], [3,4000], [4,5000]]
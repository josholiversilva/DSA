# First interview question

'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
 Input: s = "abcabcbb"
Output: 1
Explanation: The answer is "abc", with the length of 3.
Example 2:
 Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
 Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:
 Input: s = ""
Output: 0

Example 5:
 Input: s = "abacd"
Output: 4
Explanation: The answer is "bacd", with the length of 4.

Constraints:
 0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

s = "abcabcbb"
def findLongestSub(s):
    # 1. Having memory to keep track of what we've seen in string
    # 2. Looping through whole string and checking if seen before in memory
    # 3. Keep track of longest substring without repeat char
    globalMax, localMax = 0, 0
    prev = set()
    repeatIndex = 0
    for charIndex in range(len(s)):
        while s[charIndex] in prev:
            prev.remove(s[repeatIndex])
            repeatIndex += 1
            localMax -= 1
            
        prev.add(s[charIndex])
        localMax += 1
        globalMax = max(globalMax, localMax)
        
    return globalMax

#print(findLongestSub(s))






























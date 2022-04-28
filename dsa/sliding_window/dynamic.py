'''
- 2 Pointers (!st = start, 2nd = end)
- A case to Increase window, if unsatisfied contract
- globalMax, localMax, prev {} <- set if not repeating or dictionary otherwise
- base case for any other edge cases that effect points above
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dynamic sliding window with map
        # Time: O(N)
        # Space: O(N)
        prev = {}
        start, end = 0, 0
        maxLen = 0
        maxCount = 0
        while end < len(s):
            prev[s[end]] = 1 if not prev.get(s[end],None) else prev[s[end]]+1
            maxCount = max(prev.values())
            
            while (end - start + 1) - maxCount > k: # <- contraction case (continue increasing otherwise)
                prev[s[start]] -= 1
                start += 1
                
            maxLen = max(maxLen, end-start+1) # previous window size or current window size 
            end += 1
            
        return maxLen
        
        '''
        * AABABBA
        * ^
        * ^
        *
        * prev = {A:}
        * maxLen
        * maxCount
        *
        * window_size - maxCount
        * ( R - S + 1) - maxCount
        '''

# Delete three consescutive duplicates letter from an array.
s = 'aaabfjdddkkdbbbb'
def threeConsecutive(s):
    # static sliding window
    # window size of 3 every time
    # delete whole window if all is 3
    start, end = 0, 2
    s = list(s)
    if len(s) <= 2:
        return s

    while end <= len(s):
        print(s[start:end+1])
        if len(set(s[start:end+1])) == 1:
            if start == 0:
                s = s[end+1:len(s)]
            elif end == len(s)-1:
                s = s[:start]
            else:
                s = s[0:start]+s[end+1:len(s)]
            continue
        start += 1 
        end += 1

    return ''.join(s)

print(threeConsecutive(s))

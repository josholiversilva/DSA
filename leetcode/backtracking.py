'''
# 1.) 17. Letter Combinations of a Phone Number - Medium
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetter = {"2":{'a','b','c'},"3":{'d','e','f'},"4":{'g','h','i'},"5":{'j','k','l'},"6":{'m','n','o'},"7":{'p','q','r','s'},"8":{'t','u','v'},"9":{'w','x','y','z'}}
        origLen = len(digits)
        
        def getCombos(digits,output,currOutput):
            if len(currOutput) == origLen: 
                output.append(currOutput)
                return
            
            for digitIndex in range(len(digits)):
                for letter in digitToLetter.get(digits[digitIndex]):
                    getCombos(digits[digitIndex+1:],output,currOutput+letter)
                    
            return output
       
        return getCombos(digits,[],"")
                

# 2.) 78. Subsets - Medium
class Solution:
    def subsets(self,nums):
        output = []

        self.helper(nums,0,[],output)
        return output
    
    # Head recursion along the way pattern for filling output values
    def helper(self, nums, start, temp, output):            #i=0         rec       rec          rec      back+1    back+1      rec       i=1        rec         rec      i=2        i=3
            output += [temp]                                # [],       t[1]   ,  t[1,2]   ,  t[1,2,3] , t[1,2]  , t[1]      , t[1,3]  , t[]      , t[2]      , t[2,3] , t[]      , t[3]
            for i in range(start,len(nums)):                #i=0,      i=0+1   ,  (0+1)+1  ,  (0+1+1)+1, (1+1)+1 , (1+1)     , (1+1)+1 , i=1      , 1+1       ,  1+1+1 , i=2      , i=3
                self.helper(nums,i+1,temp+[nums[i]],output) #t[]+n[1],t[1]+n[2],t[1,2]+n[3],      <>   , <>      , t[1]+n[3] , <>      , t[]+n[2] , t[2]+n[3] , <>     , t[]+n[3] , DONE

    # first loop where i=0 & temp=[]+[1]
    # [[], [1], [1,2], [1,2,3], [1,3]]
    # second loop where i=1 & temp=[]+[2]
    # [[2], [2,3]]
    # third loop where i=2 & temp=[]+[3]
    # [[3]]

# 3.) 22. Generate Parenthesis
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # size 3: 3( with 3)
        #                ( <- must start with open paranthesis     
        #             /       \   
        #1          (           )   <- open again or close (always 2 choices)
        #          / \          |
        #         (   )         (   <- after close, must open if n( = n) 
        #       / |   / \      / \
        #     nO  )  (  )     (   )
        #         |  |  |     |   |
        #         )  )  (     )   (
        #         |  |  |     |   |
        #         )  )  )     )   )
        #   ['((()))', '(()())', ..]
        # If we ( n times, we're locked in, we must close it x amounts of times until size = n*2 (bc there's 2 characters for each n)
        # characters = n*2 = depth of recursion tree
        #
        # Things to keep in mind
        #
        # 1.) for each choice keep track of the # ( -> this is crucial bc we start off with 1 extra ( since we must start with (.
        # 2.) once we reach n (, we're forced to continue with ) the rest of the way
        # 3.) ALWAYS either ( OR ), no other direction -> O(n^2) executions
        # 4.) After ), must ( as long as ( == )
        
        # base case
        if n < 1:
            return []
        if n == 1:
            return ["()"]
        
        validParanthesis = []
        self.helper(n, validParanthesis, "", 0, 0)
        
        return validParanthesis
        
    def helper(self, n, validParanthesis, currentParanthesis, numOpen, numClose):       
        # append to list
        if numOpen+numClose == n*2:
            validParanthesis.append(currentParanthesis)
        
        if numOpen < n:
            self.helper(n, validParanthesis, currentParanthesis+"(", numOpen+1, numClose)
        if numClose < n and numClose < numOpen:
            self.helper(n, validParanthesis, currentParanthesis+")", numOpen, numClose+1)

# 4.) 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # With sortin
        #                         []       target = 7
        #                   /     |   \   \  
        #                  2      3    6   7 <- target >= each ele of candidate
        #      / \.     /  \     / \ 
        #     7   6     2    3   2  3
        #             / \   |   |
        #            2   3  2   2 
        #.          /
        #          None
        #
        # Optimized w/o sorting (Faster best case but same worst case ) 
        #                         []       target = 7
        #                   /     |   \   \  
        #                  2      3    6   7 <- target >= each ele of candidate
        #      / \.     /  \     / \    |
        #     7   6     2   3    6  7   7
        #             / \      
        #            2   3    
        #.          /
        #          None
        #
        #
        # Decisions: Try each element as long as-- currTarget + ele <= target
        # Return Case: currTarget == target, append currTarget to result[[]]
        # Approach: DFS/backtracking find all combo sums
        # Time: # subproblems = len(candidates), Compare len(candidates)+(O(nlogn)+O(n)) for each subproblem -> so the running time = n**n+2nlogn -> O(n^n)
        #
        # 2^2 = 4
        # 3^3 = 27
        # 4^4 = 256
        #
        # base cases
        combinationSum = []
        
        if not candidates:
            return combinationSum
        
        def traverseCandidates(combinationSum, candidates, currCombo, currSum, target):
            if currSum == target:
                # sorting is not necessary here if we use a different approach
                # i.e target=3
                #     [1,2,3]c1 -> subprob is [1,2,3] & we'd use 1+1+1, 1+2+1 <- 2 is encapsulated
                #     [1,2,3]c2 -> subprob is [2,3] since 2 is encapsulated in previous
                #     [1,2,3]c3 -> subprob is [3]
                #
                # non-optimized [220ms] - 11% faster
                #currCombo.sort() # Add nlogn
                #if currCombo in combinationSum: # Add n
                #    return
                
                combinationSum.append(currCombo[:])
                currCombo=[]
                return
        
            # non-optimized [220ms] - 11% faster
            #for candidate in candidates:
            #    if currSum+candidate <= target:
            #        #print(candidate, currSum, currSum+candidate, currCombo)
            #        traverseCandidates(combinationSum, candidates[candidate:], currCombo+[candidate], currSum+candidate, target) #n^n
            #
            # optimized [56ms] - 85% faster
            for candidateIndex in range(len(candidates)):
                if currSum+candidates[candidateIndex] <= target:
                    #print(candidate, currSum, currSum+candidate, currCombo)
                    traverseCandidates(combinationSum, candidates[candidateIndex:], currCombo+[candidates[candidateIndex]], currSum+candidates[candidateIndex], target) #n^n       

        traverseCandidates(combinationSum, candidates, [], 0, target)  
        return combinationSum
        
# 5.) 77. Combinations - Medium

'''

def bg(arr):
    output = []

    # no girl can be between any boy
    def dfs(arr, output, curr, is_bg, start, target_len):
        if len(curr) == target_len:
            print(curr)
            output.append(curr)
            return
        if is_bg and len(arr) > 0 and len(curr) >= 2:
            print('----> is_bg')
            print(curr)
            if arr[0] == 'b' and curr[len(curr)-2] == 'b':
                return

        for idx in range(start, target_len):
            print(arr, curr, start)
            #if arr[arr_idx] == 'g':
                #dfs(arr[arr_idx+1:], output, curr+arr[arr_idx], True, target_len)
            #else:
            dfs(arr, output, curr+arr[idx], False, idx+1, target_len)

        return output

    return dfs(arr, output, "", False, 0, len(arr))

print(bg(['b', 'b', 'g']))

# arr = [b,b,g]
# arr = [b,b,g,g]
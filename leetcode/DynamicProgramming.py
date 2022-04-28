''' 1.) 64. Minimum Path Sum - Medium '''
# Attempted backtracking.. Time Limit Exceeded. O(2^n+m)
# Works but too slow
# ACTUALLY should use DP (Dynamic Programming)
# DP works but still slow - O(N) but only 5% faster at 180ms
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #
        # Given that its non-negative numbers, directed (only down or right)
        #
        #
        #      (3) -----> (1) --------> (1)
        #    />    \>                 />    \>
        # (1)      (5)----------------       (1)
        #    \>   />                  \>     />
        #     (1)-------> (4) --------> (2)
        #
        #
        # 2 choices every moment in time
        # Can only go down len(rows) and right len(cols)
        #                            (0,0)
        #                   R/                  \D
        #                (0,1)                    (1,0)
        #            R/         D\            R/         \D
        #           (0,2)       (1,1)        (1,1)            (2,1)
        #         /      \     /      \     /      \       /       \
        #     (0,3)     (1,2) (1,2)  (2,1) (1,2)   (2,1)  (2,2)    (3,1)
        #             /   \    
        #           (1,3)  (2,2)
        # Backtracking
        #
        # Dynamic Programming (memo)
        memo = {}
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        def explore(start):
            row_len = len(grid)
            col_len = len(grid[0])
            row,col = start

            if memo.get((row,col)):
                return memo[(row,col)]
            if (row,col) == (row_len-1,col_len-1):
                return grid[row][col]
            if row >= row_len or col >= col_len:
                return 9999999
            
            memo[(row,col)] = grid[row][col] + min(explore((row,col+1)), explore((row+1,col)))
            return grid[row][col] + min(explore((row,col+1)), explore((row+1,col)))
        
        return explore((0,0))

''' 2.) Search 2D Matrix II - Medium '''
# Using DP doesn't work TLE - O(N)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_len = len(matrix)
        n_len = len(matrix[0])
        memo = {}
        # using dp & memoization
        def dp(target,curr):
            row,col = curr
            
            if memo.get(curr):
                return memo[curr]
            elif row >= m_len or col >= n_len:
                return False
            elif curr == (m_len-1,n_len-1) and matrix[row][col] != target:
                return False
            elif matrix[row][col] == target:
                return True
           
            memo[curr] = False
            if dp(target,(row,col+1)) or dp(target,(row+1,col)):
                return True
        
            return False
        
        return dp(target,(0,0))

 ''' 3.) Unique Paths - Medium '''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top-down dp
        memo = {}
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    memo[(row,col)] = 1
                else:
                    memo[(row,col)] = memo[(row-1,col)] + memo[(row,col-1)]
                        
        return memo[(m-1,n-1)]

# recursive memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(currRow, currCol):
            
            if memo.get((currRow,currCol)):
                return memo[(currRow,currCol)]
            if currRow >= m or currCol >= n:
                return 0
            if (currRow,currCol) == (m-1,n-1):
                return 1
                
            memo[(currRow,currCol)] = dfs(currRow+1,currCol) + dfs(currRow,currCol+1)
            return dfs(currRow+1,currCol) + dfs(currRow,currCol+1)
            
        return dfs(0,0)


''' 4.) Climbing Stairs - Easy '''
class Solution:
def climbStairs(self, n: int) -> int:
    # dfs
    # binary -> 1 or 2 steps
    # recursive algo -> once we reach stepNum == n, return 1
    #                   if > stepNum return 0
    #                   else keep recurising binary options (1 or 2 stesp)
    #                   return all possible steps
    # Time: O(2^N)
    # Space: O(1)
    #
    # Using dp recursive memo: O(N), O(N)
    memo = {}
    def dfs(stepAmount):
        if memo.get(stepAmount):
            return memo[stepAmount]
        if stepAmount == n or stepAmount == n-1:
            return 1
        if stepAmount > n:
            return 0
            
        memo[stepAmount] = dfs(stepAmount+1)+dfs(stepAmount+2)
        return dfs(stepAmount+1) + dfs(stepAmount+2)

    return dfs(0)

    # top-down tabluation approach: O(N), O(N)
    memo = {}
    stepAmount = n
    for numIndex in range(n,-1,-1):
        if stepAmount == n or stepAmount == n-1:
            memo[stepAmount] = 1
        else:
            memo[stepAmount] = memo[stepAmount+1] + memo[stepAmount+2]
        stepAmount -= 1

    return memo[0]
    

''' 5.) Longest Palindromic Substring - Medium '''
class Solution:
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
                
                        
''' 1.  Given an array of numbers and a key, return a list of lists
        for the different combinations that equal the given key
'''
class QuestionOne:
    def diffCombos(self,nums, key):
        # nums = [3,2,5,1]
        # key = 5

        # output -> [[5],[3,2], [2,2,1]]
        # when we spot 3,2 we don't use 2,3
        # also could be out of order -> 2,2,1

        # Combinations -> backtracking
        # 1. Iterate each num in nums
        # 2. for each num we recursively compare sum of currNum + everything on right of currNum, keep currList
        # 3. if currNum >= key, move on to next iteration (continue), append currList (recursive) if currNum == key to ansList
        # 4. end iteration
        # 5. return appended ansList
        # Time: O(n!+n-1!)
        # Space: O(n)

        # alternative
        # nums -> sort (Nlogn) -> [1,2,2,3,5]
        # 1. Iterate each num in nums
        # 2. for each num, we just recursively add currElement+currNum keep currNum & currList
        # 3. append currList to ansList, continue overhead iteration if >= key
        # 4. return appended ansList
        # 5. Time: O(Nlogn + n!)
        # 6. Space: O(N)
        nums.sort()
        ansList = []
        def keyEqual(currSum=0, currList=[], currNums=nums):
            if currSum == key and currList:
                if currList not in ansList:
                    ansList.append(currList[:])
                return

            for numIndex in range(len(currNums)):
                if currSum+currNums[numIndex] <= key:
                    keyEqual(currSum+currNums[numIndex],currList+[currNums[numIndex]], currNums[numIndex+1:])

            return

        keyEqual()
        return ansList

    def test(self):
        print(self.diffCombos([1,2,3,5],5))
        print(self.diffCombos([5,3,0,1,10],4))
        print(self.diffCombos([23,4,2,10,9,3,1],12))
        print(self.diffCombos([9,3,5,2,2,4],9)) # -> [2,2,3,4,5,9]

''' 2.  Given root of a binary tree and integer TargetSum
        return all root-to-leaf paths where each path's
        sum equals targetSum
'''
# Example - [4,2,6,1,3,5,7], targetSum = 10
# Return list of integers
#               (4)
#              /   \
#            (2)    (6)
#           /   \   /   \
#         (1)   (4) (5)  (7)
#               /
#             (4)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
class QuestionTwo:
    def pathSum(self, root, targetSum):
        # 1. BFS + DFS Solution (Mix)
        # Note: keep track of currList & currSum in recursive vars
        # 1. Outer Loop (BFS) -> add currNod val to currSum & recurse the children to add currSum
        # 2. DFS (Recursive currSum) -> continually add on to currSum as long as children exists & currSum <= targetSum
        # 3.                            append currList to ans
        # 4. Repeat BFS loop until traversed through all nodes
        # 5. return ans
        # Time: O(N*Logn)
        # Space: O(N) -> ans == len(tree)
        def dfs(root, currSum, currList):
            if currSum == targetSum:
                ans.append(currList[:])
            if not root or currSum >= targetSum:
                return

            if root.left:
                dfs(root.left, currSum+root.left.val, currList+[root.left.val])
            if root.right:
                dfs(root.right, currSum+root.right.val, currList+[root.right.val])
            
            return

        ans = []
        q = collections.deque([root])
        while q:
            layer = list(q)
            q.clear()
            for parent in layer:
                dfs(parent,parent.val,[parent.val])
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)

        return ans


    def test(self):
        node1 = TreeNode(4)
        node2 = TreeNode(2)
        node3 = TreeNode(6)
        node4 = TreeNode(1)
        node5 = TreeNode(4)
        node6 = TreeNode(5)
        node7 = TreeNode(7)
        node8 = TreeNode(4)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        node5.left = node8
        print(self.pathSum(node1, 10))

q1 = QuestionOne()
q2 = QuestionTwo()
q2.test()
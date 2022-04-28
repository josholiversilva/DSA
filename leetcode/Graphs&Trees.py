''' 1.) Symmetric Tree - return bool (Easy) ''' 
# Input: nums = [1,2,2,3,4,4,3]
# Output = True
# Explanation: Symmetric @ it's center

#########
######### Wrong
#########
class SolutionSymmetricTreeWrong:
    def isSymmetric(self, root: TreeNode) -> bool:
            if root == None:
                return True
            
            # iteratively
            frontier = [root]
            n = 1
            
            while frontier:
                nextFrontier = []
                compareArray = []
                noAdjacents = True
                
                for node in frontier:
                    if node.left:
                        compareArray.append(node.left.val)
                        nextFrontier.append(node.left)
                        noAdjacents = False
                    else:
                        compareArray.append(None)
                        
                    if node.right:
                        compareArray.append(node.right.val)
                        nextFrontier.append(node.right)
                        noAdjacents = False
                    else:
                        compareArray.append(None)
                        
                if noAdjacents:
                    break
                        
                if compareArray[0:2**n//2] != compareArray[2**n//2:len(compareArray)][::-1]:
                    return False
                
                frontier.pop(0)
                if nextFrontier:
                    frontier = nextFrontier
                n += 1
            
            return True      

# Time: O(n) Space: O(n)
# This is a wrong approach I was going for.
# 1.) Very long & messy with brute forced if/else statements
# 2.) Was NOT thinking recursively.. I was thinking top-level scenarios @ root (1) & connecting to roots (2,2)
# This unrecursive thinking led me to a weird answer of statically defining height & always appending "None".
# ^^ Led to a bug where None appends would lead to wrong comparisons, saying false @ wrong times

#########
######### Right
#########
# BFS with queue
class SolutionSymmetricTreeRight:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        queue = collections.deque([root.left, root.right])
        while queue:
            r1 = queue.pop()
            r2 = queue.pop()
            if r1 == None and r2 == None:
                continue
            if r1 == None or r2 == None:
                return False
            if r1.val != r2.val:
                return False
            queue.append(r1.left)
            queue.append(r2.right)
            queue.append(r1.right)
            queue.append(r2.left)
        return True

# Right approach is breaking the big tree into little trees every iteration.
# Start at the left & right childs after determining there's a root -> [left, right]
# compare left & right node, then append [left.left, right.right, left.right, right.left] iteratively
# Then we go back to comparing 2 nodes at a time [left.left, right.right, left.right, right.left] -> [left.left, right.right]
# After comparing, append child nodes of those nodes (we get back to top-inner tree later): x = left.right, y = right.left
# [left.left, right.right, x.left, y.right, x.right, y.left] keep going until no childs which leads us back to [left.left, right.right] and continue

''' 2.) Permutations - Medium '''
# Input - nums = [1,2,3]
# Output - [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
# Reason - Unique # of integers in nums so always equal to len(nums)! i.e. 3!

# DFS & Backtracking
# WORKS only for [1,2,3] <- 3 elements so NOT FULL CORRECT
from collections import defaultdict #overrides one method and adds one writable instance variable
def permute(nums):
    if len(nums) <= 1:
        return [nums]
    
    output, inner = [], []
    visited = defaultdict(list) # without this unable to initialize with visited[#] = [#]
    pool = nums[:] # pass by value - creates a copy of the original list
    # pool = nums # pass by ref - caller & function references same object in memory
    index = 0
    while True:
        if not pool:
            output.append(inner[:])
            pool.append(inner.pop())
            index -= 1  
            
            if 0 in visited.get(nums[len(nums)-1],[-1]) and len(visited.get(nums[0])) >= len(nums)-1:
                break
        
        else:
            if index not in visited.get(pool[0],[-1]):
                if not inner:
                    visited = defaultdict(list)
                visited[pool[0]].append(index)
                inner.append(pool.pop(0))
                index += 1
            else:
                pool.append(inner.pop())
                index -= 1
            
    return output 

# Right answer
# O(2^n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        
        ans = []
        permutation = []
        verified = [False]*len(nums)
        self.helper(nums, ans, permutation, verified)
        
        return ans
        
    def helper(self, nums, ans, permutation, verified):
        if len(permutation) == len(nums):
            return ans.append(list(permutation))
        
        for x in range(0,len(nums)):
            if verified[x]:
                continue
        
            verified[x] = True
            permutation.append(nums[x])
            self.helper(nums, ans, permutation, verified)
            verified[x] = False
            permutation.pop(len(permutation)-1)

''' 3.) 1325. Delete Leaves With a Given Value - Medium '''
# DELETING A NODE STEPS
# Set root = None
# Return None
# Upper Layer, set root.child = return value (None)
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        # At least 1 node
        # DFS until leaf nodes - no children, delete return None
        # if not left & right (previously had chilren) delete root & return None
        # time: O(N-1)
        if not root:
            return None
        
        if not root.left and not root.right:
            if root.val == target:
                root = None
            
            return root
            
        left = self.removeLeafNodes(root.left,target)
        right = self.removeLeafNodes(root.right,target)
        
        root.left = left
        root.right = right
        
        if not root.left and not root.right:
            if root.val == target:
                root = None
        
        return root
        
        
        

''' 6.) 207. Course Schedule - Medium '''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [[2,0],[1,0],[3,1],[3,2],[1,3]]
        #   (1) <-- (3)
        #  </      /
        # (0)     /
        #   <\  </
        #    (2)
        # takeCourse = graph.keys
        # neededCourses = graph.values
        # loop through takeCourse (outer)
        # cycle? -> determine by comparing 1st takeCourse, put in visited & continue on to neededCourses i.e {1:[0,3]} <- recurse through 0 append visited to 0, then 3 append 3 to visited 1->0, 1->3, 3->1, 1->cycle (already in visited)
        def cycle(visited, neededCourses, currCourse):
            if not neededCourses: #[0,3], [], [3]
                return False
            if currCourse in visited: #1 in[]? 1 in [1,0,3]?
                return True
            
            visited.append(currCourse) # [1,0,3]
            
            for needCourse in list(neededCourses): # [0,3], [3], [1]
                if cycle(visited,graph.get(needCourse,[]),needCourse): #0-False
                    return True 
                neededCourses.remove(needCourse) # [3]
                
        graph = {}
        for takeCourse,needCourse in prerequisites:
            if graph.get(takeCourse,None):
                graph[takeCourse].append(needCourse)
            else:
                graph[takeCourse] = [needCourse]
        
        visited, unvisited = [], graph.keys()
            
        for unvisitedCourse in unvisited: #[1]
            if unvisitedCourse in visited: #[]
                continue
            if cycle(visited,graph.get(unvisitedCourse),unvisitedCourse): #1:[0,3]
                return False
            
        return True        

''' 7.) 199. Binary Tree Right Side View - Medium '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # root -> left & right
        # array rep -> [root,left,right,ll,lr,rl,rr]
        ans = []
        if not root:
            return ans
        
        queue = collections.deque([root])
        layer = [root]
        
        while queue:
            currNode = queue.popleft()
            queue = collections.deque([])
            for node in list(layer):
                if node.left:
                    queue.appendleft(node.left)
                    layer.append(node.left)
                if node.right:
                    queue.appendleft(node.right)
                    layer.append(node.right)
                layer.pop(layer.index(node))
            
            ans.append(currNode.val)
            
        return ans

''' 8.) Invert Binary Tree - Easy'''
###  Node - > left, right ,value
### 
## root = root.val -> value
## root = {left:ptrObject,right:ptrObject2,val:1}
def invertTree(root):
    #            (1)
    #          /     \
    #       (2)       (3)
    #      /   \     /   \
    #     (4)  (5)  (6)  (7)
    def DFS(root):
        if not root:
            return root

        left = DFS(root.left)
        right = DFS(root.right)
        
        root.left = right
        root.right = left

        return root

''' 9.) 733. Flood Fill - Easy '''
# 2D Array Matrix Easy
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # [
        #   [1,1,1],
        #   [1,1,0],
        #   [1,0,1]
        # ]
        
        # add/subtract x, keep y
        # add/subtract y, keep x
        def DFS(originalColor, image, sr,sc,visited):
            if sr<0 or sc<0 or sr>len(image)-1 or sc>len(image[0])-1 or image[sr][sc] != originalColor or [sr,sc] in visited:
                return image
            else:
                visited.append([sr,sc]) 
                image[sr][sc] = newColor
                
                DFS(originalColor,image,sr-1,sc,visited)
                DFS(originalColor,image,sr+1,sc,visited)
                DFS(originalColor,image,sr,sc-1,visited)
                DFS(originalColor,image,sr,sc+1,visited)

      
        visited = []
        originalColor = image[sr][sc]
        DFS(originalColor,image,sr,sc,visited) 
        return image

''' 10.) 200. Number of Islands - Medium '''
# 2D Array Medium 
# Time Limit Exceeded (Not Optimized But Works)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop thorugh the whole grid O(N) where N = mxn
        # start @ grid[0][0] then DFS up,down,right,left until we hit 0 (water) <- base case
        # Save each visited node in a list visited[]
        # keep an islandCount, after DFS everywhere for 1 (islands) increment by 1
        # Finish after looping through whole grid & return islandCount
        # O(MxNxE) 
        def DFS(grid,m_row,n_column,m_len,n_len,visited):
            if m_row<0 or n_column<0 or m_row>m_len-1 or n_column>n_len-1 or grid[m_row][n_column] == "0" or [m_row,n_column] in visited:
                return
            
            visited.append([m_row,n_column])
            DFS(grid,m_row,n_column+1,m_len,n_len,visited) #right
            DFS(grid,m_row,n_column-1,m_len,n_len,visited) #left
            DFS(grid,m_row+1,n_column,m_len,n_len,visited) #up
            DFS(grid,m_row-1,n_column,m_len,n_len,visited) #down
            
        m_row = len(grid)
        n_column = len(grid[0])
        visited = []
        islandCount = 0
        for row in range(m_row):
            for column in range(n_column):
                if [row,column] not in visited and grid[row][column]!="0":
                    DFS(grid,row,column,len(grid),len(grid[0]),visited)
                    islandCount += 1
                
        return islandCount

''' 11.) 938. Range Sum of BST - Easy '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #DFS
        return self.DFS(root,low,high)
      
    def DFS(self,root,low,high):
        if not root:
            return 0
        
        if root.val < low:
            return self.DFS(root.right,low,high)
        elif root.val > high:
            return self.DFS(root.left,low,high)
        else:
            return root.val+self.DFS(root.right,low,high)+self.DFS(root.left,low,high)

''' 12.) 100. Same Tree - Easy '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.DFS(p) == self.DFS(q)
    
    def DFS(self,root):
        if not root:
            return [None]
       
        if root.left and root.right:
            return [root.val]+self.DFS(root.left)+self.DFS(root.right)
        elif root.left:
            return [root.val]+self.DFS(root.left)
        elif root.right:
            return [root.val,None]+self.DFS(root.right)
        else:
            return [root.val]

# N x N chess board, shortest hops needed by knight to reach (x1,y1) to (x2,y2)
# 
# (1) () () 
# () () ()
# () () (2)
#

''' 12.) Max Binary Tree - Medium'''

''' 13.) 230. Kth Smallest Element in a BST - Medium '''
# Inorder traversal w/ stack
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int, prevk=0) -> int:
        # Time: Traversing through the whole BST tree (graph w/ 2 possible child edges @ each node)
        #       O(n+e) where e is # of edges -> n-1
        #       O(n+n-1) -> O(n)
        #
        # Can NOT do this without helper function.. why? because we need a separate stack to hold value of k
        # stack: the last index is value k=1 LIFO, when we reach leaf node
        #        everytime we pop, we increment kCounter += 1
        #        compare kCounter == k, where kCounter is the len(stack)
        #        return root.val if kCounter
        stack = []
        
        def DFS(root,k):
            if not root:
                return False
            
            #go left
            if DFS(root.left,k):
                return True
            #root checks
            stack.append(root.val)
            if len(stack) == k:
                return True
            #go right
            if DFS(root.right,k): 
                return True
            
            return False
        
        DFS(root,k)
        return stack.pop() 

''' 14.) 310. Minimum Height Trees - Medium '''
#https://leetcode.com/problems/minimum-height-trees/ <- MST?

''' 15.) 98. Validate Binary Search Tree - Medium'''

''' 16.) 109. Convert Sorted List to Binary Search Tree - Medium '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        list_ref = self.convertToList(head)
        
        return self.helper(list_ref)
    
    def convertToList(self, head):
        list_ref = []
        while head != None:
            list_ref.append(head.val)
            head = head.next
            
        return list_ref
        
    def helper(self, list_ref):
        if not list_ref:
            return None
        
        if len(list_ref) == 1:
            return TreeNode(list_ref[len(list_ref)-1])
            
        mid = math.ceil(len(list_ref)//2)
        start = 0
        end = len(list_ref)
            
        root = TreeNode(list_ref[mid])
        root.left = self.helper(list_ref[start:mid])
        root.right = self.helper(list_ref[mid+1:end])
        
        return root

# Time = O(2n), Space = O(n)
# Tiime - Creating List (n) + Slice List (n) = O(2n)

''' 17.) 22. Generate Parentheses - Medium '''

''' 18.) 102. Binary Tree Level Order Traversal - Medium '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = [[root.val]]
        queue = collections.deque([])
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        return self.BFS(ans, queue)
    
    def BFS(self, ans, queue): 
        curr = []
        currNodes = []
        while queue:
            curr.append(queue[0].val)
            currNodes.append(queue.popleft())
            
        ans.append(curr)

        for node in currNodes:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if queue:
            self.BFS(ans, queue)
        
        return ans

# Short & Cleaned up version
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = collections.deque([root])
        while queue:
            currLevel = []
            for _ in range(len(queue)):
                currNode = queue.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            ans.append(currLevel)
            
        return ans

''' 19.) 207. Course Schedule - Medium '''
# Topological Sort & cycle detection
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # numCourse = 5, prerequisites = [[1,0],[2,0],[3,4], [4,2], [1,2]]
        #
        #       (1)
        #    </  ^
        # (0)    |    (3) ->  (4)
        #     <\ |             |
        #       (2)<-----------|
        # Pick 1
        # 1.) 1->0 (Check for outgoing arrows) None (Done)
        # 2.) 1 (Check for outgoing arrows) None (Done)
        # Done w/ 1. Pick 3
        # 1.) 3->4 (Check for outgoing arrows) 2
        # 2.) 4->2 (Check for outgoing arrows) 0,1
        # 3.) 2->0 (Done)
        # 4.) 2->1 (Done)
        # 5.) 2 (Check for outgoing arrows) None (Done)
        # 6.) 4 (Check for going) None (Done)
        # 7.) 3 (Check for outgoing) None (Done)
        # All Done = True, Not = False
        # Cycle = False
        # This approach failed 45/49 test cases..
        def DFS(visited, prerequisites, currNode):
            if currNode in visited: # 1 in []? no, 0 in [1]? no 2 in [1]? no 0 in [1,2]?
                return False
            for pair in prerequisites:
                if currNode == pair[0]: # 1=[1,0], 2=[2,0]
                    prerequisites.remove(pair) # 1-[[2,0],[3,4],[4,2],[1,2]], 2-[[3,4],[4,2],[1,2]]
                    if not DFS(visited+[currNode], prerequisites, pair[1]): # 1-True
                        return False

                visited.remove(currNode) #0
            return True

        return DFS([], prerequisites, prerequisites[0][0])

       # 0->10 do 10 before 0
       # 3->18
       # 5->5
       # 6->11
       # 11->14
       # 13->1
       # 15->1
       # 17->4 

    ''' 20.) 200. Number of Islands - Medium '''
    class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop thorugh the whole grid O(N) where N = mxn
        # start @ grid[0][0] then DFS up,down,right,left until we hit 0 (water) <- base case
        # Save each visited node in a list visited[]
        # keep an islandCount, after DFS everywhere for 1 (islands) increment by 1
        # Finish after looping through whole grid & return islandCount
        def DFS(grid,m_row,n_column,m_len,n_len):
            if m_row<0 or n_column<0 or m_row>m_len-1 or n_column>n_len-1 or grid[m_row][n_column] == "0": #or [m_row,n_column] in visited:
                return
                
            #visited.append([m_row,n_column])
            grid[m_row][n_column] = '0' # need to set to 0, otherwise will repeat
            DFS(grid,m_row,n_column+1,m_len,n_len) #right
            DFS(grid,m_row,n_column-1,m_len,n_len) #left
            DFS(grid,m_row+1,n_column,m_len,n_len) #up
            DFS(grid,m_row-1,n_column,m_len,n_len) #down
            
        m_row = len(grid)
        n_column = len(grid[0])
        visited = [] 
        islandCount = 0
        for row in range(m_row):
            for column in range(n_column):
                if grid[row][column] == '1':
                #if [row,column] not in visited and grid[row][column]!="0":
                    DFS(grid,row,column,len(grid),len(grid[0]))
                    islandCount += 1
                
        return islandCount
        
    ''' 21.) 1110. Delete Nodes And Return Forest - Medium '''
    class Solution:
        def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
            # DFS solution
            # forest = {TreeNode}
            # ans = [TreeNode]
            # helper function below
            # 1. inorder
            # 2. if to_delete.get(root.val), if node.left, forest.append(node.left) same w/ right & return None
            # loop while forest isnt null
            # ans.append(forest_Node)
            # after completing helper dfs, pop(0) forest set
            # return ans
            ans = []
            forest = collections.deque([root])
            def dfs(root):
                if not root:
                    return root
                if root.val in to_delete:
                    if root.left:
                        forest.append(root.left)
                    if root.right:
                        forest.append(root.right)
                    return None

                root.left = dfs(root.left)
                root.right = dfs(root.right)
                return root
            
            to_delete = set(to_delete) # difference: 11% -> 81%
            while forest:
                node = forest.popleft()
                if dfs(node):
                    ans.append(dfs(node))
            
            return ans
    
    ''' 22.) 1584. Min Cost to Connect All Points - Medium '''
    class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minimum spanning tree to find min cost 
        # kruskals algorithm: O(ELogV)
        # no cycles bc we want just all points connected (exactly one path between 2 points)
        # using union-find to connect points
        # 1. keep looping until numEdges == len(points)-1
        # 2. get all costs of every edge (manhattan distance) & store in min heap
        # 3. pop smallest from min heap
        # 4. union if both disjoint sets (not connected) else skip
        # 5. continue until (1)
        numEdges = 0
        numVertices = len(points)
        minCost = 0
        heap = []
        connected = {point: point for point in range(numVertices)}
        for pointOne in range(len(points)-1):
            for pointTwo in range(pointOne+1,len(points)):
                x = abs(points[pointOne][0] - points[pointTwo][0])
                y = abs(points[pointOne][1] - points[pointTwo][1])
                heapq.heappush(heap,(x+y,(pointOne,pointTwo)))
               
        while numEdges != numVertices-1:
            lowestEdge = heapq.heappop(heap)
            if self.find(connected.get(lowestEdge[1][0]), connected.get(lowestEdge[1][1])):
                continue
                
            minCost += lowestEdge[0]
            self.union(lowestEdge[1][0], lowestEdge[1][1], connected)
            numEdges += 1
            
        return minCost
    
    def union(self, firstVertex, secondVertex, connected):
        ogParent = connected[secondVertex]
        for vertex in connected:
            if connected[vertex] == ogParent:
                connected[vertex] = connected[firstVertex]
                    
        return connected
    
    def find(self, vertexOne, vertexTwo):
        if vertexOne == vertexTwo:
            return True

        return False
    
    ''' 23.) Network Delay Time - Medium (Dijsktra) '''
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's - single shortest path
        # source k -> target n
        # bfs to get neighbors
        # uses greedy approach
        visited = set()
        unvisited = set([x for x in range(1,n+1)])
        nxt = k

        # Create adj_list to know our neighbors
        # dk = {1: [lowest_dist_from_start, prev_vertex], ..}
        # adj_list = {src: [[target, dist], ..]}
        dk = {x: 0 if x == k else float('inf') for x in range(1,n+1)}
        adj_list = {}
        for time in times:
            if not adj_list.get(time[0]):
                adj_list[time[0]] = [[time[1], time[2]]]
                continue
                
            adj_list[time[0]].append([time[1], time[2]])
            
        
        while nxt:
            visited.add(nxt)
            unvisited.remove(nxt)
            largest_iteration = 0
            if adj_list.get(nxt):
                for adj in adj_list[nxt]:
                    adj_vertex, adj_dist = adj
                    curr_dist = dk[nxt]
                    # prevent going back to visited vertices
                    if adj_vertex in visited:
                        continue
                    # relaxation
                    print(nxt, adj_vertex, curr_dist+adj_dist, dk[adj_vertex])
                    if curr_dist+adj_dist < dk[adj_vertex]:
                        dk[adj_vertex] = curr_dist+adj_dist
                    
            # choose smallest adj_vertex
            nxt = None
            nxt_dist = float('inf')
            for vertex, vertex_low_dist in dk.items():
                if vertex in visited:
                    continue
                if vertex_low_dist < nxt_dist:
                    nxt_dist = vertex_low_dist
                    nxt = vertex
                       
        
        return -1 if unvisited else max(dk.values())
        
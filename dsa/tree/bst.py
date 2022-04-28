# Inorder, Preorder, Postorder
# DFS/BFS - Time: O(N)
#           Space: O(LogN) Auxilliary -> proportional to height of the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left=None
        self.right=None

class Tree:
    def __init__(self,root):
        self.root=Node(root)
        
    # root -> left -> right
    def preorder_print(self, start):
        preorder = []
        
        def preorder_get(start, preorder):
            if not start:
                return
        
            preorder.append(start.value)
            preorder_get(start.left, preorder)
            preorder_get(start.right, preorder)
            
        preorder_get(start, preorder)
        return "preorder: {}".format(preorder)
        
    # right -> left -> root
    def postorder_print(self, start):
        postorder = []
        
        def postorder_get(start, postorder):
            if not start:
                return
        
            postorder_get(start.right, postorder) 
            postorder_get(start.left, postorder)
            postorder.append(start.value)
            
        postorder_get(start, postorder)
        return "postorder: {}".format(postorder)
        
    # left -> root -> right
    def inorder_print(self, start):
        inorder = []
        
        def inorder_get(start, inorder):
            if not start:
                return
        
            inorder_get(start.left, inorder)
            inorder.append(start.value)
            inorder_get(start.right, inorder)
            
        inorder_get(start, inorder)
        return "inorder: {}".format(inorder)
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)


n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

t = Tree(n1)
print(t.preorder_print(n1))
print(t.postorder_print(n1))
print(t.inorder_print(n1))

### Maximum/Minimum Binary Tree Traversal ###

#Max
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        def helper(nums,root):
        #Get largest number in array & make root
            if not nums:
                return None
            
            if nums:
                root = TreeNode(max(nums))
            
            #Get subarrays
            root.left = helper(nums[0:nums.index(max(nums))], root)
            root.right = helper(nums[nums.index(max(nums))+1:len(nums)], root)
            
            return root
        
        root = TreeNode(0)
        return helper(nums,root)

### Basic DFS+BFS ###
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

nodes = []
n = 10
for x in range(n):
    nodes.append(Node(x))

for x in range(n//2-1):
    y = x+1
    nodes[x].left = nodes[y*2]
    nodes[x].right = nodes[y*2+1]

print(get_children(nodes[0]))

### DFS (Depth)  ###
def dfs(head):
    if not head.left and not head.right:
        children.append(head.val)

    if head.left:
        dfs(head.left)
    if head.right:
        dfs(head.right)

### BFS (Breadth) ###
def bfs(head):
    if not head.left and not head.right:
        children.append(head.val)
        return

    lvl = [head.left, head.right]
    while lvl:
        curr = lvl.pop(0)
        if curr.left:
            lvl.append(curr.left)
        if curr.right:
            lvl.append(curr.right)
        if not curr.left and not curr.right:
            children.append(curr.val)

#dfs(head)
def get_children(head):
    # recursive dfs
    children = []
    bfs(head)
    #dfs(head)
    return children
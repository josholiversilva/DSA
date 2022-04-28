#          (0)          (5)         ----> representative (root)
#         /   \           \
#       (3)   (1)         (2)
#       /
#     (4)

# union(0,5) -> make 5 child of 0 (y(x))
# find(1) -> recursively return the root (0)

class Node:
    def __init__(self, val, parent=None)
        self.val = val
        self.parent = parent 

def union(x: Node, y: Node) -> None:
    # Parent(find(y)) = find(x)
    # O(N)
    parentY = find(y)
    parentY.parent = find(x)

def find(curr: Node) -> Node:
    # find(x) = representative
    # O(N)
    if curr.parent == curr.val or not curr.parent:
        return curr

    return find(curr.parent)

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n0.left = n3
n0.right = n1
n3.left = n4
n5.right = n2


# ---------------------------------------------------------------
# Example: 547. Number Of Provinces - Medium
#
#     c1  c2  c3
# c1 [ 1,  1,  1 ]
# c2 [ 1,  1,  1 ]
# c3 [ 1,  1,  1 ]
        
#     c1 c2 c3 c4
# c1 [ 1, 0, 0, 1 ]
# c2 [ 0, 1, 1, 0 ]
# c3 [ 0, 1, 1, 1 ]
# c4 [ 1, 0, 1, 1 ]
        
# [-3, 0, 0]
        
# (1)->(4)
#       ^
# (2)->(3)
        
# c1,c2,c3,4
# [0,1,2,3]         -> [1,-4,1,0]
        
# cities list
# loop through isConnected (for x)
#   - find all connections for 1 (x) city
#       - current city -> parent, others are children
# loop through cities list
#   - count all that's < 0
class Solution:
    def find(self, curr_cities, city_idx):
        return city_idx if curr_cities[city_idx] < 0 else self.find(curr_cities, curr_cities[city_idx])
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        cities = [-1 for x in range(len(isConnected[0]))]
        for currIdx in range(len(cities)):
            for childIdx in range(currIdx+1,len(cities)):
                if isConnected[currIdx][childIdx]:
                    parentOfCurrIdx = self.find(cities, currIdx)
                    parentOfChildIdx = self.find(cities, childIdx)
                    
                    if parentOfCurrIdx == parentOfChildIdx:
                        continue
                    
                    cities[parentOfCurrIdx] += cities[parentOfChildIdx]
                    cities[parentOfChildIdx] = parentOfCurrIdx
        
        for idx in range(len(cities)):
            if cities[idx] < 0:
                provinces += 1
        
        return provinces

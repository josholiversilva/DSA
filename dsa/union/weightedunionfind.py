#   (1)                   (5)
#     \                  /   \
#      (2)             (7)   (6)
#        \                   
#         (3)        
#           \
#           (4)

# O(N) -> Using Quick-Find
# find(1) -> 1 step
# find(2) -> 2 steps     
# find(3) -> 3 steps
# find(4) -> 4 steps

class Node:
    def __init__(self, val, parent=None, weight=1):
        self.val = val
        self.parent = parent
        self.weight = weight

def union(x: Node, y: Node) -> None:
    pass

def find(node: Node) -> Node:
    pass

n1 = Node(1)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n5 = Node(5)
n6 = Node(6, n5)
n7 = Node(7, n5)

print(n1.weight)
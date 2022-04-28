INF = 99999

# Dijkstra
def dijkstra(graph):
    pass


# Floyd-Warshall Cycle Detection
# Reasoning
# l = length of loop
# k = distance from start of loop to where the behind & ahead ptrs met
# m = distance from head to start of loop
# b = # of revolutions inside loop for behind ptr
# a = # of revolutions inside loop for ahead ptr
#
# dist_behind = m + b * l + k
# dist_ahead = m + a * l + k
# 
# dist_ahead = 2 * dist_behind
# m + a * l + k = 2m + 2bl + 2k
# 0 = m + 2bl - al + k
# 0 = m + k + l(2b - a)
# -l(2b - a) = m + k
# l(a - 2b) = m + k 
# l(a - 2b) --> l is length of loop multiplied by an integer which will 
#               always be a multiple of loop
#               i.e. l = 4, l(a - 2b) = 4,8,12,16.. STARTING OF THE LOOP
# m + k = l * integer
# a = m + k (where behind & ahead ptrs meet)
# a = l * integer (exact value in the start of the loop)
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def floyd(head):
    behind, ahead = head, head 
    while behind.next and ahead.next:
        behind = behind.next
        ahead = ahead.next.next

        if behind == ahead:
            break

    behind = head

    while behind.next and ahead.next:
        behind = behind.next
        ahead = ahead.next

        if behind == ahead:
            break

    return ahead.val

s1 = Node(1)
s2 = Node(2)
s3 = Node(3)
s4 = Node(4)
s5 = Node(5)

s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = s3

print(floyd(s1))
# Bellman Ford

# Weighted
#        8>
#    (1) -- (3)
#  4>/    2>|  \3>
#   /       |   \
# (0)      (4)   (6)
#   \  9>/  |   /
#  8>\ /    | / 2>
#    (2) -- (5)
#         1>

graph = [
    [ 0 , 4 , 8 ,INF,INF,INF,INF],
    [INF, 0 ,INF, 8 ,INF,INF,INF],
    [INF,INF, 0 ,INF, 9 , 1 ,INF],
    [INF,INF,INF, 0 ,INF,INF, 3 ],
    [INF,INF,INF, 2 , 0 ,INF,INF],
    [INF,INF,INF,INF,INF, 0 , 2 ],
    [INF,INF,INF,INF,INF,INF, 0 ]
]

dijkstra(graph)
# MST: is a subset of the edges of a connected, edge-weighted undirected graph that 
#      connects all the vertices together, without any cycles and with the 
#      minimum possible total edge weight
#
# Num Vertices: V
# Num Edges: E
# No Edges in MST: (V-1)

# Greedy Algo
# Time -> O(NLogN) w/ Heap
# Maintain priority queue Q on V-S where v.key = min{w(u,v) | u element S}
# Initially Q stores V
    # s.key = 0 for arbitrary start vertex set
    # for v elemenv V-{s}; v.key = inf
# Until Q empty:
    # u = extract-min(Q) -> add u to S
    # for v element Adj[u]:
        # if v element Q:
            # w(u,v) < v.key:
                # v.key = w(u,v)
                # v.parent = u

# Time: O(V*E) -> O(N^2)
# Space: O(3V) -> O(N)
import time
def prims(graph):
    # Requirements
    # 1. Keep track of distance values from source: d
    # 2. Vertices included in mst: v
    # 3. Remember edges (parents): p
    d = [0 if x==0 else float('inf') for x in range(len(graph[0]))]
    v = set()
    p = [-1 for _ in range(len(graph[0]))]

    # Logical Steps
    # 1. Start at source -> 0
    # 2. Include Selected Node in mst set
    # 3. Relax/Compute all adj edges (Change Nodes Weight Value)
    # 4. Select Node With Min-Weight & Repeat

    # 1. Start at source -> 0
    n = 0
    while len(v) < len(graph[0]):
        print('---- node {} ----'.format(n))
        # 2. Include Node in MST Set
        v.add(n)
        
        # 3. Relax/Compute All Adj Edges
        for idx in range(len(graph[n])):
            print(idx, graph[n][idx])
            if idx in v or graph[n][idx] == 0:
                continue

            # Update Parent Node In p
            # Update Min Distance
            if d[idx] > graph[n][idx]:
                d[idx] = graph[n][idx]
                p[idx] = n
                print("Node: {} -> Parent: {}".format(idx, p[idx]))
            time.sleep(1)

        min_weight = float('inf')
        nxt_node = -1

        # 4. Select Node With Min Weight Not In MST
        print('\n-- d --')
        for idx in range(len(d)):
            print(idx, d[idx])
            if idx in v:
                continue

            if min_weight >= d[idx]:
                min_weight = d[idx]
                nxt_node = idx
        
        print("min_weight:{}\nnxt_node:{}\n\n".format(min_weight, nxt_node))
        n = nxt_node
        time.sleep(5)
        
    print(d)
    print(p)

graph = [
    [0, 4, 6, 0, 0, 0],
    [4, 0, 6, 3, 4, 0],
    [6, 6, 0, 1, 0, 0],
    [0, 3, 1, 0, 2, 3],
    [0, 4, 0, 2, 0, 7],
    [0, 0, 0, 3, 7, 0]
]
prims(graph)
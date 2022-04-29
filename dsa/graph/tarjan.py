# Time: O(V+E)

# Strongly Connected Component
# Self-contained cycles within a directed graph
# Every vertex in given cycle can reach every other vertex in same cycle

# Stack invariant: Set of valid nodes from which to update low-link values from
# Update on-the-fly during DFS

def create_adj_list(graph):
    adjList = {}
    for points in graph:
        src, tgt = points
        if adjList.get(src):
            adjList[src].append(tgt) 
        else:
            adjList[src] = [tgt]

    return adjList

def dfs(curr, adjList, stack, ids, lows, visited, onStack):
    ids[curr] = curr
    lows[curr] = curr
    onStack[curr] = True
    stack.append(curr)
    visited[curr] = True
    for x in adjList.get(curr, []):
        if not visited[x]:
            dfs(x, adjList, stack, ids, lows, visited, onStack)
        if onStack[x]:
            lows[curr] = min(lows[x], lows[curr])

    # only pop from stack if start of scc
    if ids[curr] == lows[curr]:
        while stack:
            node = stack.pop()
            onStack[node] = False
            if curr == node:
                break

def tarjan(n, graph):
    ids = [0]*n
    lows = [0]*n
    visited = [False]*n
    stack = []
    onStack = [False]*n
    adjList = create_adj_list(graph)

    for x in range(n):
        if not visited[x]:
            dfs(x, adjList, stack, ids, lows, visited, onStack)

    return lows
    
graph = [[0,1], [0,2], [1,3], [2,3], [2,0], [3,4], [3,5], [4,1,], [4,5], [4,6], [5,7], [6,5], [7,6]]
print(tarjan(8, graph))

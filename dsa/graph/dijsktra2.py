# undirected graphs 
cities = ['A', 'B', 'C', 'D', 'E']
graph = [
    ['A', 'B', 6],
    ['A', 'D', 1],
    ['B', 'D', 2],
    ['B', 'E', 2],
    ['B', 'C', 5],
    ['D', 'E', 1],
    ['E', 'C', 5]
]

cities2 = ['A', 'B', 'C', 'D', 'E', 'F']
graph2 = [
    ['A', 'B', 2],
    ['A', 'C', 4],
    ['B', 'C', 1],
    ['B', 'D', 7],
    ['C', 'E', 3],
    ['E', 'D', 2],
    ['D', 'F', 1],
    ['E', 'F', 5]
]

# O(N^2)
def dijsktra(graph, cities):
    # Vertex, Shortest Dist from A, Prev Vertex
    # {A: [0, -]}
    # {B: []}
    adj_list = {}
    for vertexRow in graph:
        if not adj_list.get(vertexRow[0]):
            adj_list[vertexRow[0]] = [[vertexRow[1], vertexRow[2]]]
        else:
            adj_list[vertexRow[0]].append([vertexRow[1], vertexRow[2]])

        if not adj_list.get(vertexRow[1]):
            adj_list[vertexRow[1]] = [[vertexRow[0], vertexRow[2]]]
        else:
            adj_list[vertexRow[1]].append([vertexRow[0], vertexRow[2]])
        
    res = {vertex: [0,None] if vertex == 'A' else [float('inf'),None] for vertex in cities}
    print(res)
    print(adj_list)
    visited = []
    curr = cities[0]
    
    # Loop Through All Vertices
    while len(visited) < len(cities):
        visited.append(curr)
        next_smallest = [None, float('inf')]
        print('---- {} ----'.format(curr))

        # Examine Unvisited Neighbors
        for adj_vertices in adj_list[curr]:
            curr_dist, _ = res[curr]
            adj_vertex, adj_dist = adj_vertices

            if adj_vertex in visited:
                continue

            print(curr, curr_dist, adj_vertex, adj_dist)
            # Relaxation (Update Costs to Smaller Distance)
            if curr_dist+adj_dist < res[adj_vertex][0]:
                res[adj_vertex][0] = curr_dist+adj_dist
                res[adj_vertex][1] = curr
    
            next_smallest = [adj_vertex, adj_dist] if adj_dist < next_smallest[1] else next_smallest
        curr = next_smallest[0]
    print(res)

# O(NLogN)
import heapq
def dijsktra_heap(graph, src, dst, n):
    heap = []
    dist = [float('inf')]*n
    visited = set()

    heapq.heappush(heap, [0, src])
    dist[src] = 0

    adj_list = {}
    for edge in graph:
        s, d, w = edge
        if (adj_list.get(s)):
            adj_list[s].append([d, w])
        else:
            adj_list[s] = [[d, w]]

    while heap:
        curr_weight, curr_node = heapq.heappop(heap)

        if curr_node in visited or not adj_list.get(curr_node):
            continue
        visited.add(curr_node)

        for edge in adj_list[curr_node]:
            nxt_node, nxt_weight = edge
            if curr_weight+nxt_weight < dist[nxt_node]:
                dist[nxt_node] = curr_weight + nxt_weight
                heapq.heappush(heap, [curr_weight+nxt_weight, nxt_node])

    return dist[dst]

# dijsktra(graph, cities)
# dijsktra(graph2, cities2)

# src, dst, weight
graph = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
n = 4
print(dijsktra_heap(graph, src, dst, n))
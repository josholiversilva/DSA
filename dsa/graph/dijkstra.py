# Dijkstra's algorithm 
# Time: O(V*E) -> simple implementation
# Time: O(E*Log(V)) -> using min heap
#                 12
#        (B)-----------------     (H)
#     5/    6\              |    /    \ 
# (A)         (D)           |   / 5     \ 2
#    \      /     \2       3|  /          \
#  10 \   /2       (E) --- (F) --- (G) --- (I)
#      \ /                  |   8       1
#      (C)------------------|
#               3
import time

class Node:
    def __init__(self, nodeLetter, adjacencyMap={}):
        self.nodeLetter = nodeLetter
        self.adjacencyMap = adjacencyMap

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
A.adjacencyMap = {B: 5, C:10}
B.adjacencyMap = {D: 6, F:12}
C.adjacencyMap = {D: 2, F:3}
D.adjacencyMap = {E: 2}
E.adjacencyMap = {F: 3}
F.adjacencyMap = {H: 5, G: 8}
G.adjacencyMap = {I: 1}
H.adjacencyMap = {I: 2}

# Simple Implementation O(N^2)
def dijkstra(graph, sourceNode, destNode):
    vertexMap = {vertex: {'shortestPath': float('inf'), 'prev': None} for vertex in graph}
    vertexMap[sourceNode] = {'shortestPath': 0, 'prev': None}

    visited = set()
    nextNode = sourceNode
    shortest = float('inf')

    while graph:
        currNode = graph.pop(graph.index(nextNode))
        visited.add(currNode)

        for child,cost in currNode.adjacencyMap.items():
            if child not in visited:
                vertexMap[child] = {'shortestPath': min(vertexMap[currNode]['shortestPath']+cost,vertexMap[child]['shortestPath']), 'prev': currNode}
                print(child.nodeLetter + " Cost: " + str(min(vertexMap[currNode]['shortestPath']+cost,vertexMap[child]['shortestPath'])))

        for vertex in vertexMap:
            if vertex not in visited and shortest >= vertexMap[vertex]['shortestPath']:
                nextNode = vertex
                shortest = vertexMap[vertex]['shortestPath']

        print("Next Node: " + nextNode.nodeLetter)

        shortest = float('inf')

    for node,cost in vertexMap.items():
        print(node.nodeLetter + ' - ' + str(cost['shortestPath']))

    #shortestPath = [destNode.nodeLetter]
    #prev = vertexMap[destNode]['prev']
    #while prev:
    #    shortestPath.append(prev.nodeLetter)
    #    prev = vertexMap[prev]['prev']

    #shortestPath.reverse()
    #shortestPath = '->'.join(shortestPath)
    #print("Shortest Path: " + shortestPath)
    print("Cost From " + str(sourceNode.nodeLetter) + " -> " + str(destNode.nodeLetter) + ": " + str(vertexMap[destNode]['shortestPath']))

# Heap Implementation
# Create hashmap: O(V)
# Create list for heap: O(E)
# Convert list back to hashmap: O(E)
# Heapify: O(VLogV)
# Time: O(E+2V+VLogV) -> O(NLogN)
import heapq
import collections
def dijkstraFast(graph, sourceNode, destNode):
    vertices = createNetwork(graph, sourceNode) # O(V)
    visited = set()

    while vertices:
        nodeInfo = getMinNodeFromVertices(vertices) # O(V)
        vertices = removeNodeInVertices(nodeInfo, vertices) # O(VLogV)
        visited.add(nodeInfo)

        currNode = nodeInfo[0]
        currCost = nodeInfo[1]
        for child,cost in currNode.adjacencyMap.items(): # O(E)
            if child in vertices: #O(1)
                vertices[child] = min(currCost+cost, vertices[child])
                print(child.nodeLetter + ' - ' + str(vertices[child]))

    destCost = getTargetCost(destNode, visited)

    print("Cost From " + sourceNode.nodeLetter + " -> " + destNode.nodeLetter + ': ' + str(destCost))

def createNetwork(graph, sourceNode):
    vertices = {}
    for x in range(len(graph)):
        if graph[x] == sourceNode:
            vertices[graph[x]] = 0
        else:
            vertices[graph[x]] = float('inf')

    return vertices

# return tuple: (node,cost)
def getMinNodeFromVertices(vertices):
    verticesList = [(value,key) for key,value in vertices.items()]
    heapq.heapify(verticesList)
    minNode = heapq.heappop(verticesList)

    return (minNode[1], minNode[0])

# takes node
def removeNodeInVertices(node, vertices):
    newVertices = {}
    for vertex,cost in vertices.items():
        if node[0] == vertex:
            continue
        newVertices[vertex] = cost

    return newVertices

def getTargetCost(destNode, visited):
    cost = -1
    for visit in visited:
        if visit[0] == destNode:
            cost = visit[1]

    return cost


graph = [A,B,C,D,E,F,G,H,I]
print("Simple Implementation")
dijkstra(graph, A, I)
print('')


graph = [A,B,C,D,E,F,G,H,I]
print("Heap Implementation")
dijkstraFast(graph, A, I)

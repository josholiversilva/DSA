from topsort import sortNodes
from cycle_detect import detectedCycle
from adjacencies import getAdjacencies
from mst import getMST

if __name__ == __main__:
    if detectedCycle():
        return 'Detected Cycle, Unable to perform topsort/DP..'

    sortedNodes = sortNodes()
    adjList = getAdjacencies(sortedNodes)
    mst = getMST()
    

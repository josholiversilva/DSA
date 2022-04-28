values = [60,100,120]
weights = [10,20,30]
W = 50

def knapsack(values, weights, W):
    #                   Knapsack Weight=50
    #                   0   1   2   3   4   5
    #
    # None              0   0   0   0   0   0
    # v1=60, w1=10      0   6   6   6   6   6
    # v2=100,w2=20      0   6   10  16  16  16
    # v3=120,w3=30      0   6   12  16  18  22
    #
    # v3: 22!=16, move w3=30 diagonal left (CHOSEN)
    # v2: 10!=6, move w2=20 diagonal left (CHOSEN)
    # v1: 0==0, move up (NOT CHOSEN)
    #
    # 1.) Create 2d knapsack array
    # 2.) Traverse & compare
    # 3.) Return chosen values sum
    knapsackArr = [[0]*(W//10)]
    for row in range(len(values)):
        knapSackRow = []
        for column in range(W//10):
            itemAbove = knapsackArr[row][column]
            itemValue = values[row]//10
            itemWeight = weights[row]//10

            # 1.) append New value if > itemAbove
            # 2.) append itemAbove if > new value
            # 3.) append new value + itemAbove if weight>=knapsack weight
            if itemWeight <= column:
                knapSackRow.append(itemValue) if itemValue > itemAbove else knapSackRow.append(itemAbove)
            # Get Value from Row Above
            else:
                knapSackRow.append(itemAbove)
        knapsackArr.append(knapSackRow)
    print(knapsackArr)
            
knapsack(values, weights, W)
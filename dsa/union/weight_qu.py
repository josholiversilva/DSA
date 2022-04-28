class WeightedQU():
    def __init__(self, N):
        self.id = []
        for x in range(0,N):
            self.id.append(x)
    
    def root(self, i):
        count = 0
        while i != self.id[i]: #2 != 3 (2 is the child of 3)
            i = self.id[i] # go to 3
            count +=1 # depth of root
        return i, count #returns a tuple: (input, # of parents)
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i[0] == j[0]:
            return
        if i[1] < j[1]:
            self.id[i[0]] = j[0]
        else:
            self.id[j[0]] = i[0]

qu = WeightedQU(10)
qu.union(4,3)
qu.union(3,8)
print(qu.connected(3,5))
qu.union(6,5)
print(qu.connected(4,8))
print(qu.connected(8,4))
print(qu.connected(1,4))
qu.union(9,4)
qu.union(2,1)
qu.union(5,0)
qu.union(7,3)
qu.union(7,2)
qu.union(6,3)

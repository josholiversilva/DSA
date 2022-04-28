# Time Complexity: O(N) Access, Memory: O(N^2)
# Reason: In order to find union (2 loops, to set the root of the number & linearly find the )
# Preface: Index & Value must both be equal to each other..
class QuickUnion():
    def __init__(self, N):
        self.id = []
        for x in range(0,N):
            self.id.append(x)

    def root(self, i):
        while i != self.id[i]: #2 != 3 (2 is the child of 3)
            i = self.id[i] # go to 3
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        self.id[self.root(p)] = self.root(q)
    
qu = QuickUnion(9)
qu.union(3,4)
qu.union(4,5)
print(qu.connected(3,5))
qu.union(5,8)
print(qu.connected(4,8))
print(qu.connected(8,4))

# Use the index of the array, every time we connect (x,y) x to y we make x's index equal the index/value of y.
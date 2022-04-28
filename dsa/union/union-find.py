# Quick-Find Algorithm
# Find: Check if p & q have same id
# Union: Merge comp containing p & q (O(1) best O(N) avg/worst)
# Change all entries whose id equals id[p] & id[q]
class QuickFind():
    def __init__(self, N):
        self.id = [] # array of integers
        for x in range(0,N):
            self.id.append(x)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p] # Initialized to Avoid loop overwrites
        qid = self.id[q] # Initialized to Avoid loop overwrites

        # Go through whole list & replace qid (root) with index of p
        # This will find any index with value of inserted pid
        for i in range(0,len(self.id)):
            if(self.id[i]==pid):
                self.id[i] = qid

    def getID(self):
        return self.id

qf = QuickFind(9)
qf.union(5,2)
qf.union(1,3)
qf.union(2,1)
qf.union(3,0)
print(qf.connected(1,3))
print(qf.connected(1,5))
print(qf.getID())
qf.union(3,5)
qf.union(5,0)
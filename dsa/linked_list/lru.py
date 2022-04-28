class Node:
    def __init__(self, key, val, nxt=None, before=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.before = before

# headPtr -> (2) <-> (1) <- tailPtr

class LRU:
    def __init__(self, size):
        self.size = size
        self.cacheSize = 0 
        self.cache = {} # key: (val, nodeAddr)
        self.headPtr = None
        self.tailPtr = None

    def moveNodeToFront(self, node):
        if self.headPtr != node:
            node.before.nxt = node.nxt 
            if node.nxt:
                node.nxt.before = node.before
            else:
                self.tailPtr = node.before

            self.headPtr.before = node
            node.nxt = self.headPtr
            node.before = None
            self.headPtr = node

    def pushNodeToFront(self, key):
        self.headPtr.before = self.cache[key][1]
        self.cache[key][1].nxt = self.headPtr
        self.headPtr = self.cache[key][1]

    def removeLeastRecent(self):
        del self.cache[self.tailPtr.key]
        beforeNode = self.tailPtr.before
        if self.tailPtr.before:
            self.tailPtr.before.nxt = None
            self.tailPtr.before = None
        self.tailPtr = beforeNode

    def get(self, key):
        if self.cache.get(key):
            self.moveNodeToFront(self.cache[key][1])
            return self.cache[key][0]

        return -1 

    def put(self, key, val):
        # not a new node
        if self.cache.get(key):
            node = self.cache[key][1]
            self.moveNodeToFront(self.cache[key][1])
            del self.cache[key]
            self.cache[key] = (val,node)
            self.cache[key][1].val = val
        elif self.cacheSize < self.size:
            self.cache[key] = (val, Node(key, val))
            # initialize 
            if len(self.cache) == 1:
                self.headPtr = self.cache[key][1]
                self.tailPtr = self.cache[key][1]
            # push to front
            else:
                self.pushNodeToFront(key)

            self.cacheSize += 1
        else:
            self.cache[key] = (val, Node(key, val))
            self.removeLeastRecent()
            self.pushNodeToFront(key)
        
    def printLL(self):
        head = self.headPtr
        chron = []
        while head:
            chron.append('( {} )'.format(head.val))
            head = head.nxt

        output = 'head -> ' + ' <-> '.join(chron) + ' <- tail'
        print(output)
        print(self.cache)

size = input('Enter cache size:\n')
s = LRU(int(size))
while True:
    print()
    print()
    putGet = input('Enter P (Put) or G (Get):\n').lower()
    if putGet != 'p' and putGet != 'g':
        continue
    
    if putGet == 'p':
        key,val = input('Enter Key,Val integer pair:\n').split(',')
        s.put(int(key), int(val))
    else:
        key = input('Enter Key integer:\n')
        s.get(int(key))
    
    s.printLL()
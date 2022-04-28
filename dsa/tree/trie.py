class Node:
    def __init__(self, val, children=[], isCompleteWord=False):
        self.val = val 
        self.children = children # char: Node
        self.isCompleteWord = isCompleteWord 

# My way with array
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None) # char: Node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for charIndex in range(len(word)):
            found = False
            for child in curr.children:
                if child.val == word[charIndex]:
                    node = child
                    found = True
                    
            if not found:
                node = Node(word[charIndex])
                curr.children = curr.children+[node]
                
            curr = node
                
        curr.isCompleteWord = True
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for char in word:
            found = None
            for child in curr.children:
                if child.val == char:
                    found = child
                    
            if not found:
                return False
            
            curr = found
        
        if not curr.isCompleteWord:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for char in prefix:
            found = None
            for child in curr.children:
                if child.val == char:
                    found = child
            
            if not found:
                return False
            
            curr = found
            
        return True

# using dict - much more elegant
class TrieDict:

    def __init__(self):
        self.T = {}
        
    def insert(self, word):
        node = self.T
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None
    
    def match(self, seq, prefix):
        node = self.T
        for c in seq:
            if c not in node:
                return False
            node = node[c]
        return True if prefix else '$' in node
    
    def search(self, word):
        return self.match(word, False)

    def startsWith(self, prefix):
        return self.match(prefix, True)

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = 'hello'
prefix = 'he'
obj.insert(word)
print(obj.search(word))
print(obj.startsWith(prefix))
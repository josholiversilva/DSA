# (Problem-Specific) Things to Keep in Mind

YOUR ORIGINAL IDEA IS ALWAYS ALMOST 100% WRONG, ITERATE IDEA & THINK OF CAVEATS - ITS NOT THAT SIMPLE.

1. Is the input set sorted? Will sorting help?
2. READ the INPUT VALUES & Understand the constraints. Use the inputs values as efficiently as possible.
3. BST means left < root < right
4. Inside function can use the initialized variables in outer function.
5. DFS(root.left) from root node, means all compound returns from subtrees on the left, likewise for DFS(root.right) for right
6. Will Greedy Work? Will Recursion work in given time? Dynamic Programming?
7. Stop. Think. Plan. Execute.

# (Function-Specific)
1. self.DFS(root.left,returnValue+[root]) <- This "returnValue+[root]" appends to root list all the way down, after base case it inherently pops back up
2. return root.val+self.DFS(root.left)+self.DFS(root.right) <- Returns the return values from topmost node. All self.DFS() is dependent on base case. MUST return values in order to get it back up the stack.
3. if self.DFS(root.left) or self.DFS(root.right) <- This does post-order traversal (left-right-root)
4. KTH of ANYTHING is heap or sliding window or dp
5. POP the index, REMOVE the value
6. SET (add - O(1)) is faster than LIST (append - O(N)).. Set - Adds independent to num items, List - tests membership linear in size of list
7. append(1) -> [2,3,1] end, insert(0,1) -> [1,2,3] start
8. Recursion -> return same data type in base case & end. Try to create situation where can use data type as another type (T/F)
9. Linked List -> "In Place", change pointers rather than modifying values i.e. insertion sort in linked list
10. Subarray To Equal Target value - hashmap
11. Subarray To Find Min/Max operational (add/multiply/sub/divide) value - max/min linear traversals
12. Sets have NO Index, uses keys to find/insert/delete
13. x^x = 0, 0^y = y

chr(97) -> convert to string ASCII value
ord('a') -> convert to integer ASCII value
.is_digit()
.is_integer() -> check if a float is an int or ans % 1 == 0
.isalnum()
filter(function,s) i.e. filter(str.isalnum, s)
._heapify_max(), ._heappop_max()
sorted(function,key,reverse) i.e. sorted(set(foo),key=foo.index)

collections.deque(maxlen=n)

to loop diagonally (dp)
for x in range(len(s)):
    for row in range(len(s)-x):
        col = row+x
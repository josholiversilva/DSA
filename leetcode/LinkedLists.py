''' 1.) Add Two Numbers - Medium '''
# Input - [ListNode(1), ListNode(2), ListNode(3)]
#         [ListNode(3), ListNode(4), ListNode(9)]
# Output - [ListNode(2), ListNode(6), ListNode(2), ListNode(1)]
# Output - 321 + 941 = 1262

# Tail Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionAddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toint(node: ListNode):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n // 10)
            return node 
        return tolist(toint(l1)+toint(l2))

# O(n) Time Complexity Recusion - Function is called n times before reaching the base
# O(n) space - We have 
# Thought Process: We add two numbers starting @ ones place -> tens place -> hundredths place etc..
# Starting with ListNodes, we need to convert both (l1 & l2) into ints with a recursive function
# toint - go down all the way to base with return, until a node doesn't exist
# @ base, we recursively go up the stack by adding the current value with the previous value x 10
# tolist - take the ones place digit (912%10=2), make as top-level ListNode & connect with node.next
# where .next is the next digit as long as n>9: (912//10=91 [rounded with //]) so node.next=(tolist(91)) & repeat

''' 2.) Reverse a Linked List - Easy'''

'''Recursion Review'''
n = 3
# Made before it performs it's own task
def headRec(n):
    if n==0:
        return 1
    headRec(n-1) # appands to stack [3-1, 2-1, 1-1 -> return 1]
    print(n) # reads from stack (last value -> first) prints 1,2,3
    return n # returns stateless values (last value -> first) return 1,2,3 (3 overwrites all other return values)

# Made at end of function after performing own task
def tailRec(n):
    if n==0:
        return 1
    print(n) # print 3,2,1
    return tailRec(n-1) # Appends to stack until base case is returned (3-1,2-1,1-1 -> returns 1) returns top of stack 1
    
print(headRec(3))
print(tailRec(3))

'''Recursive Solution - Tail Recursion (Stateful & return base case value)'''
def reverse(head, previous=None):
    if head == None:
        return head # return last node (5)
    
    n = head.next # n = ListNode(2)
    head.next = previous # ListNode(1).next = None
    return reverse(n, head) # Stack [reverse(1), reverse(2).. reverse(5)] # returns last value 5 after all pointer switch ops

'''Iterative Solution'''
def reverse(head):
    prev = None
    ptr = head
    while ptr != None:
        tmp = prev
        prev = ptr
        prev.next = prev
        ptr = ptr.next
    
    return prev

''' 19. Remove Nth Node From End of List - Medium '''
# Using Stack (One-Pass)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next == None:
            return None
        
        stack = []
        while head != None:
            stack.append(head)
            head = head.next
        
        pop_index = len(stack)-n
        stack[pop_index].next = None
        
        # Gotta be careful with lists & index bounds
        if (pop_index == len(stack)-1):
            stack[pop_index-1].next = None   
        elif pop_index > 0 and pop_index < len(stack)-1:
            stack[pop_index-1].next = stack[pop_index+1]
            
        stack.pop(pop_index)
        
        return stack[0]

# Using two pointers left is always behind by 2 (right)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Start 1 Node before
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # two pointers
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        
        # return original head
        return dummy.next

''' 20.) 147. Insertion Sort List - Medium '''
# Using two pointers with dummy
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(float('inf'))
        dummy.next = head
        pre1 = head
        ptr1 = head.next
            
        while ptr1:
            pre2 = dummy
            ptr2 = dummy.next
            
            # From the beginning, go until ptr1 (current node to compare)
            # is greater than the previous 4->5->2
            # pre2 = dummy (inf)
            # ptr2 = dummy.next (4)
            # ptr1 = 2
            while ptr2.val <= ptr1.val and ptr2 != ptr1:
                pre2 = ptr2
                ptr2 = ptr2.next
           
            # if equal then we found that all previous is less than.
            # it belongs in the right spot, so continue: 4->5->6
            # pre2 = 4
            # ptr2 = 5
            # ptr1 = 6
            if ptr2 == ptr1:
                pre1 = ptr1
                ptr1 = ptr1.next

            # otherwise we need to put ptr1 (curr node) in right spot
            # which is before ptr2 (broke at this point in while)
            # and after pre2 (lags behind ptr2 by one value)
            else:
                pre2.next = ptr1 # value smaller than current node, set that ptr to current node
                tmp = ptr1.next # save the next ptr for current node
                ptr1.next = ptr2 # current node points to larger node (known by while loop)
                ptr1 = tmp # continue on: move ptr1 to next node to compare (left-hand side is sorted now)
                pre1.next = ptr1 # continue on: pre1 should always lag behind ptr1 by one 
                
        return dummy.next
      
# Sort: O(nlogn) -> n to create heap, logn to heapify
# Space: O(1) -> arranged data in place
# Insertion: O(logn)
# Pop/Remove: Max/Min - O(1) Worst - O(logn)
# Peek: O(1)
# Space: O(1)
class max_heapify:
    def Heap(self, h):
        start = int(len(h)/2) #start at the lowest child

        while start >= 1:
            self.SiftDown(start)
            start -= 1

    def SiftDown(self, start):

        #initialize values
        end = len(h)
        root = start
        right_child = root * 2 + 1
        left_child = root * 2

        while (right_child-1 <= len(h)) or (left_child-1 <= len(h)):

            #determine which one is greater then switch the greater one with the root if greater than root as well
            compare = ''
            
            #get right_child if exists
            if right_child<=end:
                if h[right_child-1] >= h[left_child-1]:
                    compare = 'right_child'
                elif h[right_child-1] <= h[left_child-1]:
                    compare = 'left_child'
            
            #otherwise get left_child (there will always be a left child given start value)
            else:
                compare = 'left_child'
            
            #switch right_child with root if child is greater
            if compare == 'right_child':
                if h[root-1] <= h[right_child-1]:
                    h[root-1],h[right_child-1] = h[right_child-1],h[root-1] # switch root and right child
                   
                    #reinitialize values & compare switched root's children
                    root = right_child
                    if root * 2 <= len(h): #check if left root exists (if none there's no children)
                        right_child = root * 2 + 1
                        left_child = root * 2
                    else:
                        return
                else:
                    return

            
            #otherwise switch left_child with root if child is greater
            else:
                if h[root-1] <= h[left_child-1]:
                    h[root-1],h[left_child-1] = h[left_child-1],h[root-1] # switch root and left child
                    
                    
                    #reinitialize values & compare switched root's children (if none there's no children)
                    root = left_child
                    if root * 2 <= len(h): #check if left root exists
                        right_child = root * 2 + 1
                        left_child = root * 2
                    else:
                        return
                else:
                    return


if __name__ == '__main__':
    h = [1, 3, 36, 2, 19, 25, 100, 17, 7, 200, 5, 3000, 21, 392, 20]
    print("Before heapify - " + str(h))
    t = max_heapify()
    t.Heap(h)
    print("After heapify - " + str(h))

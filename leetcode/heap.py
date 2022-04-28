''' 1.) 1046. Last Stone Weight - Easy '''
# NOTE ABOUT HEAPS
# python default in heapq == minheap
# use heapq._heapify_max() for maxheap
# heappop always pops min most heap elemenet
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # using max heap to get 2 heaviest stones
        # continue until len(stones) == 1
        # time: O(n) [Heapify] + O(2n) [Get 2 largest stones] = O(3n) = O(N)
        while len(stones) > 1:
            heapq._heapify_max(stones)
            first,second = heapq.nlargest(2,stones)
            if first == second:
                stones.remove(first)
                stones.remove(second)
            else:
                largest = stones.pop(stones.index(first))
                secondLargest = stones.pop(stones.index(second))
                heapq.heappush(stones,largest-secondLargest)
                
        if len(stones) == 1:
            return stones[0]
        
        return 0
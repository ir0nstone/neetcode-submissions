from heapq import heapify_max, heappop_max, heappush_max

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)

        while len(stones) > 1:
            x = heappop_max(stones)
            y = heappop_max(stones)

            if x == y:
                continue
            
            heappush_max(stones, x-y)
        
        return stones[0] if len(stones) == 1 else 0

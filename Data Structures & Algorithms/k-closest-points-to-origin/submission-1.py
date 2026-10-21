from heapq import heappop_max, heappush_max

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            # no need to sqrt as comparing
            dist = p[0]**2 + p[1]**2
            heappush_max(heap, (dist, p[0], p[1]))

            if len(heap) > k:
                heappop_max(heap)

        return [[x[1], x[2]] for x in heap] 

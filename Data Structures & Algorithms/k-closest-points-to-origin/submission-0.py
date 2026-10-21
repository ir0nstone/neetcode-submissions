from heapq import heappop_max, heappush_max

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        closest = defaultdict(list)

        for p in points:
            # no need to sqrt as comparing
            dist = p[0]**2 + p[1]**2
            heappush_max(heap, dist)
            closest[dist].append(p)

            if len(heap) > k:
                closest[heappop_max(heap)].pop()

        ans_points = []

        for ps in closest.values():
            ans_points += ps

        return ans_points

from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)

        for _ in range(len(nums) - k):
            heappop(self.heap)
        
        print(self.heap)

        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) == 0:
            self.heap.append(val)
        elif val > self.heap[0]:
            heappush(self.heap, val)

            if len(self.heap) > self.k:
                heappop(self.heap)
        
        return self.heap[0]

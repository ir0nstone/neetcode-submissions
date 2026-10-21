from heapq import heappop_max, heappush_max
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        heap = []

        for task, cnt in freq.items():
            heappush_max(heap, (cnt, task))

        # (time_end, tasks_left, task_id)
        cooldowns = deque([])

        i = 0

        while heap or cooldowns:
            if cooldowns and cooldowns[0][0] == i:
                _, tasks_left, task_id = cooldowns.popleft()
                heappush_max(heap, (tasks_left, task_id))
            
            if not heap:
                i = cooldowns[0][0]
                continue
            
            task_cnt, task_id = heappop_max(heap)

            if task_cnt > 1:
                cooldowns.append((i+n+1, task_cnt-1, task_id))
            
            i += 1
        
        return i

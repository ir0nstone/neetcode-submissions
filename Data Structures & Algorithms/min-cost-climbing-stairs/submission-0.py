mem = {}

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        mem = {
            l-1: cost[l-1],
            l-2: cost[l-2]
        }

        def recurse(i):
            if i in mem:
                return mem[i]
            
            res = cost[i] + min(recurse(i+1), recurse(i+2))
            mem[i] = res
            return res
        
        return min(recurse(0), recurse(1))

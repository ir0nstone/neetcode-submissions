class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        mem = [-1] * len(nums)

        def dfs(n):
            if n >= len(nums):
                return 0
            
            if mem[n] != -1:
                return mem[n]

            res = max(nums[n] + dfs(n+2), dfs(n+1))
            mem[n] = res
            return res
        
        return dfs(0)
        
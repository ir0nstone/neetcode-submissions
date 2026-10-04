class Solution:
    def old_rob(self, nums: List[int]) -> int:
        print(nums)

        if not nums:
            return 0
        
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

    def rob(self, nums: List[int]) -> int:
        return max(self.old_rob(nums[1:]), nums[0] + self.old_rob(nums[2:-1]))

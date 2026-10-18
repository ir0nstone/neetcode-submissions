class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # store LIS from index i onwards
        mem = {len(nums)-1: 1}

        def recurse(i):
            if i in mem:
                return mem[i]

            pos = []

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    pos.append(recurse(j))
            
            mem[i] = 1 + max(pos) if pos else 1
            return mem[i]

        return max(recurse(i) for i in range(len(nums)))

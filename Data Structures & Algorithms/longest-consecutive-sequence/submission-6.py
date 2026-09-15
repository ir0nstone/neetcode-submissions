class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0

        vals_seen = set(nums)

        starts = set()
        for val in vals_seen:
            if val-1 not in vals_seen:
                i = 0
                while val+i in vals_seen:
                    i += 1
                
                maxlen = max(maxlen, i)

        return maxlen
        
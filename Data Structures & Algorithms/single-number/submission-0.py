class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        storage = 0

        for n in nums:
            storage ^= n
        
        return storage
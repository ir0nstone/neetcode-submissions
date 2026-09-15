class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        results = {}

        valid = []

        for i, n in enumerate(numbers):
            if n in results:
                valid.append([results[n], i])

            results[target-n] = i
        
        return valid

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        vals = []

        for idx, num in enumerate(nums):
            for left, right in self.twoSum(nums[idx+1:], -num):
                triplet = [num, nums[left+idx+1], nums[right+idx+1]]
                if triplet not in vals:
                    vals.append(triplet)
        
        return vals

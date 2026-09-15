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
        ctr = Counter(nums)
        nums = []

        for val in ctr:
            for _ in range(min(ctr[val], 3)):
                nums.append(val)
        
        nums.sort()

        seen = set()
        vals = []

        for idx, num in enumerate(nums):
            for left, right in self.twoSum(nums[idx+1:], -num):
                triplet = (num, nums[left+idx+1], nums[right+idx+1])
                
                if triplet not in seen:
                    vals.append(list(triplet))
                    seen.add(triplet)
        
        return vals

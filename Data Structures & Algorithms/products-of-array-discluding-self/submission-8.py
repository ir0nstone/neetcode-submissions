from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen_0 = False
        loc_0 = -1

        for i, val in enumerate(nums):
            if val == 0:
                if seen_0:
                    return [0] * len(nums)

                seen_0 = True
                loc_0 = i
        
        if seen_0:
            output = [0] * len(nums)
            output[loc_0] = prod(nums[:loc_0] + nums[loc_0+1:])
            return output

        pr = prod(nums)
        output = [pr // nums[i] for i in range(len(nums))]
        return output
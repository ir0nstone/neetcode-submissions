from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_0 = 0
        loc_0 = -1

        for i, val in enumerate(nums):
            if val == 0:
                cnt_0 += 1
                loc_0 = i

                if cnt_0 > 1:
                    return [0] * len(nums)
        
        if cnt_0 == 1:
            output = [0] * len(nums)
            print(nums[:loc_0] + nums[loc_0+1:])
            output[loc_0] = prod(nums[:loc_0] + nums[loc_0+1:])
            return output

        pr = prod(nums)
        output = [pr // nums[i] for i in range(len(nums))]
        return output
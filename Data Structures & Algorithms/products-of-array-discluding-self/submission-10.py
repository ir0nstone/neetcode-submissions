class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        pr = 1
        for i, val in enumerate(nums):
            pr *= val
            prefix[i] = pr
        
        po = 1
        for i in range(len(nums)-1, -1, -1):
            po *= nums[i]
            postfix[i] = po

        # now calculate
        output = [postfix[1]] + [prefix[i-1] * postfix[i+1] for i in range(1, len(nums)-1)] + [prefix[-2]]
        return output


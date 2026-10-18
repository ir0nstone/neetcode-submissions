from math import inf, prod

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        non_zero_subarrays = []

        start_idx = 0
        last_zero_idx = -1

        for end_idx, num in enumerate(nums):
            # if end_idx == start_idx:
            #     continue

            if num == 0:
                non_zero_subarrays.append(nums[start_idx:end_idx])
                start_idx = end_idx + 1
                last_zero_idx = end_idx

        if last_zero_idx == -1:
            return self.max_prod_array_no_zeroes(nums)

        if last_zero_idx < len(nums)-1:
            non_zero_subarrays.append(nums[last_zero_idx+1:])

        prods = [0]

        for a in non_zero_subarrays:
            prods.append(self.max_prod_array_no_zeroes(a))

        return max(prods)


    def max_prod_array_no_zeroes(self, nums):
        # what if continguous 0s, so we have empty arrays?
        if len(nums) == 0:
            return -inf

        if len(nums) == 1:
            return nums[0]

        l_neg_idx, r_neg_idx = -1, -1
        even_neg_count = True

        for idx, num in enumerate(nums):
            if num < 0:
                even_neg_count = not even_neg_count

                if l_neg_idx == -1:
                    l_neg_idx = idx

                r_neg_idx = idx

        if even_neg_count:
            return prod(nums)
        else:
            return max(prod(nums[l_neg_idx+1:]), prod(nums[:r_neg_idx]))
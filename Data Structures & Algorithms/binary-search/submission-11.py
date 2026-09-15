class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        if right == 0:
            return 0 if nums[0] == target else -1
        
        while left + 1 != right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

        return -1

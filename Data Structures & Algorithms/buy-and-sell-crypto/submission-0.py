class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1

        max_diff = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            elif prices[right] > prices[left]:
                max_diff = max(prices[right] - prices[left], max_diff)
            
            right += 1
        
        return max_diff

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        results = {}

        for i, n in enumerate(numbers):
            if n in results:
                return [results[n]+1, i+1]

            results[target-n] = i
        
        return []
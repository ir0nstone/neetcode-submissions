class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count - O(n)
        ctr = Counter(nums)

        # now create a "dictionary" where the index is
        # the count of that number and the value the number
        # this helps us find the top K in O(n)
        # TODO how is this not just sorting in O(n)??
        swapped = [[] for _ in range(len(nums) + 1)]
        top_k = []

        for val, cnt in ctr.items():
            swapped[cnt].append(val)
        
        for idx in range(len(swapped) - 1, -1, -1):
            top_k += swapped[idx]

            if len(top_k) == k:
                break
        
        return top_k

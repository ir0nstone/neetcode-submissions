class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        cmn = ctr.most_common()
        vals = [t[0] for t in cmn[:k]]

        return vals
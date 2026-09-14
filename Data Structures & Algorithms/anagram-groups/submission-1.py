class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)

        for s in strs:
            srt = ''.join(sorted(s))
            grps[srt].append(s)

        return list(grps.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)
        base = ord('a')

        for s in strs:
            signature = [0] * 26

            for l in s:
                signature[ord(l) - base] += 1
            
            signature = tuple(signature)
            grps[signature].append(s)

        return list(grps.values())

from string import printable

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        delim = '>'
        included = ''.join(strs)

        for p in printable:
            if p not in included:
                delim = p
                print(delim)
                break
        
        return delim + delim.join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        if len(s) == 1:
            return [""]

        delim, text = s[0], s[1:]

        return text.split(delim)

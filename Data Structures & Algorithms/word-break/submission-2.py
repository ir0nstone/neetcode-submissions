class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {'': True}

        def recurse(st):
            if st in mem:
                return mem[st]

            for w in wordDict:
                if st.startswith(w) and recurse(st.removeprefix(w)):
                    mem[st] = True
                    return True
            
            mem[st] = False
            return False
        
        return recurse(s)
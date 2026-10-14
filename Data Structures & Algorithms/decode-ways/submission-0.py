from string import ascii_uppercase

class Solution:
    def numDecodings(self, s: str) -> int:
        mem = [-1] * len(s)

        rev_map = {str(i+1): ascii_uppercase[i] for i in range(26)}

        def decode_from(i):
            if i == len(s):
                return 1
            elif i > len(s):
                return 0

            if mem[i] != -1:
                return mem[i]
            
            total = 0

            if s[i] in rev_map:
                total += decode_from(i+1)
            if s[i:i+2] in rev_map:
                total += decode_from(i+2)
            
            mem[i] = total
            return total
        
        return decode_from(0)

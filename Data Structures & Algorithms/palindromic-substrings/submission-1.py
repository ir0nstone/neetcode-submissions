class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            left, right = i, i

            count += 1
            
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                count += 1
                left -= 1
                right += 1
            
            if i == len(s) - 1 or s[i] != s[i+1]:
                continue

            left = i
            right = i+1
            
            count += 1

            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                count += 1
                left -= 1
                right += 1
        
        return count

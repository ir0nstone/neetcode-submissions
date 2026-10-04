class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_len_str = s[0]

        for i in range(len(s)):
            # do the odd-length ones first
            left = i
            right = i
            length = 1
            
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                length += 2
                left -= 1
                right += 1
            
            if length > max_len:
                max_len = length
                max_len_str = s[left:right+1]
            
            # do the even ones now
            if i == len(s) - 1 or s[i] != s[i+1]:
                continue

            left = i
            right = i+1
            length = 2
            
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                length += 2
                left -= 1
                right += 1
            
            if length > max_len:
                max_len = length
                max_len_str = s[left:right+1]

        return max_len_str

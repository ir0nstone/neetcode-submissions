from string import ascii_letters, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        comb = set(ascii_letters + digits)

        sub = []

        for c in s:
            if c in comb:
                sub.append(c.lower())

        return list(reversed(sub)) == sub
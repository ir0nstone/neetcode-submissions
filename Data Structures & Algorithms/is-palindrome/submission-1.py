from string import ascii_letters, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        comb = set(ascii_letters + digits)

        sub = []

        for c in s:
            if c in comb:
                sub.append(c.lower())

        l = len(sub)

        return all(sub[i] == sub[l-1-i] for i in range(len(sub)//2))
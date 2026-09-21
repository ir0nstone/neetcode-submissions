class Solution:
    def isValid(self, s: str) -> bool:
        opening = '({['
        closing = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for l in s:
            if l in opening:
                stack.append(l)
            elif stack and stack[-1] == closing[l]:
                stack.pop()
            else:
                return False
            
        return not stack

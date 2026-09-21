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
            elif not stack or stack[-1] != closing[l]:
                return False
            else:
                    stack.pop()
            
        return not stack

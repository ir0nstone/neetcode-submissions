class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for sym in tokens:
            if sym == '+':
                nums.append(nums.pop() + nums.pop())
            elif sym == '-':
                nums.append(-nums.pop() + nums.pop())
            elif sym == '*':
                nums.append(nums.pop() * nums.pop())
            elif sym == '/':
                den = nums.pop()
                nums.append(int(nums.pop() / den))
            else:
                nums.append(int(sym))
        
        return int(nums[0])

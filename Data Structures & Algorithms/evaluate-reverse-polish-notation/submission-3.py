class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']

        nums = []

        for sym in tokens:
            if sym == '+':
                t = nums.pop() + nums.pop()
                nums.append(t)
            elif sym == '-':
                t = -nums.pop() + nums.pop()
                nums.append(t)
            elif sym == '*':
                t = nums.pop() * nums.pop()
                nums.append(t)
            elif sym == '/':
                den = nums.pop()
                nums.append(int(nums.pop() / den))
            else:
                nums.append(int(sym))
        
        return int(nums[0])

class Solution:
    def __init__(self):
        self.mem = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        # print(n)
        if n in self.mem:
            return self.mem[n]

        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.mem[n] = res
        return res

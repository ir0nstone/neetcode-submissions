class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {0: 0}

        def min_to_reach(val):
            if val in mem:
                return mem[val]
            
            pos = []

            for c in coins:
                if c <= val and (v := min_to_reach(val-c)) != -1:
                    pos.append(v)
            
            best = 1 + min(p for p in pos) if pos else -1
            mem[val] = best
            
            return best
        
        return min_to_reach(amount)

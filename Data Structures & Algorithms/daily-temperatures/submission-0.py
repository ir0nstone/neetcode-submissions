class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        waiting = []
        
        for i, temp in enumerate(temperatures):
            while waiting and temp > waiting[-1][1]:
                idx, _ = waiting.pop()
                output[idx] = i - idx

            waiting.append((i, temp))

        return output

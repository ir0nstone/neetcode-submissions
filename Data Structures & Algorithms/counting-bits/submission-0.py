class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if i == 2 * offset:
                offset = i

            output[i] = 1 + output[i-offset]

        return output

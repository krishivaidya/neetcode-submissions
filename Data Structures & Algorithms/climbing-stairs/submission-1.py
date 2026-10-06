class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0] * (n + 2)

        count[n + 1] = 0
        count [n] = 1

        for i in range(n - 1, -1, -1):
            count[i] = count[i + 1] + count[i + 2]

        return count[0]



        
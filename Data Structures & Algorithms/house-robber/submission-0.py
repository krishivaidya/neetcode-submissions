class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def rob(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            best = nums[i]

            for j in range(i + 2, len(nums)):
                best = max(best, nums[i] + rob(j))

            memo[i] = best
            return memo[i]

        answer = 0

        for k in range(len(nums)):
            answer = max(answer, rob(k))

        return answer

        
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def dfs(index):
            if index >= n:
                return 0

            if index in memo:
                return memo[index]

            choice1 = nums[index] + dfs(index + 2)
            choice2 = dfs(index + 1)
            memo[index] = max(choice1,choice2)
            return memo[index] 

        return dfs(0)

        
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums) 


        def dp (prev_ind, cur_ind):
            if cur_ind >= n:
                return 0 

            if (prev_ind, cur_ind) in memo:
                return memo[(prev_ind, cur_ind)]

            skip = dp(prev_ind, cur_ind + 1)
            choose = 0
            if prev_ind == -1 or nums[prev_ind] < nums[cur_ind]:
                choose = 1 + dp(cur_ind, cur_ind + 1)
            memo[(prev_ind, cur_ind)] = max(skip, choose)
            return memo[(prev_ind, cur_ind)]

        return dp(-1, 0)
                

        
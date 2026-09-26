class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        ind = 0

        def dfs(ind):
            if ind > len(nums) - 1:
                res.append(subset.copy())
                return 

            dfs(ind + 1)

            subset.append(nums[ind])
            dfs(ind + 1)
            subset.pop()

        dfs(0)

        return res

        

        
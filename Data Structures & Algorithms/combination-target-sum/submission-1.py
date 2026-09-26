class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        check = set()
        subset = []

        def dfs(final, idx):

            if final == 0:
                result.append(subset.copy())
                return

            if final < 0 or idx >= len(nums):
                return

            subset.append(nums[idx])
            dfs(final - nums[idx], idx)

            subset.pop()

            dfs(final, idx + 1)

        dfs(target, 0)
        return result
        
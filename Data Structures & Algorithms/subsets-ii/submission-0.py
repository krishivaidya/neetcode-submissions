class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        i = 0 

        def backtrack(i):
            if i > len(nums) - 1:
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            i = i + 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1

            backtrack(i)

        backtrack(0)

        return res

        
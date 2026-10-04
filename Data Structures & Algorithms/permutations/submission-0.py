class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = [float("inf")] * len(nums)

        def back(index):
            if index == len(nums):
                result.append(subset.copy())
                return
    

            for i in range(len(nums)):
                if subset[i] == float("inf"):
                    subset[i] = nums[index]
                    back(index + 1)
                    subset[i] = float("inf")

                else:
                    continue 

        back(0)
        return result 
        
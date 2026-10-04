class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for i in range(len(nums)):
            if nums[i] in store:
                return True 

            else:
                store.add(nums[i])

        return False
        
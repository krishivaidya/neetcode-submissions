class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for num in range(len(nums)):
            check = target - nums[num]
            if check in values and num != values[check]:
                return [values[check], num]
            else:
                values[nums[num]] = num
        

        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue 
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                csum = a + nums[l] + nums[r]
                if csum > 0:
                    r -= 1
                elif csum < 0:
                    l+= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l = l + 1
        
        return res




        
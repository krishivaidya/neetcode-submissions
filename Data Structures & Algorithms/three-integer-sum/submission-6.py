class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
       

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                csum = nums[i] + nums[l] + nums[r]

                if csum > 0:
                    r -= 1
                
                elif csum < 0:
                    l += 1
                
                else:
                    
                    res.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                     
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1
                
                    while l < r and nums[r] == nums[r + 1]:
                        r = r - 1
        return res

                
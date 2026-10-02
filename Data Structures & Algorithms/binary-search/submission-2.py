class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(l,r):
            if l > r:
                return -1

            mid = l + (r - l)// 2

            
            if target == nums[mid]:
                return mid 

            elif target > nums[mid]:
                l = mid + 1
                return bs(l,r)

            else:
                r = mid - 1
                return bs(l,r)



        return bs(0,len(nums) - 1)
    




        
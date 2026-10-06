class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 
        maxim = [-1] *  (n + 2)
        maxim[n] = 0
        maxim [n + 1] = 0

        for i in range(n - 1, -1 , -1):
            currentval = 0 

            if i >= n:
                currentval = 0

            else:
                currentval = nums[i]
            choice1 = currentval + maxim[i + 2]
            choice2 = maxim[i + 1]
            maxim[i] = max(choice1, choice2)

        return maxim[0]
            

        
        
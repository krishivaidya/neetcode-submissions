class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = 0
        memo = {}
        start = False 

        def bt(i):
            if i >= len(cost):
                return 0 

            if i in memo:
                return memo[i]
            else:
                first = cost[i] + bt(i + 1)
                second = cost[i] + bt(i + 2)
                memo[i] = min(first, second)
        
            return memo[i]


        return min(bt(0), bt(1))



                

        
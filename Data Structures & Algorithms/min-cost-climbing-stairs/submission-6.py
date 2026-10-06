class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
    

        def dfs(ind):
            if ind >= len(cost):
                return 0 

            if ind in memo:
                return memo[ind]

            memo[ind] = cost[ind] + min(dfs(ind + 1) , dfs(ind + 2))
            return memo[ind]


        return min(dfs(0), dfs(1))            
           
        


        
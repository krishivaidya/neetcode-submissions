class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [-1] * (len(cost) + 3)
        n = len(cost)
        mincost[n + 2] = 0
        mincost[n + 1] = 0 

        for i in range(n, -1, -1):
            curcost = 0
            if i > n - 1:
                curcost = 0
            else:
                curcost = cost[i]

            choice1 = curcost + mincost[i + 1]
            choice2 = curcost + mincost[i + 2]
            mincost[i] = min(choice1, choice2)

        return min(mincost[0], mincost[1])


        
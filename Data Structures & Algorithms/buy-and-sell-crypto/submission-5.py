class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxprof = 0

        for r in range(l + 1, len(prices)):
            if prices[l] > prices[r]:
                l = r

            else:
                maxprof = max(maxprof, prices[r] - prices[l])


        return maxprof

        
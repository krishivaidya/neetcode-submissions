class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxprof = 0

        while r <= len(prices) - 1:
            if prices[l] > prices[r]:
                l = r
                r = l + 1

            else:
                maxprof = max(maxprof, prices[r] - prices[l])
                r += 1


        return maxprof
        
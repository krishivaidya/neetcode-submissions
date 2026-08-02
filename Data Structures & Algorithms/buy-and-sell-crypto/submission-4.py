class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r 
                r += 1
            else:
                current = prices[r] - prices[l]
                maxp = max(maxp, current)
                r += 1
        return maxp

        
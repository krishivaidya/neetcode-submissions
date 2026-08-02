class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmax = 0
        
        for i in range(len(prices)):
            buy_date = prices[i]
            for j in range(i + 1, len(prices)):
                selldate = prices[j]
                tmax = max(tmax, selldate - buy_date)

        if tmax <= 0:
            return 0
        else:
            return tmax 



        
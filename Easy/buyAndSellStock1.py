class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -1
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1] and buy == -1:
                buy = prices[i-1]
            elif prices[i-1] > prices[i] and buy != -1:
                profit += prices[i-1]-buy
                buy = -1
            if i == len(prices)-1 and buy != -1:
                print(buy, prices[i])
                profit += prices[i]-buy
        return profit
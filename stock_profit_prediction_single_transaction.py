class Solution:
    def maxProfit(self, prices):
        # code here
        profits = set()
        profit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
            else:
                profits.add(profit)
                profit = 0
        return max(profits)

obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
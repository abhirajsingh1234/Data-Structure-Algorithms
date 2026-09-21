class Solution:
    def maxProfit(self, prices):
        # code here
        profit = 0
        for i in range(len(prices)-1):
            
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
            print(profit)
        return profit
obj = Solution()
print(obj.maxProfit([100, 180, 260, 310, 40, 535, 695]))
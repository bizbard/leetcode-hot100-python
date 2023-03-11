from typing import List


"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        minprice = prices[0]
        dp = [0] * n
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minprice)

        return max(dp)
    

"""
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0
        
        # n = len(prices)
        # profit = 0
        # for i in range(1, n):
        #     tmp = prices[i] - prices[i-1]
        #     if tmp > 0:
        #         profit = profit + tmp

        # return profit
        if not prices:
            return 0
        
        n = len(prices)
        if n < 2:
            return 0
        
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[n-1][0]
    

"""
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0, 0, 0]] * n
        dp[0][0] = -prices[0]
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0]+prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[n-1][1], dp[n-1][2])


if __name__ == "__main__":
    # dp[i]=max(dp[i−1],prices[i]−minprice)
    # ======= Test Case =======
    prices = [7,1,5,3,6,4]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maxProfit(prices)
    print(res)
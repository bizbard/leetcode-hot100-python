import collections
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][0]: 手上持有股票的最大收益
        # dp[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # dp[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[n - 1][1], dp[n - 1][2])


if __name__ == '__main__':
    # ======= Test Case =======
    prices = [1,2,3,0,2]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maxProfit(prices)
    print(res)
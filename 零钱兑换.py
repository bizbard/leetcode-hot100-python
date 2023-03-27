import collections
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(n):
            # base case
            if n == 0: 
                return 0
            if n < 0: 
                return -1
            # 求最小值，所以初始化为正无穷
            res = float('INF')
            for coin in self.coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            return res if res != float('INF') else -1

        self.coins = coins
        return dp(amount)


if __name__ == '__main__':
    # ======= Test Case =======
    coins = [1, 2, 5]
    amount = 11
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.coinChange(coins, amount)
    print(res)
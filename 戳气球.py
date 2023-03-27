import collections
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n-1, -1, -1):
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    total = val[i] * val[k] * val[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)

        return dp[0][n + 1]


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [3,1,5,8]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maxCoins(nums)
    print(res)
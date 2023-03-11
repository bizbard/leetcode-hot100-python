class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n)]

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]
            

if __name__ == '__main__':
    # ======= Test Case =======
    n = 3
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.climbStairs(n)
    print(res)
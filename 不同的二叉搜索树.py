class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]

        return dp[n]
    

if __name__ == '__main__':
    # G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
    # G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)
    # ======= Test Case =======
    n = 3
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.numTrees(n)
    print(res)
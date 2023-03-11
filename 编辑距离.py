class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]
            

if __name__ == '__main__':
    # dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
    # 其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
    # ======= Test Case =======
    word1 = "horse"
    word2 = "ros"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.minDistance(word1, word2)
    print(res)
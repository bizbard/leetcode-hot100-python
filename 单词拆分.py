from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # dp = [False] * (n+1)
        # dp[0] = True
        # for i in range(1, n+1):
        #     for j in range(i+1, n+1):
        #         if dp[i] and s[i:j] in wordDict:
        #             dp[j] = True

        # return dp[-1]

        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]
        

if __name__ == '__main__':
    # ======= Test Case =======
    s = "leetcode"
    wordDict = ["leet", "code"]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.wordBreak(s, wordDict)
    print(res)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        res = []
        stack = []
        i = 0
        for i in range(len(s)):
            if stack and s[i] == ')':
                res.append(stack.pop())
                res.append(i)
            else:
                stack.append(i)
        
        # 判断res的最长连续子序列
        i = 0
        ans = 0
        while i < len(res):
            j = i
            while j < len(res)-1 and res[j] == res[j+1] - 1:
                j += 1
            ans = max(ans, j-i+1)
            i = j+1
        return ans


if __name__ == '__main__':
    # 先使用栈找到所有可以匹配的索引号，然后找出最长连续数列
    # ======= Test Case =======
    s = ")()())"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.longestValidParentheses(s)
    print(res)

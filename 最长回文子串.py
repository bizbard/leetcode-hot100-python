class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = list(s)
        res = []

        def getPalindrome(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        for i in range(len(s)):
            s1 = getPalindrome(s, i, i)
            s2 = getPalindrome(s, i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2

        return ''.join(res)

if __name__ == '__main__':
    # ======= Test Case =======
    s = "babad"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.longestPalindrome(s)
    print(res)
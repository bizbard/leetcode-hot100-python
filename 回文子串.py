import collections
from typing import List, Optional
    

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def getHui(s, left, right):
            temp = 0
            while 0 <= left and right < len(s):
                if s[left] == s[right]:
                    temp += 1
                left -= 1
                right += 1
            return temp


        res = 0
        for i in range(len(s)):
            cnt1 = getHui(s, i, i)
            cnt2 = getHui(s, i, i+1)
            res = res + cnt1 + cnt2
        
        return res 


if __name__ == '__main__':
    # ======= Test Case =======
    s = "aaa"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.countSubstrings(s)
    print(res)
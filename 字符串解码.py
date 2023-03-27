import collections
from typing import List, Optional
    

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for i in s:
            if i == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif i == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= i <= '9':
                multi = multi * 10 + int(i)
            else:
                res += i
        return res

if __name__ == '__main__':
    # ======= Test Case =======
    s = "3[a2[c]]"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.decodeString(s)
    print(res)
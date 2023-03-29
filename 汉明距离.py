import collections
from typing import List, Optional
    

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        print(x^y)
        print(bin(x^y))
        print(type(bin(x^y)))
        return bin(x^y).count("1")


if __name__ == '__main__':
    # ======= Test Case =======
    x = 1
    y = 4
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.hammingDistance(x, y)
    print(res)
import collections
from typing import List, Optional


class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones
        
        bits = [countOnes(i) for i in range(n + 1)]
        return bits


if __name__ == '__main__':
    # ======= Test Case =======
    n = 5
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.countBits(n)
    print(res)
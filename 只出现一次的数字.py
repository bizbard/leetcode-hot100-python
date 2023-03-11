from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

if __name__ == '__main__':
    # 位运算
    # 任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
    # 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
    # 异或运算满足交换律和结合律，即 a⊕b⊕a = b⊕a⊕a = b⊕(a⊕a) = b⊕0 = b
    # ======= Test Case =======
    nums = [2,2,1]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.singleNumber(nums)
    print(res)
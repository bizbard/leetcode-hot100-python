import collections
from typing import List, Optional
    

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {0:1}
        sum = 0
        res = 0
        for num in nums:
            sum += num
            res += dic.get(sum-k, 0)
            dic[sum] = dic.get(sum,0)+1
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,1,1]
    k = 2
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.subarraySum(nums, k)
    print(res)
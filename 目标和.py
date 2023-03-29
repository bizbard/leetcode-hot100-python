import collections
from typing import List, Optional
    

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        sum = 0
        self.res = 0
        def findWay(nums, sum):
            if not nums:
                if sum == target:
                    self.res += 1
                return
            
            findWay(nums[1:], sum+nums[0])
            findWay(nums[1:], sum-nums[0])

        findWay(nums, sum)
        return self.res


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,1,1,1,1]
    target = 3
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.findTargetSumWays(nums, target)
    print(res)
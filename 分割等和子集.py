import collections
from typing import List, Optional
    

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:      # 总和无法等分
            return False
        
        target = total // 2
        if max(nums) > target:  # 最大值大于总和的一半，无法分割
            return False
        
        dp = [[False] * (target + 1) for i in range(len(nums))]
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(target+1):
                if j - nums[i] == 0:
                    dp[i][j] = True

                if j - nums[i] > 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        
        return dp[len(nums)-1][target]


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,2,3,5]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.canPartition(nums)
    print(res)
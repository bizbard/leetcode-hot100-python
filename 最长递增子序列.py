import collections
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 的值代表 nums 以 nums[i]nums[i]nums[i] 结尾的最长子序列长度
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [10,9,2,5,3,7,101,18]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.lengthOfLIS(nums)
    print(res)
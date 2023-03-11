from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)


if __name__ == '__main__':
    # dp[i]：表示以 nums[i] 结尾的连续子数组的最大和
    # ======= Test Case =======
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maxSubArray(nums)
    print(res)
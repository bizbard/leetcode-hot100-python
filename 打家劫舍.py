from typing import List

class Solution:
    """
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的
    房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        
        return dp[n]
    

    """
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这
    意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
    """
    def rob(self, nums: List[int]) -> int:
        def robBase(nums):
            n = len(nums)
            dp = [0] * (n+1)
            dp[0] = 0
            dp[1] = nums[0]

            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            
            return dp[n]
        
        front = robBase(nums[1:])
        end = robBase(nums[:-1])

        return max(front, end)
            

if __name__ == '__main__':
    # dp[i]表示从前 i 个房子中能偷到的最大金额
    # ======= Test Case =======
    nums = [2,3,2]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.rob(nums)
    print(res)
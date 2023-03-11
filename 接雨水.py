from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # leftMax
        leftMax = [0 for i in range(len(height))]
        leftMax[0] = height[0]

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])

        # rightMax
        n = len(height)
        rightMax = [0 for i in range(n)]
        rightMax[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        # result
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i])-height[i]
        
        return res


if __name__ == '__main__':
    # 创建两个长度为 n 的数组 leftMax 和 rightMax。
    # 对于 0≤i<n0，leftMax[i]表示下标 i 及其左边的位置中，height的最大高度，
    # rightMax[i]表示下标 i 及其右边的位置中，height的最大高度。
    # ======= Test Case =======
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.trap(height)
    print(res)
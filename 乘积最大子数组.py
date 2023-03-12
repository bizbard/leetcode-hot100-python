from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        minPro = [0] * n
        maxPro = [0] * n
        minPro[0] = maxPro[0] = nums[0]

        for i in range(1, n):
            maxPro[i] = max(maxPro[i - 1] * nums[i], nums[i], minPro[i - 1] * nums[i])
            minPro[i] = min(minPro[i - 1] * nums[i], nums[i], maxPro[i - 1] * nums[i])

        return max(maxPro)
            

if __name__ == '__main__':
    # 令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
    # 由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
    # ======= Test Case =======
    nums = [2,3,-2,4]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maxProduct(nums)
    print(res)
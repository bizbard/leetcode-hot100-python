from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]

        r = [1 for i in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]

        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            res[i] = l[i] * r[i]

        return res
            

if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,2,3,4]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.productExceptSelf(nums)
    print(res)
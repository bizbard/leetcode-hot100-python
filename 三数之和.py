from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            target = 0 - nums[first]

            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


if __name__ == '__main__':
    # 三重循环，但是在第二重和第三重循环中有优化
    # ======= Test Case =======
    nums = [-1,0,1,2,-1,-4]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.threeSum(nums)
    print(res)
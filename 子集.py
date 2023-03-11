from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,2,3]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.subsets(nums)
    print(res)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i , num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [2,7,11,15]
    target = 9
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.twoSum(nums, target)
    print(res)
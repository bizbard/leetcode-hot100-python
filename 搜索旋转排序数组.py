from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid]:
                if nums[0] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target < nums[n-1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


if __name__ == '__main__':
    # 利用双段有序的特性
    # ======= Test Case =======
    nums = [4,5,6,7,0,1,2]
    target = 0
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.search(nums, target)
    print(res)
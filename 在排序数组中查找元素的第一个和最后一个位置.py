from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        leftIndex = self.binarySearch_1(nums, target) # 找第一个大于等于target的元素下标
        rightIndex = self.binarySearch_2(nums, target) - 1 # 找第一个大于target的元素下标 - 1
        if leftIndex <= rightIndex and rightIndex < len(nums) and nums[leftIndex] == nums[rightIndex] == target:
            return [leftIndex, rightIndex]
        else:
            return [-1, -1]
        
    def binarySearch_1(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans

    def binarySearch_2(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target: # 可复用
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 利用有序的特性进行二分
    # ======= Test Case =======
    nums = [5,7,7,8,8,10]
    target = 8
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.searchRange(nums, target)
    print(res)
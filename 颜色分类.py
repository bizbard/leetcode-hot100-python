from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums, l, r):
            i, j = l, r
            while i < j:
                while i < j and nums[j] >= nums[l]: j -= 1
                while i < j and nums[i] <= nums[l]: i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            return i

        def quicksort(nums, l, r):
            if l >= r:
                return
            mid = partition(nums, l, r)
            quicksort(nums, l, mid-1)
            quicksort(nums, mid+1, r)

        # def quick_sort(nums, l, r):
        #     # 子数组长度为 1 时终止递归
        #     if l >= r: return
        #     # 哨兵划分操作
        #     i = partition(nums, l, r)
        #     # 递归左（右）子数组执行哨兵划分
        #     quick_sort(nums, l, i - 1)
        #     quick_sort(nums, i + 1, r)
    
        # def partition(nums, l, r):
        #     # 以 nums[l] 作为基准数
        #     i, j = l, r
        #     while i < j:
        #         while i < j and nums[j] >= nums[l]: j -= 1
        #         while i < j and nums[i] <= nums[l]: i += 1
        #         nums[i], nums[j] = nums[j], nums[i]
        #     nums[l], nums[i] = nums[i], nums[l]
        #     return i

        quicksort(nums, 0, len(nums)-1)
            

if __name__ == '__main__':
    # 快速排序partition
    # ======= Test Case =======
    nums = [2,0,2,1,1,0]
    # ====== Driver Code ======
    Sol = Solution()
    Sol.sortColors(nums)
    print(nums)
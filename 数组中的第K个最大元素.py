from typing import List
import random

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     def quickSelect(nums, l, r, index):
    #         pivotIndex = randomPartition(nums, l, r);
    #         if pivotIndex == index:
    #             return nums[pivotIndex];
    #         else:
    #             return quickSelect(nums, pivotIndex + 1, r, index) if pivotIndex < pivotIndex else quickSelect(nums, l, pivotIndex - 1, index)

    #     def randomPartition(nums, l, r):
    #         t = random.randint(l, r)
    #         nums[t], nums[r] = nums[r], nums[t]
    #         return partition(nums, l, r)

    #     def partition(nums, l, r):
    #         if l >= r:
    #             return
            
    #         pivot = nums[l]
    #         # all in nums[left + 1..j] <= pivot
    #         # all in nums(j..i) > pivot
    #         j = l
    #         i = l + 1
    #         while i <= r:
    #             if nums[i] > pivot:
    #                 i += 1
    #             else:
    #                 j += 1
    #                 nums[j], nums[i] = nums[i], nums[j]
    #                 i += 1
    #         nums[l], nums[j] = nums[j], nums[l]
    #         return j
            
    #     res = quickSelect(nums, 0, len(nums)-1, len(nums)-k)

    #     return res
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(arr: List[int], low: int, high: int) -> int:
            pivot = arr[low]                                        # 选取最左边为pivot

            left, right = low, high     # 双指针
            while left < right:
                
                while left<right and arr[right] >= pivot:          # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]                             # 并将其移动到left处
                
                while left<right and arr[left] <= pivot:           # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]                             # 并将其移动到right处
            
            arr[left] = pivot           # pivot放置到中间left=right处
            return left
        
        def randomPartition(arr: List[int], low: int, high: int) -> int:
            pivot_idx = random.randint(low, high)                   # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
            return partition(arr, low, high)                        # 调用partition函数

        def topKSplit(arr: List[int], low: int, high: int, k: int) -> int:
            # mid = partition(arr, low, high)                   # 以mid为分割点【非随机选择pivot】
            mid = randomPartition(arr, low, high)               # 以mid为分割点【随机选择pivot】
            if mid == k-1:                                      # 第k小元素的下标为k-1
                return arr[mid]                                 #【找到即返回】
            elif mid < k-1:
                return topKSplit(arr, mid+1, high, k)           # 递归对mid右侧元素进行排序
            else:
                return topKSplit(arr, low, mid-1, k)            # 递归对mid左侧元素进行排序
        
        n = len(nums)
        return topKSplit(nums, 0, n-1, n-k+1)                   # 第k大元素即为第n-k+1小元素
            

if __name__ == '__main__':
    # 数组中的第 k 个最大元素，也即是数组中的第 n - k + 1 个最小元素
    # ======= Test Case =======
    nums = [3,2,1,5,6,4]
    k = 2
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.findKthLargest(nums, k)
    print(res)
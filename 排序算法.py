from typing import List

class Solution:
    # # 选择排序
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)

    #     for i in range(n-1):
    #         minIndex = i
    #         for j in range(i+1, n):
    #             if nums[j] < nums[minIndex]:
    #                 minIndex = j
    #         nums[i], nums[minIndex] = nums[minIndex], nums[i]
    #     return nums

    # # 冒泡排序
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)

    #     for i in range(n-1):
    #         sorted = True
    #         for j in range(1, n-i):
    #             if nums[j-1] > nums[j]:
    #                 nums[j-1], nums[j] = nums[j], nums[j-1]
    #                 sorted = False
    #         if sorted:
    #             return nums
    #     return nums

    # # 插入排序
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)

    #     for i in range(1, n):
    #         for j in range(i, 0, -1):
    #             if nums[j-1] > nums[j]:
    #                 nums[j-1], nums[j] = nums[j], nums[j-1]
    #             else:
    #                 break
    #     return nums

    # # 希尔排序
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     delta = n // 2
    #     while delta > 0:
    #         for start in range(delta):
    #             i = start + delta
    #             while i < n:
    #                 j = i
    #                 while j - delta >= 0:
    #                     if nums[j-delta] > nums[j]:
    #                         nums[j-delta], nums[j] = nums[j], nums[j-delta]
    #                     else:
    #                         break
    #                     j -= delta
    #                 i += delta
    #         delta = delta // 2

    #     return nums

    # 归并排序
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0] * n

        # 对 nums[left...right] 进行归并排序
        def mergeSort(nums, left, right, temp):
            if left == right:
                return
            
            mid = (left + right) // 2
            mergeSort(nums, left, mid, temp)
            mergeSort(nums, mid + 1, right, temp)

            # 合并两个有序区间
            for i in range(left, right + 1):
                temp[i] = nums[i]
            i = left
            j = mid + 1
            for k in range(left, right + 1):
                if i == mid+1:
                    nums[k] = temp[j]
                    j += 1
                elif j == right + 1:
                    nums[k] = temp[i]
                    i += 1
                elif temp[i] <= temp[j]:
                    nums[k] = temp[i]
                    i += 1
                else:
                    nums[k] = temp[j]
                    j += 1
        
        mergeSort(nums, 0, n-1, temp)
        return nums

        return nums
            

if __name__ == '__main__':
    # 给你一个整数数组 nums，请你将该数组升序排列。
    # ======= Test Case =======
    nums = [5,1,1,2,0,0]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.sortArray(nums)
    print(res)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        arr = []

        while i < m or j < n:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1

            elif i < m:
                arr.append(nums1[i])
                i += 1

            elif j < n:
                arr.append(nums2[j])
                j += 1

        return arr[len(arr)//2] if len(arr) % 2 else (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2.0


if __name__ == '__main__':
    # 中位数：指的是该数左右个数相等
    # [nums1[:left1],nums2[:left2] | nums1[left1:], nums2[left2:]]
    # ======= Test Case =======
    nums1 = [1,2]
    nums2 = [3,4]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.findMedianSortedArrays(nums1, nums2)
    print(res)
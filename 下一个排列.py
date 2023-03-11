from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(lists, i, j):
            while i < j:
                lists[i], lists[j] = lists[j], lists[i]
                i += 1
                j -= 1

        n = len(nums)
        firstIndex = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                firstIndex = i
                numk = nums[i]
                break
        if firstIndex == -1:
            reverse(nums, 0, n-1)

        secondIndex = -1
        for i in range(n-1, -1, -1):
            if nums[i] > numk:
                secondIndex = i

        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex+1, n-1)


if __name__ == '__main__':
    # 先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组
    # 再找出另一个最大索引 l 满足 nums[l] > nums[k]
    # 交换 nums[l] 和 nums[k]
    # 最后翻转 nums[k+1:]
    # ======= Test Case =======
    nums = [1,2,3]
    # ====== Driver Code ======
    Sol = Solution()
    Sol.nextPermutation(nums)
    print(nums)
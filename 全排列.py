from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], tmp + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == '__main__':
    # 回溯
    # ======= Test Case =======
    nums = [1,2,3]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.permute(nums)
    print(res)
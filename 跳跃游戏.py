from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i , jump in enumerate(nums):
            if max_jump >= i and i + jump > max_jump:
                max_jump = i + jump
        
        return max_jump >= len(nums)


if __name__ == '__main__':
    # 贪心算法，尽可能到达最远位置，如果能到达某个位置，那一定能到达它前面的所有位置。
    # ======= Test Case =======
    nums = [3,2,1,0,4]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.canJump(nums)
    print(res)
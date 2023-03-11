from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if (num - 1) not in num_set:
                cur_num = num
                cur_length = 1

                while cur_num + 1 in num_set:
                    cur_length += 1
                    cur_num = cur_num + 1

                longest_streak = max(longest_streak, cur_length)

        return longest_streak
        

if __name__ == '__main__':
    # ======= Test Case =======
    nums = [100,4,200,1,3,2]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.longestConsecutive(nums)
    print(res)
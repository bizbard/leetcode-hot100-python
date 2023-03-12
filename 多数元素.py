from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntdic = {}
        for num in nums:
            if num in cntdic:
                cntdic[num] += 1
            else:
                cntdic[num] = 1
            if cntdic[num] > len(nums) // 2:
                return num
        
        return None
            

if __name__ == '__main__':
    # ======= Test Case =======
    nums = [2,2,1,1,1,2,2]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.majorityElement(nums)
    print(res)
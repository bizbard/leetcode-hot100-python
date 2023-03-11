# 题目过难，略过

from typing import List


# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         # 我们在缓存数据的时候，是从左向右缓存的，我们计算出一个结果的顺序是从右向左的
#         size = len(heights)
#         res = 0

#         stack = []

#         for i in range(size):
#             while len(stack) > 0 and heights[i] < heights[stack[-1]]:
#                 cur_height = heights[stack.pop()]

#                 while len(stack) > 0 and cur_height == heights[stack[-1]]:
#                     stack.pop()

#                 if len(stack) > 0:
#                     cur_width = i - stack[-1] - 1
#                 else:
#                     cur_width = i

#                 res = max(res, cur_height * cur_width)
#             stack.append(i)

#         while len(stack) > 0 != None:
#             cur_height = heights[stack.pop()]
#             while len(stack) > 0 and cur_height == heights[stack[-1]]:
#                 stack.pop()

#             if len(stack) > 0:
#                 cur_width = size - stack[-1] - 1
#             else:
#                 cur_width = size
#             res = max(res, cur_height * cur_width)

#         return res

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
    

if __name__ == '__main__':
    # ======= Test Case =======
    heights = [2,1,5,6,2,3]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.largestRectangleArea(heights)
    print(res)
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                k = i
                l = j
                cur = 0
                while 0<=k<len(matrix) and matrix[k][l] == "1":
                    cur += 1
                    k += 1
                dp[i][j] = cur
                
        def maxRectangleArea(heights):
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
            
            ans = max(min((right[i] - left[i] - 1), heights[i])**2 for i in range(n)) if n > 0 else 0
            return ans

        maxArea = []
        for i in range(len(matrix)):
            maxArea.append(maxRectangleArea(dp[i]))
            
        return max(maxArea)
            

if __name__ == '__main__':
    # ======= Test Case =======
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maximalSquare(matrix)
    print(res)
# 题目过难，略过

from typing import List


class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        # 记录当前位置上方连续“1”的个数
        pre=[0]*(n)
        ans = []
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j]=pre[j]+1 if mat[i][j]=="1" else 0

            n = len(pre)
            left, right = [0] * n, [0] * n

            mono_stack = list()
            for i in range(n):
                while mono_stack and pre[mono_stack[-1]] >= pre[i]:
                    mono_stack.pop()
                left[i] = mono_stack[-1] if mono_stack else -1
                mono_stack.append(i)
            
            mono_stack = list()
            for i in range(n - 1, -1, -1):
                while mono_stack and pre[mono_stack[-1]] >= pre[i]:
                    mono_stack.pop()
                right[i] = mono_stack[-1] if mono_stack else n
                mono_stack.append(i)
            
            ans.append(max((right[i] - left[i] - 1) * pre[i] for i in range(n)) if n > 0 else 0)

        return max(ans)

if __name__ == '__main__':
    # ======= Test Case =======
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maximalRectangle(matrix)
    print(res)
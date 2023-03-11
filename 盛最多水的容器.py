from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0

        while i <= j:
            size = min(height[i], height[j]) * (j - i)
            res = max(size, res)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return res


if __name__ == '__main__':
    # 在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽底边宽度−1变短：
    # 若向内移动短板，水槽的短板min(h[i],h[j])min(h[i], h[j])min(h[i],h[j])可能变大，因此下个水槽的面积可能增大。
    # 若向内移动长板，水槽的短板min(h[i],h[j])min(h[i], h[j])min(h[i],h[j])​不变或变小，因此下个水槽的面积一定变小。
    # ======= Test Case =======
    height = [1,8,6,2,5,4,8,3,7]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maxArea(height)
    print(res)
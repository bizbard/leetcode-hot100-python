from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]


if __name__ == '__main__':
    # 先沿主对角线交换两侧的元素
    # 然后对现在矩阵的每一行进行反转
    # ======= Test Case =======
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # ====== Driver Code ======
    Sol = Solution()
    Sol.rotate(matrix)
    print(matrix)
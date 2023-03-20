from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n-1
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False
            

if __name__ == '__main__':
    # ======= Test Case =======
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.searchMatrix(matrix, target)
    print(res)
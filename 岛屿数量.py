from typing import List

class Solution:
    # 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    # 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    # 此外，你可以假设该网格的四条边均被水包围。
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     def dfs(grid, i, j):
    #         m = len(grid)
    #         n = len(grid[0])
    #         if not 0 <= i < m or not 0 <= j < n or grid[i][j] != "1":
    #             return
            
    #         grid[i][j] = "0"
    #         dfs(grid, i-1, j)
    #         dfs(grid, i+1, j)
    #         dfs(grid, i, j-1)
    #         dfs(grid, i, j+1)

    #     if not grid:
    #         return 0
        
    #     m = len(grid)
    #     n = len(grid[0])
    #     numIsland = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == "1":
    #                 numIsland += 1
    #                 dfs(grid, i, j)
        
    #     return numIsland
    
    """
    网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
    岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
    用“先污染后治理”的方法，先做递归调用，再在每个 DFS 函数的开头判断坐标是否合法，不合法的直接返回。岛屿的周长就是岛屿方格和非岛屿方格相邻的边的数量。
    """
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     def dfs(grid, i, j):
    #         m = len(grid)
    #         n = len(grid[0])

    #         if not 0 <= i < m or not 0 <= j < n:
    #             return 1
            
    #         if grid[i][j] == 0:
    #             return 1
            
    #         if grid[i][j] != 1:
    #             return 0
            
    #         grid[i][j] = 2
    #         return dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1)

    #     m = len(grid)
    #     n = len(grid[0])

    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 return dfs(grid, i, j)
        
    #     return 0
    

    """
    计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            if not 0<=i<m or not 0<=j<n:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            elif grid[i][j] == 2:
                return 0
            
            else:
                grid[i][j] = 2
                return 1 + dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1)

        m = len(grid)
        n = len(grid[0])

        maxsize = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxsize = max(maxsize, dfs(grid, i, j))

        return maxsize


if __name__ == '__main__':
    # ======= Test Case =======
    # grid = [
    #     ["1","1","1","1","0"],
    #     ["1","1","0","1","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","0","0","0"]
    # ]
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.maxAreaOfIsland(grid)
    print(res)
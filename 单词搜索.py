class Solution(object):
    
    def exist(self, board, word):
        # 标记矩阵
        mark = [[0 for i in range(len(board[0]))] for i in range(len(board))]

        # 找入口
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if not word:
            return True
        
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direct in directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if mark[cur_i][cur_j] == 1:
                    continue
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    mark[cur_i][cur_j] = 0
        return False

if __name__ == '__main__':
    # ======= Test Case =======
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.exist(board, word)
    print(res)
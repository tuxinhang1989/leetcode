class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m < 3:
            return
        n = len(board[0])
        if n < 3:
            return

        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][n-1] == 'O':
                self.dfs(i, n-1, board)

        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(0, j, board)
            if board[m-1][j] == 'O':
                self.dfs(m-1, j, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'

    def dfs(self, row, col, board):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return
        if board[row][col] in ['X', 'Y']:
            return
        board[row][col] = 'Y'
        for i, j in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
            self.dfs(i, j, board)


if __name__ == '__main__':
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'O', 'X'],
    ]
    print Solution().solve(board)


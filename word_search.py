class Solution(object):
    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[row])):
                exists = self.dfs(board, row, col, word, 0)
                if exists:
                    return True
        return False

    def dfs(self, board, row, col, word, word_idx):
        if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:
            return False
        c = board[row][col]
        if c == '#':
            return False
        if word_idx == len(word) - 1 and c == word[word_idx]:
            return True
        if word[word_idx] != c:
            return False
        board[row][col] = '#'
        success = (self.dfs(board, row-1, col, word, word_idx + 1) or
                  self.dfs(board, row+1, col, word, word_idx + 1) or
                  self.dfs(board, row, col-1, word, word_idx + 1) or
                  self.dfs(board, row, col+1, word, word_idx + 1))
        board[row][col] = c
        return success


if __name__ == '__main__':
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = 'ABCCED'
    #word = 'SEE'
    #word = 'ABCB'
    board = [['a']]
    word = 'a'
    print Solution().exist(board, word)


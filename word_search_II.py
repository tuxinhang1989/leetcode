class Node(object):
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
        node.word = word


class Solution(object):
    def findWords(self, board, words):
        root = Node()
        self.build_trie(root, words)
        result = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.dfs(board, row, col, root, result)
        return list(result)

    def build_trie(self, root, words):
        for word in words:
            root.insert(word)

    def dfs(self, board, row, col, node, result):
        print row, col
        c = board[row][col]
        if c == '#':
            return
        if c not in node.children:
            return
        node = node.children[c]
        if node.end:
            result.add(node.word)
        board[row][col] = '#'
        if row > 0:
            self.dfs(board, row-1, col, node, result)
        if col > 0:
            self.dfs(board, row, col-1, node, result)
        if row < len(board) - 1:
            self.dfs(board, row+1, col, node, result)
        if col < len(board[0]) - 1:
            self.dfs(board, row, col+1, node, result)
        board[row][col] = c


if __name__ == '__main__':
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    '''
    board = [['a']]
    words = ['a']
    '''
    print Solution().findWords(board, words)


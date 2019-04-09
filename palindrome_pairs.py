class Node(object):
    def __init__(self):
        self.children = {}
        self.index = -1
        self.palindromes_below = []


class Solution(object):
    def palindromePairs(self, words):
        root = Node()
        for index, word in enumerate(words):
            self.build_trie(root, word[::-1], index)

        res = []
        for i, word in enumerate(words):
            self.collect_pair(i, word, root, res)
        return res

    def collect_pair(self, word_idx, word, root, pairs):
        node = root
        for j, c in enumerate(word):
            if node.index != -1 and self.is_palindrome(word[j:]) and word_idx != node.index:
                pairs.append([word_idx, node.index])
            if c not in node.children:
                return 
            node = node.children[c]
        # self.traverse_node(node, '', pairs, word_idx)
        pairs.extend([[word_idx, idx] for idx in node.palindromes_below if word_idx != idx])

    def traverse_node(self, node, s, pairs, word_idx):
        if node.index != -1 and node.index != word_idx and self.is_palindrome(s):
            pairs.append([word_idx, node.index])
        if not node.children:
            return
        for c, child in node.children.items():
            self.traverse_node(child, s+c, pairs, word_idx)

    def is_palindrome(self, s):
        n = len(s)
        if n < 2:
            return True
        mid = (n-1)//2
        if n % 2 == 0:
            return s[:mid+1] == s[n-1:mid:-1]
        else:
            return s[:mid] == s[n-1:mid:-1]

    def build_trie(self, root, word, index):
        node = root
        for i, c in enumerate(word):
            if c not in node.children:
                node.children[c] = Node()
            if self.is_palindrome(word[i:]):
                node.palindromes_below.append(index)
            node = node.children[c]
        node.index = index
        node.palindromes_below.append(index)


if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll", ""]
    # words = ["bat","tab","cat", 'aba']
    # words = ['a', '']
    print Solution().palindromePairs(words)

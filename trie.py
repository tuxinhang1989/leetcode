class Node(object):
    def __init__(self):
        self.children = {}
        self.value = None
        self.end = False


class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def insert(self, key, value):
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.value = value
        node.end = True

    def traverse(self, node, s, res):
        if node.end:
            res.add(s)
        if not node.children:
            return res.add(s)
        for c, child in node.children.items():
            self.traverse(child, s+c, res)

    def find(self, key):
        node = self.root
        for c in key:
            if c not in node.children:
                return None
            else:
                node = node.children[c]
        return node.value


if __name__ == '__main__':
    t = Trie()
    t.insert('hello', 1)
    t.insert('hell', 2)
    t.insert('hex', 3)
    t.insert('abc', 4)
    t.insert('www', 5)

    assert t.find('hello') == 1
    assert t.find('hell') == 2
    assert t.find('hex') == 3

    res = set()
    t.traverse(t.root, '', res)
    print res


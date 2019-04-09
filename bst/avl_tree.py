class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        new_root.height = max(node.height, self.height(new_root.right)) + 1
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        new_root.height = max(node.height, self.height(new_root.left)) + 1
        return new_root

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if node.val > val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        diff = self.height(node.left) - self.height(node.right)
        if diff > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        elif diff < -1:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def remove(self, val):
        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        if node is None:
            return None
        if node.val > val:
            node.left = self._remove(node.left, val)
        elif node.val < val:
            node.right = self._remove(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.find_least_node(node.right)
                node.val = successor.val
                node.right = self._remove(node.right, successor.val)
        diff = self.height(node.left) - self.height(node.right) 
        if diff > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        elif diff < -1:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def find_least_node(self, node):
        if node is None or node.left is None:
            return node
        return self.find_least_node(node.left)


if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    print avl.root.val, avl.root.height
    print avl.root.left.val, avl.root.left.height
    print avl.root.right.val, avl.root.right.height

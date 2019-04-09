# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.array = []
        self.limit = k
        self.result = None
        self.traverse(root)
        return self.result

    def traverse(self, root):
        if not root or self.result:
            return
        self.traverse(root.left)
        self.array.append(root.val)
        if len(self.array) == self.limit:
            self.result = self.array[-1]
            return
        self.traverse(root.right)

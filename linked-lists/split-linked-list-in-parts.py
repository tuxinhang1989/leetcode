import math
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        cur = root
        while cur is not None:
            cur = cur.next
            length += 1
        i = k
        res = []
        while i > 0:
            print i
            if root is None:
                res.append(None)
            else:
                part_len = int(math.ceil(length/float(i)))
                length -= part_len
                if part_len == 0:
                    res.append(None)
                else:
                    pre = None
                    cur = root
                    for j in range(part_len):
                        pre = cur
                        cur = cur.next
                    pre.next = None
                    res.append(root)
                    root = cur
            i -= 1
        return res

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    k = 5
    print Solution().splitListToParts(root, k)

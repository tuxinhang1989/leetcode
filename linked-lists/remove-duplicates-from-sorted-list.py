class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur = head
        nex = cur.next
        while nex is not None:
            if cur.val != nex.val:
                cur.next = nex
                cur = nex
                nex = cur.next
            else:
                nex = nex.next

        cur.next = nex
        return head

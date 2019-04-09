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
        pre = None
        cur = head
        nex = cur.next
        while nex is not None:
            if cur.val != nex.val:
                if cur.next is not nex:
                    if pre is None:
                        cur = head = nex
                        nex = cur.next
                    else:
                        pre.next = nex
                        cur = nex
                        nex = cur.next
                else:
                    pre = cur
                    cur = nex
                    nex = cur.next
            else:
                nex = nex.next

        if cur.next is not None:
            if pre is None:
                head = None
            else:
                pre.next = None

        return head

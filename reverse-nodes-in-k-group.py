class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        cur_head = head
        cur_tail = head
        for i in range(k-1):
            cur_tail = cur_tail.next
            if cur_tail is None:
                return head
        next_head = cur_tail.next
        head = cur_tail
        pre = None
        cur = head
        nex = cur.next
        for i in range(k):
            cur.next = pre
            pre = cur
            if nex is None:
                return cur
            cur = nex
            nex = nex.next

        while True:
            cur_tail = next_head
            cur_head.next = next_head
            for i in range(k-1):
                cur_tail = cur_tail.next
                if cur_tail is None:
                    return head

            cur_head.next = cur_tail
            cur_head = next_head
            next_head = cur_tail.next
            pre = None
            cur = cur_head
            nex = cur.next
            for i in range(k):
                cur.next = pre
                pre = cur
                if nex is None:
                    return head
                cur = nex
                nex = nex.next



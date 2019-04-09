# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        pre = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if fast is None:
            pre.next = None
        pre = None
        cur = slow
        while cur is not None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        right_cur = pre
        right_next = right_cur.next
        left_cur = head
        left_next = left_cur.next
        while left_next is not None and right_next is not None:
            left_cur.next = right_cur
            right_cur.next = left_next
            left_cur = left_next
            left_next = left_cur.next
            right_cur = right_next
            right_next = right_cur.next
        left_cur.next = right_cur
        right_cur.next = None


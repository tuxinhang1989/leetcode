class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur = head.next
        pre = head
        head = cur
        nex = cur.next
        while nex is not None:
            cur.next = pre
            cur = nex.next
            if cur is None:
                pre.next = nex
                break
            else:
                pre.next = nex.next
                pre = nex
                nex = cur.next

        if cur is not None:
            cur.next = pre
            pre.next = None
        self.draw(head)
        return head

    def draw(self, head):
        cur = head
        while cur is not None:
            print cur.val
            cur = cur.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    Solution().swapPairs(head)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        s, f, pre = head, head, None
        while f and f.next:
            s, f, pre = s.next, f.next.next, s
        pre.next = None
        p1, p2 = self.sortList(head), self.sortList(s)
        res_head = res_node = None
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                s = p1
                p1 = p1.next
            else:
                s = p2
                p2 = p2.next
            if res_head is None:
                res_head = res_node = s
            else:
                res_node.next = s
                res_node = s

        while p1 is not None:
            res_node.next = p1
            res_node = p1
            p1 = p1.next

        while p2 is not None:
            res_node.next = p2
            res_node = p2
            p2 = p2.next
        return res_head

if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5)
    res_head = Solution().sortList(head)
    res_node = res_head
    while res_node is not None:
        print res_node.val
        res_node = res_node.next


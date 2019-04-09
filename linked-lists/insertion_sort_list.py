class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        cur = head.next
        nxt = cur.next
        res_head = head
        res_head.next = None
        while cur is not None:
            if cur.val <= res_head.val:
                cur.next = res_head
                res_head = cur
            else:
                res_cur = res_head
                while res_cur is not None:
                    if res_cur.val <= cur.val and (res_cur.next is None or res_cur.next.val > cur.val):
                        cur.next = res_cur.next
                        res_cur.next = cur
                        break
                    else:
                        res_cur = res_cur.next
            cur = nxt
            if cur is None:
                break
            nxt = cur.next
        return res_head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    res_head = Solution().insertionSortList(head)
    res_node = res_head
    while res_node is not None:
        print res_node.val
        res_node = res_node.next


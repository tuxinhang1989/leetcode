class Solution(object):
    def reverseList(self, head, m, n):
        cur = head
        for i in range(m-2):
            cur = cur.next
        pre_node = cur
        m_node = pre = cur.next
        cur = pre.next
        nex = cur.next
        for i in range(n-m-1):
            cur.next = pre
            pre = cur
            cur = nex
            nex = cur.next
        cur.next = pre
        pre_node.next = cur
        m_node.next = nex
        return head


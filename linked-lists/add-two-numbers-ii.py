# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        cur = l1
        while cur is not None:
            num1 = num1 * 10 + cur.val
            cur = cur.next
        num2 = 0
        cur = l2
        while cur is not None:
            num2 = num2 * 10 + cur.val
            cur = cur.next
        num = num1 + num2
        print num
        stack = []
        while num > 0:
            stack.append(num % 10)
            num //= 10
        if not stack:
            return None
        cur = head = ListNode(stack.pop())
        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next
        return head

if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print Solution().addTwoNumbers(l1, l2)


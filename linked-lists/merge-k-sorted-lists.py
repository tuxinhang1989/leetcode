from heapq import heappush, heappop
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Element(object):
    __slots__ = ('row', 'val', 'node')

    def __init__(self, row, val, node):
        self.row = row
        self.val = val
        self.node = node

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = cur = None
        heap = []
        for i in range(lists):
            if lists[i] is not None:
                ele = Element(i, lists[i].val, lists[i])
                heappush(heap, ele)
        while len(heap) > 0:
            min_ele = heappop(heap)
            min_node = min_ele.node
            if head is None:
                head = cur = min_node
            else:
                cur.next = min_node
                cur = min_node

            if min_node.next is not None:
                node = min_node.next
                min_ele.val = node.val
                min_ele.node = node
                heappush(heap, min_ele)

        return head

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = self.heapify(nums[:k])
        for num in nums[k:]:
            if num > min_heap[0]:
                self.pop(min_heap)
                self.push(min_heap, num)
        return min_heap[0]

    def heapify(self, arr):
        size = len(arr)
        k = size // 2 - 1
        while k >= 0:
            self._shift_down(arr, k)
            k -= 1
        return arr

    def push(self, heap, element):
        heap.append(element)
        self._shift_up(heap, len(heap)-1)

    def pop(self, heap):
        size = len(heap)
        heap[0], heap[size-1] = heap[size-1], heap[0]
        res = heap.pop()
        self._shift_down(heap, 0)
        return res

    def _shift_down(self, heap, pos):
        left = 2 * pos + 1
        right = 2 * pos + 2
        size = len(heap)
        while left < size:
            if right < size:
                if heap[pos] > min(heap[left], heap[right]):
                    if heap[left] < heap[right]:
                        heap[pos], heap[left] = heap[left], heap[pos]
                        pos = left
                    else:
                        heap[pos], heap[right] = heap[right], heap[pos]
                        pos = right
                else:
                    break
            else:
                if heap[pos] > heap[left]:
                    heap[pos], heap[left] = heap[left], heap[pos]
                    pos = left
                else:
                    break
            left = 2 * pos + 1
            right = 2 * pos + 2

    def _shift_up(self, heap, pos):
        parent = (pos - 1) // 2
        while parent >= 0:
            if heap[parent] > heap[pos]:
                heap[parent], heap[pos] = heap[pos], heap[parent]
                pos = parent
                parent = (pos - 1) // 2
            else:
                break


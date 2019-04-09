import heapq


class Element(object):
    __slots__ = ('row', 'idx', 'value')
    def __init__(self, row, idx, value):
        self.row = row
        self.idx = idx
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = []
        max_val = nums[0][0]
        min_val = nums[0][0]
        for i in xrange(len(nums)):
            element = Element(i, 0, nums[i][0])
            if element.value > max_val:
                max_val = element.value
            if element.value < min_val:
                min_val = element.value
            heapq.heappush(pq, element)

        min_range = max_val - min_val
        start = min_val
        end = max_val
        while len(pq) == len(nums):
            min_ele = heapq.heappop(pq)
            if max_val - min_ele.value < min_range:
                start = min_ele.value
                end = max_val
                min_range = end - start

            if min_ele.idx + 1 < len(nums[min_ele.row]):
                min_ele.idx += 1
                min_ele.value = nums[min_ele.row][min_ele.idx]
                if min_ele.value > max_val:
                    max_val = min_ele.value
                heapq.heappush(pq, min_ele)

        return [start, end]


if __name__ == '__main__':
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    nums = [[1,2,3],[1,2,3],[1,2,3]]
    print Solution().smallestRange(nums)

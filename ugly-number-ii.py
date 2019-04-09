from heapq import heappush, heappop


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = set()
        heap = [1]
        i = 0
        while i < n:
            num = heappop(heap)
            i += 1
            a = num * 2
            if a not in s:
                heappush(heap, a)
                s.add(a)
            b = num * 3
            if b not in s:
                heappush(heap, b)
                s.add(b)
            c = num * 5
            if c not in s:
                heappush(heap, c)
                s.add(c)
        return num


if __name__ == '__main__':
    print Solution().nthUglyNumber(11)


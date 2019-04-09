class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        lo, hi = 1, n

        while lo <= hi:
            mid = (lo+hi) // 2
            if citations[mid-1] >= n+1-mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return n - lo + 1


if __name__ == '__main__':
    citations = [0, 1, 3, 5, 6, 7, 9]
    print Solution().hIndex(citations)


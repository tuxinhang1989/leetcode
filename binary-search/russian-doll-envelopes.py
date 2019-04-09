from bisect import bisect_left

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def cmp(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            else:
                return a[0] - b[0]
        envelopes.sort(cmp=cmp)
        ends = []
        for envelop in envelopes:
            idx = bisect_left(ends, envelop[1])
            if idx == len(ends):
                ends.append(envelop[1])
            else:
                ends[idx] = envelop[1]
        return len(ends)


if __name__ == '__main__':
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print Solution().maxEnvelopes(envelopes)


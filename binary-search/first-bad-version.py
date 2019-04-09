def isBadVersion(version):
    if version > 3:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo+hi) >> 1
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    print Solution().firstBadVersion(5)

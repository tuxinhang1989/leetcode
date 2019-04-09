class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    nums = [1,2,3,1]
    print Solution().findPeakElement(nums)

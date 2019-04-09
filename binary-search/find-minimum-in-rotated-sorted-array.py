class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[0]

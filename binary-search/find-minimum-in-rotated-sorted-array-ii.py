class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi and nums[lo] == nums[hi]:
            lo += 1
        if lo > hi:
            return nums[0]
        leftmost = lo
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] >= nums[leftmost]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[leftmost]


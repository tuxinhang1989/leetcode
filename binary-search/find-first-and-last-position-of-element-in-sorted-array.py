class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        if 0 <= lo < len(nums) and nums[lo] == target:
            first = lo
        else:
            first = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        if 0 <= hi < len(nums) and nums[hi] == target:
            last = hi
        else:
            last = -1
        return [first, last]


if __name__ == '__main__':
    nums = [1,3,3,7,7,8]
    target = 2
    print Solution().searchRange(nums, target)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        pivot = self.find_pivot(nums)
        print pivot
        if pivot == 0:
            return self.dfs(nums, 0, len(nums) - 1, target)
        elif nums[pivot] == target:
            return True
        elif nums[0] > target:
            return self.dfs(nums, pivot, len(nums) - 1, target)
        else:
            return self.dfs(nums, 0, pivot-1, target)

    def find_pivot(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo <= hi and nums[lo] == nums[hi]:
            lo += 1
        leftmost = lo
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] < nums[mid-1]:
                return mid
            elif nums[mid] >= nums[leftmost]:
                lo = mid + 1
            else:
                hi = mid - 1
        if leftmost > len(nums) - 1:
            return 0
        else:
            return leftmost

    def dfs(self, nums, lo, hi, target):
        if lo > hi:
            return False
        if lo == hi:
            return nums[lo] == target
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return self.dfs(nums, lo, mid-1, target)
        else:
            return self.dfs(nums, mid+1, hi, target)


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    print Solution().search(nums, target)

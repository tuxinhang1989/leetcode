class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = self.find_pivot(nums)
        if pivot == 0:
            return self.dfs(nums, 0, len(nums)-1, target)
        elif nums[0] <= target:
            return self.dfs(nums, 0, pivot-1, target)
        else:
            return self.dfs(nums, pivot, len(nums)-1, target)

    def find_pivot(self, nums):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] >= nums[0]:
                lo = mid+1
            elif nums[mid] < nums[mid-1]:
                return mid
            else:
                hi = mid-1
        return 0

    def dfs(self, nums, left, right, target):
        if left > right:
            return -1
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.dfs(nums, mid+1, right, target)
        else:
            return self.dfs(nums, left, mid-1, target)


if __name__ == '__main__':
    nums = [3, 1]
    target = 1
    print Solution().search(nums, target)

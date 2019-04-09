class Solution(object):
    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = 0
        while True:
            finder = nums[finder]
            slow = nums[slow]
            if slow == finder:
                return finder

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 5]
    print Solution().findDuplicate(nums)

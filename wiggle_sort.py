class Solution(object):
    def wiggle_sort(self, nums):
        nums.sort()
        half = (len(nums) + 1) / 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 5, 6, 7, 4, 8]
    print Solution().wiggle_sort(nums)


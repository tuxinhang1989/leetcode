class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = j = 0
        min_gap = n = len(nums)
        sum = 0
        while j < n:
            sum += nums[j]
            j += 1
            while sum >= s:
                min_gap = min(min_gap, j-i)
                sum -= nums[i]
                i += 1
        return min_gap if min_gap != n else 0


if __name__ == '__main__':
    s = 7
    nums = [2,3,1,2,4,3]
    print Solution().minSubArrayLen(s, nums)

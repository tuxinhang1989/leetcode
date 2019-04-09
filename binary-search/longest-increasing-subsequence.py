class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])

        return max(dp)


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print Solution().lengthOfLIS(nums)


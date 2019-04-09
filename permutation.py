class Solution(object):
    def permutation(self, nums):
        res = []
        for i, num in enumerate(nums):
            self.dfs([num], nums[:i]+nums[i+1:], res)
        return res

    def dfs(self, seq, nums, res):
        if not nums:
            res.append(seq)
            return
        for i, num in enumerate(nums):
            self.dfs(seq + [num], nums[:i]+nums[i+1:], res)


if __name__ == '__main__':
    import pprint
    nums = [1, 2, 3]
    res = Solution().permutation(nums)
    pprint.pprint(res)

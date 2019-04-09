class Solution(object):
    def sortColors(self, nums):
        z_idx = 0
        t_idx = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != 0:
                z_idx = i
                break

        for j in range(len(nums)-1, -1, -1):
            if nums[j] != 2:
                t_idx = j
                break

        i = z_idx
        while z_idx <= t_idx and i <= t_idx:
            if nums[i] == 0:
                nums[i], nums[z_idx] = nums[z_idx], nums[i]
                z_idx += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[t_idx] = nums[t_idx], nums[i]
                t_idx -= 1
            else:
                i += 1
        

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    print nums
    Solution().sortColors(nums)
    print nums


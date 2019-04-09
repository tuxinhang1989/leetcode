class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum

    def divide_and_conquer(self, nums):
        def dac(nums, left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]
            mid = ((left+right) >> 1)
            left_max = dac(nums, left, mid)
            right_max = dac(nums, mid+1, right)
            m1 = m2 = nums[mid+1]
            for i in range(mid+2, right+1):
                m2 += nums[i]
                if m2 > m1:
                    m1 = m2
            n1 = n2 = nums[mid]
            i = mid - 1
            while i > left - 1:
                n2 += nums[i]
                if n2 > n1:
                    n1 = n2
                i -= 1
            mid_max = m1 + n1
            return max(left_max, right_max, mid_max)
        return dac(nums, 0, len(nums)-1)


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print Solution().divide_and_conquer(arr)

def max_sub_sum(nums):
    n = len(nums)
    if n == 0:
        return 0
    max_sum = [0] * len(nums)
    max_sum[0] = nums[0]

    for i in range(1, n):
        if max_sum[i-1] > 0:
            max_sum[i] = max_sum[i-1] + nums[i]
        else:
            max_sum[i] = nums[i]
    return max(max_sum)


if __name__ == '__main__':
    nums = [1, -2, 3, 10, -4, 7, 2, -5]
    nums = [1, 1, 1, -2, -3, 2, 3, -1, 2, 3, -1, 3, 4]
    print max_sub_sum(nums)

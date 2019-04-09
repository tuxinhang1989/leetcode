class Solution(object):
    def find_start(self, numbers, target):
        end = len(numbers) - 1
        lo, hi = 0, end
        while lo < hi:
            mid = (lo + hi) >> 1
            if numbers[mid] + numbers[end] == target:
                return mid
            elif numbers[mid] + numbers[end] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def find_end(self, numbers, target):
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if numbers[0] + numbers[mid] == target:
                return mid
            elif numbers[0] + numbers[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers[0] + numbers[-1] > target:
            start = 0
            end = self.find_end(numbers, target)
        else:
            start = self.find_start(numbers, target)
            end = len(numbers) - 1

        i, j = start, end
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


if __name__ == '__main__':
    nums = [-3, 3, 5, 7, 9]
    target = 0
    print Solution().twoSum(nums, target)


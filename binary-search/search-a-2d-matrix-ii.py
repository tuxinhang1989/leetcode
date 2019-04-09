class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                res = self.find_first_smaller(matrix[row], 0, col, target)
                if res is True:
                    return True
                col = res
            else:
                row += 1
        return False

    def find_first_smaller(self, nums, lo, hi, target):
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi


if __name__ == '__main__':
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    target = 20
    print Solution().searchMatrix(matrix, target)

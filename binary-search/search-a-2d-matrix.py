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
        first_column = [row[0] for row in matrix]
        lo, hi = 0, m - 1
        if first_column[0] > target or matrix[-1][-1] < target:
            return False

        while lo < hi:
            mid = (lo + hi) // 2
            if first_column[mid] == target:
                return True
            elif first_column[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if first_column[lo] == target:
            return True
        if first_column[lo] > target:
            row_index = lo - 1
        else:
            row_index = lo

        row = matrix[row_index]
        lo, hi = 0, len(row) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


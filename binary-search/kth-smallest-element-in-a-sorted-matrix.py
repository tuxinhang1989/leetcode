from bisect import bisect_right

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) >> 1
            if sum(bisect_right(row, mid) for row in matrix) < k:
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == '__main__':
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]
    k = 8
    print Solution().kthSmallest(matrix, k)


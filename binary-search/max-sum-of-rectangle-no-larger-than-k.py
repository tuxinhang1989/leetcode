class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = float('-inf')
        for i in range(n):
            sums = [0] * m
            for j in range(i, n):
                for row in range(m):
                    sums[row] += matrix[row][j]
                max_sum = self.get_max_sub_sum(sums, k)
                if max_sum > res:
                    res = max_sum
        return res

    def get_max_sub_sum(self, sums, k):
        res = float('-inf')
        for i in range(len(sums)):
            s = 0
            for j in range(i, len(sums)):
                s += sums[j]
                if s > k:
                    continue
                if s > res:
                    res = s
        return res


if __name__ == '__main__':
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
    k = 8
    print Solution().maxSumSubmatrix(matrix, k)


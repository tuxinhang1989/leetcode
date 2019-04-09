from heapq import heappush, heappop

class Cell(object):
    __slots__ = ('row', 'col', 'height')
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __gt__(self, other):
        return self.height > other.height

    def __lt__(self, other):
        return self.height < other.height


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[0] * n for i in range(m)]
        pq = []
        for i in range(m):
            visited[i][0] = 1
            heappush(pq, Cell(i, 0, heightMap[i][0]))
            visited[i][n-1] = 1
            heappush(pq, Cell(i, n-1, heightMap[i][n-1]))

        for j in range(1, n-1):
            visited[0][j] = 1
            heappush(pq, Cell(0, j, heightMap[0][j]))
            visited[m-1][j] = 1
            heappush(pq, Cell(m-1, j, heightMap[m-1][j]))

        res = 0
        while len(pq) > 0:
            cell = heappop(pq)
            for row, col in ((cell.row-1, cell.col), (cell.row+1, cell.col), 
                             (cell.row, cell.col-1), (cell.row, cell.col+1)):
                if 0 <= row < m and 0 <= col < n and not visited[row][col]:
                    res += max(0, cell.height - heightMap[row][col])
                    new_cell = Cell(row, col, max(cell.height, heightMap[row][col]))
                    visited[row][col] = 1
                    heappush(pq, new_cell)

        return res


if __name__ == '__main__':
    heightMap = [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]
    print Solution().trapRainWater(heightMap)


import time
from collections import deque


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        m = len(grid)
        n = len(grid[0])
        q = deque()
        island_found = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))
                    island_found = 1
                    break
            if island_found:
                break

        res = 0
        while len(q) > 0:
            row, col = q.popleft()
            if row == 0:
                res += 1
            if col == 0:
                res += 1
            if row == m-1:
                res += 1
            if col == n-1:
                res += 1
            for i, j in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 0:
                        res += 1
                    else:
                        cell = (i, j)
                        if cell not in visited:
                            q.append(cell)
                            visited.add(cell)

        return res


if __name__ == '__main__':
    grid = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
    print Solution().islandPerimeter(grid)


import time
from collections import deque


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        visited = set()
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    start = (i, j)
                    visited.add(start)
                    q.append(start)
                    area = 0
                    while len(q) > 0:
                        sr, sc = q.popleft()
                        area += 1
                        for nr, nc in ((sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)):
                            neighbor_cell = (nr, nc)
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and neighbor_cell not in visited:
                                visited.add(neighbor_cell)
                                q.append(neighbor_cell)
                    if area > max_area:
                        max_area = area
        return max_area


if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print Solution().maxAreaOfIsland(grid)

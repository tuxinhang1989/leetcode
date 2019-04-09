from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
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

        res = 0
        for i in range(m):
            for j in range(n):
                start = (i, j)
                if grid[i][j] == "1" and start not in visited:
                    res += 1
                    visited.add(start)
                    q.append(start)
                    while len(q) > 0:
                        sr, sc = q.popleft()
                        for nr, nc in ((sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)):
                            next_cell = (nr, nc)
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1" and next_cell not in visited:
                                visited.add(next_cell)
                                q.append(next_cell)

        return res


if __name__ == '__main__':
    grid = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0],
    ]
    grid = [
        ["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print Solution().numIslands(grid)

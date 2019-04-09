class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[1] * n for i in range(m)]
        dp[m-1][n-1] = max(1 - dungeon[m-1][n-1], 1)
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(dp[i+1][n-1] - dungeon[i][n-1], 1)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(dp[m-1][j+1] - dungeon[m-1][j], 1)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)
        return dp[0][0]


if __name__ == '__main__':
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5],
    ]
    print Solution().calculateMinimumHP(dungeon)


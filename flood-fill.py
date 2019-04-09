import time
from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        q = deque()
        q.append((sr, sc))
        while len(q) > 0:
            row, col = q.popleft()
            image[row][col] = newColor
            for i, j in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if 0 <= i < m and 0 <= j < n and image[i][j] == color:
                    q.append((i, j))
        return image


if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1
    print Solution().floodFill(image, sr, sc, newColor)


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            if height[start] < height[end]:
                max_area = max(max_area, height[start] * (end-start))
                start += 1
            else:
                max_area = max(max_area, height[end] * (end-start))
                end -= 1
        return max_area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print Solution().maxArea(height)

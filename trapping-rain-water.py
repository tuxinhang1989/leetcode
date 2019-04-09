class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        left_highest = right_highest = 0
        res = 0
        while i < j:
            left_highest = max(left_highest, height[i])
            right_highest = max(right_highest, height[j])
            if left_highest <= right_highest:
                res += (left_highest - height[i])
                i += 1
            else:
                res += (right_highest - height[j])
                j -= 1
        return res


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print Solution().trap(height)


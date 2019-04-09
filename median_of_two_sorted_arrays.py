class Solution(object):
    def compare(self, left, right):
        if len(left) == 0 or len(right) == 0:
            return True
        return left[-1] <= right[0]

    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        if x == 0:
            if y % 2 == 0:
                return (nums2[(y+1)/2] + nums2[(y-1)/2]) / 2.0
            else:
                return nums2[(y-1)/2]
        start, end = 0, x-1
        while True:
            p1 = (start+end) / 2 + 1
            p2 = (x+y+1)/2 - p1
            if (self.compare(nums1[:p1], nums2[p2:]) and self.compare(nums2[:p2], nums1[p1:])):
                break
            elif nums1[p1-1] > nums2[p2]:
                end = p1 - 2
            elif nums2[p2-1] > nums1[p1]:
                start = p1
        if p1 <= 0:
            x2 = float('-inf')
        else:
            x2 = nums1[p1-1]
        if p2 <= 0:
            y2 = float('-inf')
        else:
            y2 = nums2[p2-1]
        if (x+y) % 2 == 0:
            if p1 >= x:
                x1 = float('inf')
            else:
                x1 = nums1[p1]
            if p2 >= y:
                y1 = float('inf')
            else:
                y1 = nums2[p2]
            r1 = min(x1, y1)
            r2 = max(x2, y2)
            return (r1 + r2) / 2.0
        else:
            return max(x2, y2)


if __name__ == '__main__':
    nums1 = [100001]
    nums2 = [100000]
    print Solution().findMedianSortedArrays(nums1, nums2)


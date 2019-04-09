class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sig = (dividend < 0) == (divisor < 0)
        res = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            i = 1
            temp = divisor
            while dividend >= temp:
                dividend -= temp
                res += i
                temp <<= 1
                i <<= 1
        return min(res, 2**32-1) if sig else -res


if __name__ == '__main__':
    print Solution().divide(20, 3)


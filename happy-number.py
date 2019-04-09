mem = set()

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        mem.add(n)
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        print mem, res
        if res in mem:
            return False
        else:
            return self.isHappy(res)


if __name__ == '__main__':
    print Solution().isHappy(13)

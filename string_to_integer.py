class Solution(object):
    def myAtoi(self, str):
        res = 0
        sign = ''
        integers = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        signs = ['+', '-']
        seen = 0
        last = ''
        for c in str:
            if not seen:
                if c in signs:
                    if last in signs:
                        break
                    sign = c
                elif c == ' ':
                    if last in signs:
                        break
                elif c in integers:
                    if sign and last != sign:
                        break
                    seen = 1
                    res = res * 10 + int(c)
                else:
                    break
            else:
                if c not in integers:
                    break
                res = res * 10 + int(c)
            last = c

        if sign == '-':
            res = res * -1
            if res < -2**31:
                res = -2**31
        else:
            if res > 2**31 - 1:
                res = 2**31 - 1
        return res


if __name__ == '__main__':
    s = '42'
    s = '   -42'
    s = "4193 with words"
    #s = "words and 987"
    #s = "-91283472332"
    #s = "+-2"
    s = "- 234"
    print Solution().myAtoi(s)

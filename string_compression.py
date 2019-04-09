class Solution(object):
    def compress(self, chars):
        if len(chars) < 2:
            return len(chars)
        i = 1
        pre = chars[0]
        count = 1
        res = [pre]
        c_idx = 0
        while i < len(chars):
            c = chars[i]
            if c == pre:
                count += 1
            else:
                if count > 1:
                    digits = str(count)
                    for j in range(len(digits)):
                        c_idx += 1
                        chars[c_idx] = digits[j]
                count = 1
                pre = c
                c_idx += 1
                chars[c_idx] = pre
            i += 1
        if count > 1:
            digits = str(count)
            for j in range(len(digits)):
                c_idx += 1
                chars[c_idx] = digits[j]
        chars[c_idx+1:] = []

        return len(chars)


if __name__ == '__main__':
    chars = ['a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    print Solution().compress(chars)
    print chars


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        a = set()
        b = set()
        n = len(s)
        for i in range(n-9):
            substr = s[i:i+10]
            if substr in a:
                b.add(substr)
            else:
                a.add(substr)
        print substr
        return list(b)


if __name__ == '__main__':
    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    print Solution().findRepeatedDnaSequences(s)

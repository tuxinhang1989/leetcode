import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        i = 0
        start = end = 0
        for j, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if not missing:
                while i <= j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if need[s[i]] == 0:
                    need[s[i]] += 1
                    missing += 1
                    if not end or j - i < end - start:
                        start, end = i, j + 1
                    i += 1

        return s[start: end]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = 'a'
    t = 'aa'
    print Solution().minWindow(s, t)

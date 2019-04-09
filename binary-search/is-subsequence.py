from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_idx = defaultdict(list)
        for i, c in enumerate(t):
            char_idx[c].append(i)
        pos = 0
        for c in s:
            if not char_idx[c] or pos > char_idx[c][-1]:
                return False
            pos = char_idx[c][bisect_left(char_idx[c], pos)] + 1
        return True

    def method2(self, s, t):
        pos = 0
        for c in s:
            pos = t.find(c, pos)
            if pos == -1:
                return False
            pos += 1
        return True

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print Solution().method2(s, t)

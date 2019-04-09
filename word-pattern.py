class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = {}
        used = set()
        words = str.split()
        if len(pattern) != len(words):
            return False

        for i, c in enumerate(pattern):
            if c not in m:
                if words[i] not in used:
                    m[c] = words[i]
                    used.add(words[i])
                else:
                    return False
            else:
                if m[c] != words[i]:
                    return False

        return True


if __name__ == '__main__':
    pattern = 'abba'
    str = 'dog dog dog dog'
    print Solution().wordPattern(pattern, str)


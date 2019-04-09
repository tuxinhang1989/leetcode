class Solution(object):
    def isMatch(self, s, p):
        s_len = len(s)
        p_len = len(p)
        dp = [[0] * (p_len+1) for i in range(s_len+1)]
        dp[0][0] = 1
        for j in range(2, p_len+1, 2):
            if (p[j-1] == '*' and dp[0][j-2]):
                dp[0][j] = 1
        i = 1
        j = 1
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if s[i-1] != p[j-2] and p[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]

        return dp[s_len][p_len]

    def method2(self, s, p):
        if len(p) == 0:
            return len(s) == 0
        first_match = len(s)> 0 and (p[0] == '.' or p[0] == s[0])
        if len(p) > 1 and p[1] == '*':
            if first_match:
                return self.method2(s[1:], p) or self.method2(s, p[2:])
            else:
                return self.method2(s, p[2:])
        else:
            return first_match and self.method2(s[1:], p[1:])

if __name__ == '__main__':
    s = 'mississippi'
    p = 'mis*is*p*.'
    s = 'aab'
    p = 'c*a*b*'
    print Solution().isMatch(s, p)

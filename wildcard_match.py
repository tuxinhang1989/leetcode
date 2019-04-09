class Solution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[0] * (n+1) for i in range(m+1)]
        dp[0][0] = 1
        for j in range(1, n+1):
            if p[j-1] == '*' and dp[0][j-1]:
                dp[0][j] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]

        return bool(dp[m][n])


if __name__ == '__main__':
    s = 'acdcb'
    p = 'a*c?b'
    print Solution().isMatch(s, p)

class Solution(object):
    def longestPalindrome(self, s):
        '''
        longest = ''
        for i in range(len(s)):
            sub_str = ''
            for j in range(i, len(s)):
                sub_str += s[j]
                if sub_str == sub_str[::-1] and len(sub_str) > len(longest):
                    longest = sub_str
        return longest
        '''
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        i = n - 1 
        res = ''
        while i >= 0:
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
            i -= 1
        return res


if __name__ == '__main__':
    s = ''
    res = Solution().longestPalindrome(s)
    print repr(res)


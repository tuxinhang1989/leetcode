class Solution(object):
    def shortestPalindrome(self, s):
        j = 0
        for i in range(len(s)):
            if s[:i+1] == s[i::-1]:
                j = i
        return s[j+1:][::-1] + s

    def is_palindrome(self, s):
        i = 0
        n = len(s)
        mid = (n - 1) // 2
        while i <= mid:
            if s[i] != s[n-1-i]:
                return False
            i += 1
        return True

    def method2(self, s):
        j = len(s) - 1
        for j in range(len(s)-1, -1, -1):
            if self.is_palindrome(s[:j+1]):
                break
        return s[:j:-1] + s


if __name__ == '__main__':
    #s = 'abcd'
    #s = "aacecaaa"
    #print Solution().method2(s)
    print Solution().is_palindrome('abba')


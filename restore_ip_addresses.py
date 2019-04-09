class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, (), res)
        return res

    def dfs(self, s, ip, res):
        if len(ip) == 4 and s:
            return
        if len(ip) == 3:
            if not s:
                return
            if len(s) == 1 or (s[0] != '0' and 0 <= int(s) <= 255):
                ip += (s,)
                res.append('.'.join(ip))
                return
            else:
                return
        if s[:1]:
            self.dfs(s[1:], ip + (s[:1],), res)
        if len(s[:2]) == 2 and s[0] != '0':
            self.dfs(s[2:], ip + (s[:2],), res)
        if len(s[:3]) == 3 and s[0] != '0' and 0 <= int(s[:3]) <= 255:
            self.dfs(s[3:], ip + (s[:3],), res)


if __name__ == '__main__':
    s = '25525511135'
    s = "0000"
    s = "010010"
    print Solution().restoreIpAddresses(s)

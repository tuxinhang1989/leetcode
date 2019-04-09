class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        s_len = len(s)
        word_len = len(words[0])
        n = len(words)
        sub_str_len = n * word_len
        target = []
        i = 0
        while 1:
            if s_len - i < sub_str_len:
                break
            target_words = words[:]
            for k in range(n):
                start = i + k * word_len
                end = start + word_len
                word = s[start:end]
                if word not in target_words:
                    break
                else:
                    target_words.remove(word)
            if not target_words:
                target.append(i)
            i += 1
        return target


if __name__ == '__main__':
    s = 'barfoothefoobarman'
    words = ["foo","bar"]
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print Solution().findSubstring(s, words)


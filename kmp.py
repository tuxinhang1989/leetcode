def search(s, p):
    i = 0
    j = 0
    res = []
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            if i == len(s) - 1 and j < len(p) - 1:
                break
            elif i < len(s) and j == len(p) - 1:
                res.append(i - j)
                i += 1
                j = 0
            else:
                i += 1
                j += 1
        else:
            if j == 0:
                i += 1
            else:
                i -= get_partial(p[:j])
                j = 0
    return res


def get_partial(s):
    i = len(s) - 1
    j = 1
    while s[:i] != s[j:] and i > 0:
        i -= 1
        j += 1

    return i


if __name__ == '__main__':
    #s = 'BBC ABCDAB ABCDABCDABDE'
    #pattern = 'ABCDABD'
    s = 'abcdabecde'
    pattern = 'cde'
    print search(s, pattern)

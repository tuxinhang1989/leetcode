class Solution(object):
    def convert(self, s, numRows):
        if numRows < 3:
            numCols = len(s)
        else:
            numCols = (len(s) / (2*numRows - 2) + 1) * (numRows - 1)
        matrix = [[''] * numCols for i in range(numRows)]
        j = 0
        idx = 0
        end = False
        while 1:
            i = 0
            while i < numRows:
                if idx >= len(s):
                    end = True
                    break
                matrix[i][j] = s[idx]
                i += 1
                idx += 1
            if end:
                break
            i = numRows - 2
            j += 1
            while i > 0:
                if idx >= len(s):
                    end = True
                    break
                matrix[i][j] = s[idx]
                i -= 1
                j += 1
                idx += 1
            if end:
                break
            
        return ''.join([''.join(row) for row in matrix])


if __name__ == '__main__':
    #s = "PAYPALISHIRING"
    #numRows = 4
    s = 'AB'
    numRows = 1
    print Solution().convert(s, numRows)

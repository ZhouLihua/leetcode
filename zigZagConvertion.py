class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        Frequency function, T = numRows + (numRows - 2)
        """
        strLength = len(s)
        if strLength <= numRows or numRows < 2:
            return s
        index = 0
        frequent = 2 * numRows - 2
        rows = [[] for _ in range(numRows)]
        while index < strLength:
            order = index % frequent
            if order < numRows:
                rows[order].append(s[index])
            else:
                rows[frequent - order].append(s[index])
            index += 1
        return "".join(["".join(rows[x]) for x in range(numRows)])


if __name__ == "__main__":
    solution = Solution()
    # expect "PAHNAPLSIIGYIR"
    print solution.convert("PAYPALISHIRING", 3)
    print solution.convert("PAYPALISHIRING", 1)
"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        index = 0
        totalLen = len(str)
        if totalLen == 0:
            return 0
        #skip first white spaces
        while index < totalLen and str[index] == " ":
            index += 1
        # only has white space
        if index == totalLen:
            return 0
        # first character is a word
        if str[index] not in ("+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return 0
        start = index
        # skip the first sign
        if str[index] in ("+", "-"):
            index += 1
        while index < totalLen:
            if str[index] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                index += 1
            else:
                break
        maxInt = (2 << 30) -1
        minInt = -(2 << 30)
        result = str[start:index]
        # only has + or - character
        try:
            result_int = int(result)
            if result_int < minInt:
                return minInt
            if result_int > maxInt:
                return maxInt
            return result_int
        except ValueError:
            return 0


if __name__ == "__main__":
    solution = Solution()
    print solution.myAtoi("    42")
    print solution.myAtoi("42")
    print solution.myAtoi("4193 with words")
    print solution.myAtoi("words and 987")
    print solution.myAtoi("-91283472332")
    print solution.myAtoi("-5-")

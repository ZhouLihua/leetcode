class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        slength = len(s)
        result = 0
        while index < slength:
            if s[index] == "I":
                if index + 1 < slength and s[index + 1] == "V":
                    result += 4
                    index += 2
                    continue
                if index + 1 < slength and s[index + 1] == "X":
                    result += 9
                    index += 2
                    continue
                else:
                    result += 1
                    index += 1
                    continue
            if s[index] == "X":
                if index + 1 < slength and s[index+1] == "L":
                    result += 40
                    index += 2
                    continue
                if index + 1 < slength and s[index+1] == "C":
                    result += 90
                    index += 2
                    continue
                else:
                    result += 10
                    index += 1
                    continue
            if s[index] == "C":
                if index + 1 < slength and s[index + 1] == "D":
                    result += 400
                    index += 2
                    continue
                if index + 1 < slength and s[index + 1] == "M":
                    result += 900
                    index += 2
                    continue
                else:
                    result += 100
                    index += 1
                    continue
            if s[index] == "V":
                result += 5
                index += 1
                continue
            if s[index] == "L":
                result += 50
                index += 1
                continue
            if s[index] == "D":
                result += 500
                index += 1
                continue
            if s[index] == "M":
                result += 1000
                index += 1
                continue
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("IX") == 9
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
